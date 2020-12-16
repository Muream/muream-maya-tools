import os
import maya.cmds as cmds


def init_hotkeys():
    if not "hotkeys" in cmds.hotkeySet(q=True, hotkeySetArray=True):
        cmds.hotkeySet(
            edit=True, ip=os.path.join(os.path.dirname(__file__), "hotkeys.mhk")
        )
