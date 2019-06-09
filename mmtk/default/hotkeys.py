import maya.cmds as cmds


def init_hotkeys():
    if not 'hotkeys' in cmds.hotkeySet(q=True, hotkeySetArray=True):
        cmds.hotkeySet(edit=True, ip='/home/muream/projects/muream-maya-toolkit/mmtk/default/hotkeys.mhk');

