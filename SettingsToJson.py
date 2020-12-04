from SettingsList import setting_infos, setting_map, get_setting_info, get_settings_from_section, get_settings_from_tab
from Utils import data_path
import sys
import json
import copy


tab_keys     = ['text', 'app_type', 'footer']
section_keys = ['text', 'is_colors', 'is_sfx', 'col_span', 'row_span', 'subheader']
setting_keys = ['hide_when_disabled', 'min', 'max', 'size', 'max_length', 'file_types', 'no_line_break', 'function']
types_with_options = ['Checkbutton', 'Radiobutton', 'Combobox', 'SearchBox']


def RemoveTrailingLines(text):
    while text.endswith('<br>'):
        text = text[:-4]
    while text.startswith('<br>'):
        text = text[4:]
    return text


def deep_update(source, new_dict):
    for k, v in new_dict.items():
        if isinstance(v, dict):
            source[k] = deep_update(source.get(k, { }), v)
        elif isinstance(v, list):
            source[k] = (source.get(k, []) + v)
        else:
            source[k] = v
    return source


def GetSettingJson(setting, web_version, as_array=False):
    try:
        setting_info = get_setting_info(setting)
    except KeyError:
        if as_array:
            return {'name': setting}
        else:
            return {}

    if setting_info.gui_text is None:
        return None

    settingJson = {
        'options':       [],
        'default':       setting_info.default,
        'text':          setting_info.gui_text,
        'tooltip':       RemoveTrailingLines('<br>'.join(line.strip() for line in setting_info.gui_tooltip.split('\n'))),
        'type':          setting_info.gui_type,
        'shared':        setting_info.shared,
    }

    if as_array:
        settingJson['name'] = setting_info.name
    else:
        settingJson['current_value'] = setting_info.default

    setting_disable = {}
    if setting_info.disable != None:
        setting_disable = copy.deepcopy(setting_info.disable)

    for key, value in setting_info.gui_params.items():
        if key.startswith('web:'):
            if web_version:
                key = key[4:]
            else:
                continue
        if key.startswith('electron:'):
            if not web_version:
                key = key[9:]
            else:
                continue

        if key in setting_keys:
            settingJson[key] = value
        if key == 'disable':
            for option,types in value.items():
                for s in types.get('settings', []):
                    if get_setting_info(s).shared:
                        raise ValueError(f'Cannot disable setting {s}. Disabling "shared" settings in the gui_params is forbidden. Use the non gui_param version of disable instead.')
                for section in types.get('sections', []):
                    for s in get_settings_from_section(section):
                        if get_setting_info(s).shared:
                            raise ValueError(f'Cannot disable setting {s} in {section}. Disabling "shared" settings in the gui_params is forbidden. Use the non gui_param version of disable instead.')
                for tab in types.get('tabs', []):
                    for s in get_settings_from_tab(tab):
                        if get_setting_info(s).shared:
                            raise ValueError(f'Cannot disable setting {s} in {tab}. Disabling "shared" settings in the gui_params is forbidden. Use the non gui_param version of disable instead.')
            deep_update(setting_disable, value)


    if settingJson['type'] in types_with_options:
        if as_array:
            settingJson['options'] = []
        else:
            settingJson['options'] = {}

        tags_list = []

        for option_name in setting_info.choice_list:
            if as_array:
                optionJson = {
                    'name':     option_name,
                    'text':     setting_info.choices[option_name],
                }
            else:
                optionJson = {
                    'text':     setting_info.choices[option_name],
                }

            if option_name in setting_disable:
                disable_option = setting_disable[option_name]
                if disable_option.get('settings') != None:
                    optionJson['controls_visibility_setting'] = ','.join(disable_option['settings'])
                if disable_option.get('sections') != None:
                    optionJson['controls_visibility_section'] = ','.join(disable_option['sections'])
                if disable_option.get('tabs') != None:
                    optionJson['controls_visibility_tab'] = ','.join(disable_option['tabs'])

            option_tooltip = setting_info.gui_params.get('choice_tooltip', {}).get(option_name, None)
            if option_tooltip != None:
                optionJson['tooltip'] = RemoveTrailingLines('<br>'.join(line.strip() for line in option_tooltip.split('\n')))

            option_filter = setting_info.gui_params.get('filterdata', {}).get(option_name, None)
            if option_filter != None:
                optionJson['tags'] = option_filter
                for tag in option_filter:
                    if tag not in tags_list:
                        tags_list.append(tag)

            if as_array:
                settingJson['options'].append(optionJson)
            else:
                settingJson['options'][option_name] = optionJson

        if tags_list:
            tags_list.sort()
            settingJson['tags'] = ['(all)'] + tags_list
            settingJson['filter_by_tag'] = True

    return settingJson


def GetSectionJson(section, web_version, as_array=False):
    if as_array:
        sectionJson = {
            'name'     : section['name'],
            'settings' : []
        }
    else:
        sectionJson = {
            'settings' : {}
        }

    for key, value in section.items():
        if key in section_keys:
            sectionJson[key] = value

    for setting in section['settings']:
        settingJson = GetSettingJson(setting, web_version, as_array)
        if as_array:
            sectionJson['settings'].append(settingJson)
        else:
            sectionJson['settings'][setting] = settingJson

    return sectionJson


def GetTabJson(tab, web_version, as_array=False):
    if as_array:
        tabJson = {
            'name'     : tab['name'],
            'sections' : []
        }
    else:
        tabJson = {
            'sections' : {}
        }

    for key, value in tab.items():
        if key in tab_keys:
            tabJson[key] = value

    for section in tab['sections']:
        sectionJson = GetSectionJson(section, web_version, as_array)
        if as_array:
            tabJson['sections'].append(sectionJson)
        else:
            tabJson['sections'][section['name']] = sectionJson

    return tabJson


def CreateJSON(path, web_version=False):
    settingOutputJson = {
        'settingsObj'   : {},
        'settingsArray' : [],
        'cosmeticsObj'  : {},
        'cosmeticsArray': [],
    }

    for tab in setting_map['Tabs']:
        if tab.get('exclude_from_web', False) and web_version:
            continue
        elif tab.get('exclude_from_electron', False) and not web_version:
            continue

        tabJsonObj = GetTabJson(tab, web_version, as_array=False)
        tabJsonArr = GetTabJson(tab, web_version, as_array=True)

        settingOutputJson['settingsObj'][tab['name']] = tabJsonObj
        settingOutputJson['settingsArray'].append(tabJsonArr)
        if tab.get('is_cosmetics', False):
            settingOutputJson['cosmeticsObj'][tab['name']] = tabJsonObj
            settingOutputJson['cosmeticsArray'].append(tabJsonArr)

    with open(path, 'w') as f:
        json.dump(settingOutputJson, f)

 
def settingToJsonMain():
    web_version = '--web' in sys.argv
    CreateJSON(data_path('generated/settings_list.json'), web_version)


if __name__ == '__main__':
    settingToJsonMain()
