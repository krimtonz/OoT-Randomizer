import logging

from BaseClasses import Item


def ItemFactory(items):
    ret = []
    singleton = False
    if isinstance(items, str):
        items = [items]
        singleton = True
    for item in items:
        if item in item_table:
            advancement, priority, type, code, index, object, model = item_table[item]
            ret.append(Item(item, advancement, priority, type, code, index, object, model))
        else:
            logging.getLogger('').warning('Unknown Item: %s', item)
            return None

    if singleton:
        return ret[0]
    return ret


class ShopData(object):
    def __init__(self, model, gid, price):
        self.model = model
        self.gid = gid
        self.price = price


# Format: Name: (Advancement, Priority, Type, ItemCode, Index)
item_table = {
    'Bow': (True, False, None, None, 0x83, 0x00E9, 0x35),
    'Progressive Hookshot': (True, False, None, None, 0x80, 0x00DD, 0x2D),
    'Hammer': (True, False, None, 0x01A0, 0x0D, 0x00F6, 0x41),
    'Slingshot': (True, False, None, None, 0x84, 0x00E7, 0x33),
    'Boomerang': (True, False, None, 0x00C0, 0x06, 0x00E8, 0x34),
    'Bomb Bag': (True, False, None, None, 0x82, 0x00BF, 0x18),
    'Lens of Truth': (True, False, None, 0x0140, 0x0A, 0x00EA, 0x36),
    'Dins Fire': (True, False, None, 0x0B80, 0x5C, 0x015D, 0x64),
    'Farores Wind': (True, False, None, 0x0BA0, 0x5D, 0x015D, 0x65),
    'Nayrus Love': (True, False, None, 0x0BC0, 0x5E, 0x015D, 0x66),
    'Fire Arrows': (True, False, None, 0x0B00, 0x58, 0x0158, 0x60),
    'Ice Arrows': (True, False, None, 0x0B20, 0x59, 0x0158, 0x61),
    'Light Arrows': (True, False, None, 0x0B40, 0x5A, 0x0158, 0x62),
    'Fairy Ocarina': (True, False, None, 0x0760, 0x3B, 0x010E, 0x46),
    'Ocarina of Time': (True, False, None, 0x0180, 0x0C, 0x00DE, 0x2F),
    'Ocarina': (True, False, None, 0x0180, 0xC3, 0x00DE, 0x2F),
    'Bottle': (True, False, None, 0x01E0, 0x0F, 0x00C6, 0x01),
    'Bottle with Letter': (True, False, None, 0x02A0, 0x15, 0x010B, 0x45),
    'Bottle with Milk': (True, False, None, 0x0280, 0x14, 0x00DF, 0x30),
    'Bottle with Red Potion': (True, False, None, None, 0x89, 0x00C6, 0x01),
    'Bottle with Green Potion': (True, False, None, None, 0x8A, 0x00C6, 0x01),
    'Bottle with Blue Potion': (True, False, None, None, 0x8B, 0x00C6, 0x01),
    'Bottle with Fairy': (True, False, None, None, 0x8C, 0x00C6, 0x01),
    'Bottle with Fish': (True, False, None, None, 0x8D, 0x00C6, 0x01),
    'Bottle with Blue Fire': (True, False, None, None, 0x8E, 0x00C6, 0x01),
    'Bottle with Bugs': (True, False, None, None, 0x8F, 0x00C6, 0x01),
    'Bottle with Poe': (True, False, None, None, 0x91, 0x00C6, 0x01),
    'Weird Egg': (True, False, None, 0x08E0, 0x47, 0x00DA, 0x29),
    'Pocket Egg': (True, False, None, 0x03A0, 0x1D, 0x00DA, 0x29),
    'Pocket Cucco': (True, False, None, 0x03C0, 0x1E, 0x0109, 0x44),
    'Cojiro': (True, False, None, 0x01C0, 0x0E, 0x0109, 0x5E),
    'Odd Mushroom': (True, False, None, 0x03E0, 0x1F, 0x0141, 0x54),
    'Odd Potion': (True, False, None, 0x0400, 0x20, 0x0140, 0x53),
    'Poachers Saw': (True, False, None, 0x0420, 0x21, 0x00F5, 0x40),
    'Broken Sword': (True, False, None, 0x0440, 0x22, 0x0143, 0x56),
    'Prescription': (True, False, None, 0x0460, 0x23, 0x0146, 0x57),
    'Eyeball Frog': (True, False, None, 0x0480, 0x24, 0x0149, 0x5A),
    'Eyedrops': (True, False, None, 0x04A0, 0x25, 0x013F, 0x52),
    'Claim Check': (True, False, None, 0x04C0, 0x26, 0x0142, 0x55),
    'Kokiri Sword': (True, False, None, 0x04E0, 0x27, 0x018D, 0x74),
    'Master Sword': (True, False, None, None, None, None, None),
    'Biggoron Sword': (True, False, None, None, 0xB5, 0x00F8, 0x43),
    'Deku Shield': (False, False, None, 0x0520, 0x29, 0x00CB, 0x1D),
    'Hylian Shield': (False, False, None, 0x0540, 0x2A, 0x00DC, 0x2C),
    'Mirror Shield': (True, False, None, 0x0560, 0x2B, 0x00EE, 0x3A),
    'Goron Tunic': (True, False, None, 0x0580, 0x2C, 0x00F2, 0x3C),
    'Zora Tunic': (True, False, None, 0x05A0, 0x2D, 0x00F2, 0x3D),
    'Iron Boots': (True, False, None, 0x05C0, 0x2E, 0x0118, 0x47),
    'Hover Boots': (True, False, None, 0x05E0, 0x2F, 0x0157, 0x5F),
    'Progressive Strength Upgrade': (True, False, None, None, 0x81, 0x0147, 0x58),
    'Progressive Scale': (True, False, None, None, 0x86, 0x00DB, 0x2A),
    'Progressive Wallet': (True, False, None, None, 0x85, 0x00D1, 0x22),
    'Deku Stick Capacity': (False, False, None, None, 0x88, 0x00C7, 0x1B),
    'Deku Nut Capacity': (False, False, None, None, 0x87, 0x00BB, 0x12),
    'Magic Meter': (True, False, None, None, 0xC0, 0x00CD, 0x1E),
    'Double Defense': (False, False, None, None, 0xBF, 0x00BD, 0x13),
    'Stone of Agony': (True, False, None, 0x0720, 0x39, 0x00C8, 0x21),
    'Piece of Heart': (False, False, None, 0x07C0, 0x3E, 0x00BD, 0x14),
    'Heart Container': (False, False, None, 0x07A0, 0x3D, 0x00BD, 0x13),
    'Piece of Heart (Treasure Chest Game)': (False, False, None, None, 0x76, 0x00BD, 0x14),
    'Heart Container (Boss)': (False, False, None, None, 0x4F, 0x00BD, 0x13),
    'Recovery Heart': (False, False, None, None, 0xB6, 0x00B7, 0x09),
    'Arrows (5)': (False, False, None, None, 0xB7, 0x00D8, 0x25),
    'Arrows (10)': (False, False, None, None, 0xB8, 0x00D8, 0x26),
    'Arrows (30)': (False, False, None, None, 0xB9, 0x00D8, 0x27),
    'Bombs (5)': (False, False, None, None, 0xBA, 0x00CE, 0x20),
    'Bombs (10)': (False, False, None, None, 0xBB, 0x00CE, 0x20),
    'Bombs (20)': (False, False, None, None, 0xBC, 0x00CE, 0x20),
    'Bombchus (5)': (True, False, None, 0x0D40, 0x6A, 0x00D9, 0x28),
    'Bombchus (10)': (True, False, None, 0x0060, 0x03, 0x00D9, 0x28),
    'Bombchus (20)': (True, False, None, 0x0D60, 0x6B, 0x00D9, 0x28),
    'Bombchus': (True, False, None, None, 0xC2, 0x00D9, 0x28),
    'Deku Nuts (5)': (False, False, None, None, 0xBD, 0x00BB, 0x12),
    'Deku Nuts (10)': (False, False, None, None, 0xBE, 0x00BB, 0x12),
    'Rupee (1)': (False, False, None, 0x0980, 0x4C, 0x017F, 0x6D),
    'Rupees (5)': (False, False, None, 0x09A0, 0x4D, 0x017F, 0x6E),
    'Rupees (20)': (False, False, None, 0x09C0, 0x4E, 0x017F, 0x6F),
    'Rupees (50)': (False, False, None, 0x0AA0, 0x55, 0x017F, 0x71),
    'Rupees (200)': (False, False, None, 0x0AC0, 0x56, 0x017F, 0x72),
    'Skull Mask': (False, False, None, 0x02E0, 0x17, 0x0136, 0x4F),
    'Spooky Mask': (False, False, None, 0x0300, 0x18, 0x0135, 0x32),
    'Keaton Mask': (False, False, None, 0x0340, 0x1A, 0x0134, 0x31),
    'Bunny Hood': (False, False, None, 0x0360, 0x1B, 0x0137, 0x50),
    'Mask of Truth': (False, False, None, 0x0380, 0x1C, 0x0138, 0x51),
    'Goron Mask': (False, False, None, 0x0A20, 0x51, 0x0150, 0x5B),
    'Zora Mask': (False, False, None, 0x0A40, 0x52, 0x0151, 0x5C),
    'Gerudo Mask': (False, False, None, 0x0A60, 0x53, 0x0152, 0x5D),
    'Ice Trap': (False, True, None, 0x0F80, 0x7C, None, None),
    'Magic Bean': (True, False, None, 0x02C0, 0x16, 0x00F3, 0x3E),
    'Map': (False, False, 'Map', 0x0820, 0x41, 0x00C8, 0x1C),
    'Compass': (False, False, 'Compass', 0x0800, 0x40, 0x00B8, 0x0B),
    'Boss Key': (True, False, 'BossKey', 0x07E0, 0x3F, 0x00B9, 0x0A),
    'Small Key': (True, False, 'SmallKey', 0x0840, 0x42, 0x00AA, 0x02),
    'Boss Key (Forest Temple)': (True, False, 'BossKey', None, 0x92, 0x00B9, 0x0A),
    'Boss Key (Fire Temple)': (True, False, 'BossKey', None, 0x93, 0x00B9, 0x0A),
    'Boss Key (Water Temple)': (True, False, 'BossKey', None, 0x94, 0x00B9, 0x0A),
    'Boss Key (Spirit Temple)': (True, False, 'BossKey', None, 0x95, 0x00B9, 0x0A),
    'Boss Key (Shadow Temple)': (True, False, 'BossKey', None, 0x96, 0x00B9, 0x0A),
    'Boss Key (Ganons Castle)': (True, False, 'BossKey', None, 0x97, 0x00B9, 0x0A),
    'Compass (Deku Tree)': (False, False, 'Compass', None, 0x98, 0x00B8, 0x0B),
    'Compass (Dodongos Cavern)': (False, False, 'Compass', None, 0x99, 0x00B8, 0x0B),
    'Compass (Jabu Jabus Belly)': (False, False, 'Compass', None, 0x9A, 0x00B8, 0x0B),
    'Compass (Forest Temple)': (False, False, 'Compass', None, 0x9B, 0x00B8, 0x0B),
    'Compass (Fire Temple)': (False, False, 'Compass', None, 0x9C, 0x00B8, 0x0B),
    'Compass (Water Temple)': (False, False, 'Compass', None, 0x9D, 0x00B8, 0x0B),
    'Compass (Spirit Temple)': (False, False, 'Compass', None, 0x9E, 0x00B8, 0x0B),
    'Compass (Shadow Temple)': (False, False, 'Compass', None, 0x9F, 0x00B8, 0x0B),
    'Compass (Bottom of the Well)': (False, False, 'Compass', None, 0xA0, 0x00B8, 0x0B),
    'Compass (Ice Cavern)': (False, False, 'Compass', None, 0xA1, 0x00B8, 0x0B),
    'Map (Deku Tree)': (False, False, 'Map', None, 0xA2, 0x00C8, 0x1C),
    'Map (Dodongos Cavern)': (False, False, 'Map', None, 0xA3, 0x00C8, 0x1C),
    'Map (Jabu Jabus Belly)': (False, False, 'Map', None, 0xA4, 0x00C8, 0x1C),
    'Map (Forest Temple)': (False, False, 'Map', None, 0xA5, 0x00C8, 0x1C),
    'Map (Fire Temple)': (False, False, 'Map', None, 0xA6, 0x00C8, 0x1C),
    'Map (Water Temple)': (False, False, 'Map', None, 0xA7, 0x00C8, 0x1C),
    'Map (Spirit Temple)': (False, False, 'Map', None, 0xA8, 0x00C8, 0x1C),
    'Map (Shadow Temple)': (False, False, 'Map', None, 0xA9, 0x00C8, 0x1C),
    'Map (Bottom of the Well)': (False, False, 'Map', None, 0xAA, 0x00C8, 0x1C),
    'Map (Ice Cavern)': (False, False, 'Map', None, 0xAB, 0x00C8, 0x1C),
    'Small Key (Forest Temple)': (True, False, 'SmallKey', None, 0xAC, 0x00AA, 0x02),
    'Small Key (Fire Temple)': (True, False, 'SmallKey', None, 0xAD, 0x00AA, 0x02),
    'Small Key (Water Temple)': (True, False, 'SmallKey', None, 0xAE, 0x00AA, 0x02),
    'Small Key (Spirit Temple)': (True, False, 'SmallKey', None, 0xAF, 0x00AA, 0x02),
    'Small Key (Shadow Temple)': (True, False, 'SmallKey', None, 0xB0, 0x00AA, 0x02),
    'Small Key (Bottom of the Well)': (True, False, 'SmallKey', None, 0xB1, 0x00AA, 0x02),
    'Small Key (Gerudo Training Grounds)': (True, False, 'SmallKey', None, 0xB2, 0x00AA, 0x02),
    'Small Key (Gerudo Fortress)': (True, False, 'FortressSmallKey', None, 0xB3, 0x00AA, 0x02),
    'Small Key (Ganons Castle)': (True, False, 'SmallKey', None, 0xB4, 0x00AA, 0x02),
    'Zeldas Letter': (True, False, None, None, None, None, None),
    'Zeldas Lullaby': (True, False, 'Song', [0x0A, 0x5], 0xCA, 0x00B6, 0x04),
    'Eponas Song': (True, False, 'Song', [0x09, 0x4], 0xCB, 0x00B6, 0x06),
    'Suns Song': (True, False, 'Song', [0x0B, 0x2], 0xCD, 0x00B6, 0x08),
    'Sarias Song': (True, False, 'Song', [0x08, 0x3], 0xCC, 0x00B6, 0x03),
    'Song of Time': (True, False, 'Song', [0x0C, 0x1], 0xCE, 0x00B6, 0x05),
    'Song of Storms': (True, False, 'Song', [0x0D, 0x0], 0xCF, 0x00B6, 0x07),
    'Minuet of Forest': (True, False, 'Song', [0x02, 0xB], 0xC4, 0x00B6, 0x03),
    'Prelude of Light': (True, False, 'Song', [0x07, 0x6], 0xC9, 0x00B6, 0x08),
    'Bolero of Fire': (True, False, 'Song', [0x03, 0xA], 0xC5, 0x00B6, 0x04),
    'Serenade of Water': (True, False, 'Song', [0x04, 0x9], 0xC6, 0x00B6, 0x05),
    'Nocturne of Shadow': (True, False, 'Song', [0x06, 0x7], 0xC8, 0x00B6, 0x07),
    'Requiem of Spirit': (True, False, 'Song', [0x05, 0x8], 0xC7, 0x00B6, 0x08),
    'Gold Skulltulla Token': (True, False, 'Token', None, 0x5B, 0x015C, 0x63),
    'Epona': (True, False, 'Event', None, None, None, None),
    'Carpenter Rescue': (True, False, 'Event', None, None, None, None),
    'Gerudo Membership Card': (True, False, None, 0x0740, 0x3A, 0x00D7, 0x24),
    'Kokiri Emerald': (True, False, 'Event', 0x6C, None, None, None),
    'Goron Ruby': (True, False, 'Event', 0x6D, None, None, None),
    'Zora Sapphire': (True, False, 'Event', 0x6E, None, None, None),
    'Forest Medallion': (True, False, 'Event', 0x66, None, None, None),
    'Fire Medallion': (True, False, 'Event', 0x67, None, None, None),
    'Water Medallion': (True, False, 'Event', 0x68, None, None, None),
    'Spirit Medallion': (True, False, 'Event', 0x69, None, None, None),
    'Shadow Medallion': (True, False, 'Event', 0x6A, None, None, None),
    'Light Medallion': (True, False, 'Event', 0x6B, None, None, None),
    'Forest Trial Clear': (True, False, 'Event', None, None, None, None),
    'Fire Trial Clear': (True, False, 'Event', None, None, None, None),
    'Water Trial Clear': (True, False, 'Event', None, None, None, None),
    'Shadow Trial Clear': (True, False, 'Event', None, None, None, None),
    'Spirit Trial Clear': (True, False, 'Event', None, None, None, None),
    'Light Trial Clear': (True, False, 'Event', None, None, None, None),
    'Triforce': (True, False, 'Event', None, None, None, None),
    'Buy Deku Nut (5)': (False, True, 'Shop', None, 0x00, 0x00BB, 0x12), 
    'Buy Arrows (30)': (False, True, 'Shop', None, 0x01, 0x00D8, 0x26), 
    #'Buy Arrows (50)': (False, True, 'Shop', None, 0x02, 0x00D8, 0x27), 
    'Buy Bombs (5)': (False, True, 'Shop', None, 0x03, 0x00CE, 0x20), 
    'Buy Deku Nut (10)': (False, True, 'Shop', None, 0x04, 0x00BB, 0x12), 
    'Buy Deku Stick (1)': (False, True, 'Shop', None, 0x05, 0x00C7, 0x1B), 
    'Buy Bombs (10)': (False, True, 'Shop', None, 0x06, 0x00CE, 0x20), 
    'Buy Fish': (False, True, 'Shop', None, 0x07, 0x00F4, 0x3F), 
    'Buy Red Potion': (False, True, 'Shop', None, 0x08, 0x00EB, 0x15), 
    'Buy Green Potion': (False, True, 'Shop', None, 0x09, 0x00EB, 0x16), 
    #'Buy Blue Potion': (False, True, 'Shop', None, 0x0A, 0x00EB, 0x17), 
    'Buy Hylian Shield': (True, False, 'Shop', None, 0x0C, 0x00DC, 0x2C), 
    'Buy Deku Shield': (True, False, 'Shop', None, 0x0D, 0x00CB, 0x1D), 
    'Buy Goron Tunic': (True, False, 'Shop', None, 0x0E, 0x00F2, 0x3C), 
    'Buy Zora Tunic': (True, False, 'Shop', None, 0x0F, 0x00F2, 0x3D), 
    'Buy Heart': (False, True, 'Shop', None, 0x10, 0x00B7, 0x09), 
    'Buy Bombchu (10)': (True, False, 'Shop', None, 0x15, 0x00D9, 0x28), 
    'Buy Bombchu (20)': (True, False, 'Shop', None, 0x16, 0x00D9, 0x28), 
    'Buy Bombchu (5)': (True, False, 'Shop', None, 0x18, 0x00D9, 0x28), 
    'Buy Deku Seeds (30)': (False, True, 'Shop', None, 0x1D, 0x0119, 0x48), 
    'Sold Out': (False, True, 'Shop', None, 0x26, 0x0148, 0x59), 
    'Buy Blue Fire': (True, False, 'Shop', None, 0x27, 0x0173, 0x67), 
    'Buy Bottle Bug': (False, True, 'Shop', None, 0x28, 0x0174, 0x68), 
    'Buy Fairy\'s Spirit': (False, True, 'Shop', None, 0x2B, 0x0177, 0x6B), 
    'Buy Arrow (10)': (False, True, 'Shop', None, 0x2C, 0x00D8, 0x25), 
    'Buy Bombs (20)': (False, True, 'Shop', None, 0x2D, 0x00CE, 0x20), 
    #'Buy Bombs (30)': (False, True, 'Shop', None, 0x2E, 0x00CE, 0x20), 
}

item_data = {
    'Hammer': [0x11, 0x80, 0x41, 0x38, 0x00, 0xF6],
    'Boomerang': [0x0E, 0x80, 0x34, 0x35, 0x00, 0xE8],
    'Lens of Truth': [0x0F, 0x80, 0x36, 0x39, 0x00, 0xEA],
    'Dins Fire': [0x05, 0x80, 0x64, 0xAD, 0x01, 0x5D],
    'Farores Wind': [0x0D, 0x80, 0x65, 0xAE, 0x01, 0x5D],
    'Nayrus Love': [0x13, 0x80, 0x66, 0xAF, 0x01, 0x5D],
    'Fire Arrows': [0x04, 0x80, 0x60, 0x70, 0x01, 0x58],
    'Ice Arrows': [0x0C, 0x80, 0x61, 0x71, 0x01, 0x58],
    'Light Arrows': [0x12, 0x80, 0x62, 0x72, 0x01, 0x58],
    'Bottle': [0x14, 0x80, 0x01, 0x42, 0x00, 0xC6],
    'Bottle with Letter': [0x1B, 0x80, 0x45, 0x99, 0x01, 0x0B],
    'Bottle with Milk': [0x1A, 0x80, 0x30, 0x98, 0x00, 0xDF],
    'Pocket Egg': [0x2D, 0x80, 0x29, 0x01, 0x00, 0xDA],
    'Pocket Cucco': [0x2E, 0x80, 0x44, 0x0B, 0x01, 0x09],
    'Cojiro': [0x2F, 0x80, 0x5E, 0x02, 0x01, 0x09],
    'Odd Mushroom': [0x30, 0x80, 0x54, 0x03, 0x01, 0x41],
    'Odd Potion': [0x31, 0x80, 0x53, 0x04, 0x01, 0x40],
    'Poachers Saw': [0x32, 0x80, 0x40, 0x05, 0x00, 0xF5],
    'Broken Sword': [0x33, 0x80, 0x56, 0x08, 0x01, 0x43],
    'Prescription': [0x34, 0x80, 0x57, 0x09, 0x01, 0x46],
    'Eyeball Frog': [0x35, 0x80, 0x5A, 0x0D, 0x01, 0x49],
    'Eyedrops': [0x36, 0x80, 0x52, 0x0E, 0x01, 0x3F],
    'Claim Check': [0x37, 0x80, 0x55, 0xA4, 0x01, 0x8D],
    'Kokiri Sword': [0x3B, 0x80, 0x74, 0xA4, 0x01, 0x8D],
    'Deku Shield': [0x3E, 0xA0, 0xE3, 0x4C, 0x00, 0xCB],
    'Hylian Shield': [0x3F, 0xA0, 0xD4, 0x4D, 0x00, 0xDC],
    'Mirror Shield': [0x40, 0x80, 0x3A, 0x4E, 0x00, 0xEE],
    'Goron Tunic': [0x42, 0xA0, 0x3C, 0x50, 0x00, 0xF2],
    'Zora Tunic': [0x43, 0xA0, 0x3D, 0x51, 0x00, 0xF2],
    'Iron Boots': [0x45, 0x80, 0x47, 0x53, 0x01, 0x18],
    'Hover Boots': [0x46, 0x80, 0x5F, 0x54, 0x01, 0x57],
    'Stone of Agony': [0x6F, 0x80, 0x21, 0x68, 0x00, 0xC8],
    'Piece of Heart': [0x7A, 0x80, 0x14, 0xC2, 0x00, 0xBD],
    'Recovery Heart': [0x83, 0x80, 0x09, 0x55, 0x00, 0xB7],
    'Arrows (5)': [0x92, 0x48, 0xDB, 0xE6, 0x00, 0xD8],
    'Arrows (10)': [0x93, 0x4A, 0xDA, 0xE6, 0x00, 0xD8],
    'Arrows (30)': [0x94, 0x4A, 0xD9, 0xE6, 0x00, 0xD8],
    'Bombs (5)': [0x8E, 0x59, 0xE0, 0x32, 0x00, 0xCE],
    'Bombs (10)': [0x8F, 0x59, 0xE0, 0x32, 0x00, 0xCE],
    'Bombs (20)': [0x90, 0x59, 0xE0, 0x32, 0x00, 0xCE],
    'Bombchus (5)': [0x96, 0x80, 0xD8, 0x33, 0x00, 0xD9],
    'Bombchus (10)': [0x09, 0x80, 0xD8, 0x33, 0x00, 0xD9],
    'Bombchus (20)': [0x97, 0x80, 0xD8, 0x33, 0x00, 0xD9],
    'Deku Nuts (5)': [0x8C, 0x0C, 0xEE, 0x34, 0x00, 0xBB],
    'Deku Nuts (10)': [0x8D, 0x0C, 0xEE, 0x34, 0x00, 0xBB],
    'Rupee (1)': [0x84, 0x00, 0x93, 0x6F, 0x01, 0x7F],
    'Rupees (5)': [0x85, 0x01, 0x92, 0xCC, 0x01, 0x7F],
    'Rupees (20)': [0x86, 0x02, 0x91, 0xF0, 0x01, 0x7F],
    'Rupees (50)': [0x87, 0x14, 0x8F, 0xF1, 0x01, 0x7F],
    'Rupees (200)': [0x88, 0x13, 0x8E, 0xF2, 0x01, 0x7F],
    'Skull Mask': [0x25, 0x80, 0x4F, 0x10, 0x01, 0x36 ],
    'Spooky Mask': [0x26, 0x80, 0x32, 0x11, 0x01, 0x35],
    'Keaton Mask': [0x24, 0x80, 0x31, 0x12, 0x01, 0x34],
    'Bunny Hood': [0x27, 0x80, 0x50, 0x13, 0x01, 0x37],
    'Mask of Truth': [0x2B, 0x80, 0x51, 0x17, 0x01, 0x38],
    'Goron Mask': [0x28, 0x80, 0x5B, 0x14, 0x01, 0x50],
    'Zora Mask': [0x29, 0x80, 0x5C, 0x15, 0x01, 0x51 ],
    'Gerudo Mask': [0x2A, 0x80, 0x5D, 0x16, 0x01, 0x52],
    'Ice Trap': [0x85, 0x01, 0x92, 0xCC, 0x01, 0x7F], # Ice Trap in special spots will become a blue rupee.
    'Zeldas Lullaby': 0xD4,
    'Eponas Song': 0xD2,
    'Suns Song': 0xD3,
    'Sarias Song': 0xD1,
    'Song of Time': 0xD5,
    'Song of Storms': 0xD6,
    'Minuet of Forest': 0x73,
    'Bolero of Fire': 0x74,
    'Serenade of Water': 0x75,
    'Nocturne of Shadow': 0x77,
    'Requiem of Spirit': 0x76,
    'Prelude of Light': 0x78,
    'Kokiri Emerald': [0x04, 0xA5, 0x80, [0x00, 0x04, 0x00, 0x00]],
    'Goron Ruby': [0x08, 0xA5, 0x81, [0x00, 0x08, 0x00, 0x00]],
    'Zora Sapphire': [0x10, 0xA5, 0x82, [0x00, 0x10, 0x00, 0x00]],
    'Forest Medallion': [0x01, 0xA7, 0x3E, [0x00, 0x00, 0x00, 0x01]],
    'Fire Medallion': [0x02, 0xA7, 0x3C, [0x00, 0x00, 0x00, 0x02]],
    'Water Medallion': [0x04, 0xA7, 0x3D, [0x00, 0x00, 0x00, 0x04]],
    'Spirit Medallion': [0x08, 0xA7, 0x3F, [0x00, 0x00, 0x00, 0x08]],
    'Shadow Medallion': [0x10, 0xA7, 0x41, [0x00, 0x00, 0x00, 0x10]],
    'Light Medallion': [0x20, 0xA7, 0x40, [0x00, 0x00, 0x00, 0x20]]}
