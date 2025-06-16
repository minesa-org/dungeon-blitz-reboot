# Character.py

import os
import json
from BitUtils import BitBuffer

# Default gear definitions
DEFAULT_GEAR = {
    "paladin": [
        [1, 0, 0, 0, 0, 0],  # Shield
        [13, 0, 0, 0, 0, 0],  # Sword
        [0, 0, 0, 0, 0, 0],   # Gloves
        [0, 0, 0, 0, 0, 0],   # Hat
        [0, 0, 0, 0, 0, 0],   # Armor
        [0, 0, 0, 0, 0, 0],   # Boots
    ],
    "rogue": [
        [39, 0, 0, 0, 0, 0],  # Off Hand/Shield
        [27, 0, 0, 0, 0, 0],  # Sword
        [0, 0, 0, 0, 0, 0],   # Gloves
        [0, 0, 0, 0, 0, 0],   # Hat
        [0, 0, 0, 0, 0, 0],   # Armor
        [0, 0, 0, 0, 0, 0],   # Boots
    ],
    "mage": [
        [53, 0, 0, 0, 0, 0],  # Staff
        [65, 0, 0, 0, 0, 0],  # Focus/Shield
        [0, 0, 0, 0, 0, 0],   # Gloves
        [0, 0, 0, 0, 0, 0],    # Hat
        [0, 0, 0, 0, 0, 0],   # Robe
        [0, 0, 0, 0, 0, 0],   # Boots
    ],
}

# Default building configuration
DEFAULT_BUILDINGS = [
    {
        "buildingID": 2,
        "displayName": "Magic Forge",
        "type": "forge",
        "rank": 2,
        "playerLevel": 5,
        "goldCost": 100,
        "idolCost": 5,
        "upgradeTime": 5,
        "art": "a_Upgrade_Forge_0",
        "backgroundArt": "a_Upgrade_Forge_0",
        "upgradeIcon": "a_ForgeUpgradeIcon"
    }
]

# Default learned abilities
DEFAULT_ABILITIES = [
    {"abilityID": 27, "rank": 1},
    {"abilityID": 1692, "rank": 1},
    {"abilityID": 20, "rank": 1},
    {"abilityID": 21, "rank": 1},
    {"abilityID": 81, "rank": 1},
    {"abilityID": 447, "rank": 1}
]

CHAR_SAVE_DIR = "saves"

def load_characters(user_id: str) -> list[dict]:
    """Load the list of characters for a given user_id."""
    path = os.path.join(CHAR_SAVE_DIR, f"{user_id}.json")
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("characters", [])

def save_characters(user_id: str, char_list: list[dict]):
    """Save the list of characters for a given user_id, preserving other fields."""
    os.makedirs(CHAR_SAVE_DIR, exist_ok=True)
    path = os.path.join(CHAR_SAVE_DIR, f"{user_id}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"email": None, "characters": []}
    data["characters"] = char_list
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def default_master_for_base(base_cls: str) -> str:
    """Return the default MasterClass name for a given base class."""
    return {
        "Paladin": "Sentinel",
        "Rogue": "Executioner",
        "Mage": "Frostwarden"
    }.get(base_cls, "")

def make_character_dict_from_tuple(character):
    (name, class_name, level,
     gender, head, hair, mouth, face,
     hair_color, skin_color, shirt_color, pant_color,
     equipped_gear) = character

    cls = class_name.lower()

    # Handle equipped gear
    if (isinstance(equipped_gear, (list, tuple))
        and len(equipped_gear) == 6
        and all(isinstance(slot, (list, tuple)) and len(slot) == 6
                for slot in equipped_gear)):
        gear_list = [list(slot) for slot in equipped_gear]
    else:
        gear_list = [list(slot) for slot in DEFAULT_GEAR.get(cls, [[0]*6]*6)]

    # Assemble the complete character dictionary
    return {
        "name": name,
        "class": class_name,
        "level": level,
        "gender": gender or "Male",
        "headSet": head or "Head01",
        "hairSet": hair or "Hair01",
        "mouthSet": mouth or "Mouth01",
        "faceSet": face or "Face01",
        "hairColor": hair_color,
        "skinColor": skin_color,
        "shirtColor": shirt_color,
        "pantColor": pant_color,
        "gearList": gear_list,
        "xp": 23000 if level > 1 else 1,
        "gold": 100000,
        "Gems": 100000,
        "DragonOre": 100000,
        "mammothIdols": 100000,
        "DragonKeys": 100000,
        "SilverSigils": 100000,
        "showHigher": True,
        "MasterClass": default_master_for_base(class_name),
        "ability": [{
            "abilityID": 19,
            "baseClass": "Paladin",
            "hotbarLocation": 1,
            "category": "Vindication",
            "goldCost": 219,
            "idolCost": 1,
            "upgradeTime": 20,
            "type": "attack",
            "rank": 1
        }],
        "inventoryGears": [
            {"gearID": 1, "tier": 1, "runes": [1, 2, 3], "colors": [255, 0]},
            {"gearID": 13, "tier": 2, "runes": [0, 0, 0], "colors": [0, 128]},
            {"gearID": 30, "tier": 0, "runes": [0, 0, 0], "colors": [0, 0]}
        ],
        "building": DEFAULT_BUILDINGS,
        "learnedAbilities": DEFAULT_ABILITIES
    }

def build_paperdoll_packet(character_dict):
    buf = BitBuffer()
    buf.write_utf_string(character_dict["name"])
    buf.write_utf_string(character_dict["class"])
    buf.write_utf_string(character_dict["gender"])
    buf.write_utf_string(character_dict["headSet"])
    buf.write_utf_string(character_dict["hairSet"])
    buf.write_utf_string(character_dict["mouthSet"])
    buf.write_utf_string(character_dict["faceSet"])
    buf.write_bits(character_dict["hairColor"], 24)
    buf.write_bits(character_dict["skinColor"], 24)
    buf.write_bits(character_dict["shirtColor"], 24)
    buf.write_bits(character_dict["pantColor"], 24)

    for slot in character_dict.get("gearList", []):
        buf.write_bits(slot[0], 11)  # Write only GearID

    return buf.to_bytes()

def build_login_character_list_bitpacked(characters):
    """Builds the 0x15 login-character-list packet."""
    buf = BitBuffer()
    buf.write_method_4(1)  # user_id (will be overwritten)
    buf.write_method_393(8)  # max_chars
    buf.write_method_393(len(characters))  # char_count

    for char in characters:
        buf.write_utf_string(char["name"])
        buf.write_utf_string(char["class"])
        buf.write_method_6(char["level"], 6)

    import struct
    header = struct.pack(">HH", 0x15, len(buf.to_bytes()))
    return header + buf.to_bytes()