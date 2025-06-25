import xml.etree.ElementTree as ET
import os


class MissionDef:
    def __init__(self, var_1775: bool, var_908: int, var_134: bool):
        self.var_1775 = var_1775
        self.var_908   = var_908
        self.var_134   = var_134

def _extract_from_swz(swz_path: str):
    if not os.path.isfile(swz_path):
        return None
    with open(swz_path, "r", encoding="utf-8") as f:
        text = f.read()
    start = text.find("<MissionTypes")
    end = text.find("</MissionTypes>")
    if start == -1 or end == -1:
        return None
    xml = text[start:end + len("</MissionTypes>")]
    return ET.fromstring(xml)


def load_mission_defs(path: str):
    if not os.path.isfile(path):
        # Fallback to the data extracted from Game.swz
        swz_root = _extract_from_swz("data/swz-files/Game.swz.txt")
        if swz_root is None:
            print(f"[missions] Missing {path}; using empty mission definitions")
            return [None]
        root = swz_root
    else:
        tree = ET.parse(path)
        root = tree.getroot()
    defs = [None]  # index 0 unused
    for node in root.findall('MissionType'):
        mid   = int(node.findtext('MissionID', '0'))
        ctr   = int(node.findtext('CompleteCount', '0'))
        timed = node.find('Timed') is not None
        oneshot = (ctr <= 1)
        # ensure list grows to mid
        while len(defs) <= mid:
            defs.append(None)
        defs[mid] = MissionDef(var_1775=oneshot, var_908=ctr, var_134=timed)
    # fill any gaps up to the max ID with dummy
    max_id = len(defs) - 1
    for i in range(1, max_id+1):
        if defs[i] is None:
            defs[i] = MissionDef(False, 1, False)
    return defs

# at module scope:
var_238 = load_mission_defs('data/MissionTypes.txt')


