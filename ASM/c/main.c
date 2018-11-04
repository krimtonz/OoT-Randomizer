#include "dungeon_info.h"
#include "file_select.h"
#include "gfx.h"
#include "text.h"
#include "util.h"
#include "z64.h"

static uint16_t pad_pressed_raw, 
	pad, 
	pad_pressed;

void c_init() {
	pad_pressed_raw = 0;
	pad = 0;
	pad_pressed = 0;
    heap_init();
    gfx_init();
    text_init();
}

void zu_execute_game(int16_t entrance_index, uint16_t cutscene_index)
{
	z64_file.entrance_index = entrance_index;
	z64_file.cutscene_index = cutscene_index;
	z64_file.interface_flag = 0;
	if (z64_file.minigame_state == 1)
		z64_file.minigame_state = 3;
	z64_game.entrance_index = entrance_index;
	z64_ctxt.state_continue = 0;
	z64_ctxt.next_ctor = z64_state_ovl_tab[3].vram_ctor;
	z64_ctxt.next_size = z64_state_ovl_tab[3].ctxt_size;
}

void c_after_game_state_update() {
    if (z64_game.pause_state == 6 &&
                z64_game.pause_screen == 0 &&
                !z64_game.pause_screen_changing &&
                z64_ctxt.input[0].raw.a) {
        z64_disp_buf_t *db = &(z64_ctxt.gfx->overlay);
        draw_dungeon_info(db);
    }

	uint16_t z_pad = z64_input_direct.raw.pad;
	pad_pressed_raw = (pad ^ z_pad) & z_pad;
	pad = z_pad;
	pad_pressed = 0;
	for (int i = 0; i < 16; ++i) {
		uint16_t p = 1 << i;
		if ((pad_pressed_raw & p))
			pad_pressed |= p;
	}

	if (pad_pressed & 0x0800) {
		int age = z64_file.link_age;
		z64_file.link_age = z64_game.link_age;
		z64_game.link_age = !z64_game.link_age;
		z64_SwitchAgeEquips();
		z64_file.link_age = age;
		for (int i = 0; i < 4; ++i)
			if (z64_file.button_items[i] != Z64_ITEM_NULL)
				z64_UpdateItemButton(&z64_game, i);
		z64_UpdateEquipment(&z64_game, &z64_link);



		zu_execute_game(z64_file.entrance_index, 0x0000);

	}

	if (z64_file.link_age==0) {

		if (pad_pressed & 0x0200 && z64_file.iron_boots) {
			if (z64_file.equip_boots == 2) z64_file.equip_boots = 1;
			else z64_file.equip_boots = 2;
			z64_UpdateEquipment(&z64_game, &z64_link);
		}

		if ((pad_pressed & 0x0100) && z64_file.hover_boots) {
			if (z64_file.equip_boots == 3) z64_file.equip_boots = 1;
			else z64_file.equip_boots = 3;
			z64_UpdateEquipment(&z64_game, &z64_link);
		}

		
	}
}
