import logging
import sys
import os

import maya.cmds as cmds
from maya.utils import executeDeferred

logger = logging.getLogger(__name__)


def initialize():
    init_now()
    executeDeferred(init_deferred)


def init_now():
    sys.dont_write_bytecode = True
    cmds.commandPort(n="localhost:7001", stp="mel", echoOutput=True)
    init_cosmos()


def init_deferred():
    init_hotkeys()
    init_viewport()

    logger.info("Muream Maya Tools initialized.")


def init_cosmos():
    if "cosmos" in sys.modules:
        import cosmos

        current_directory = os.path.dirname(__file__)

        cosmos_actions_path = os.path.abspath(
            os.path.join(current_directory, "cosmos-actions")
        )

        path_string = cosmos.prefs.getGenericSettings("scriptPath")
        paths = path_string.split(";")

        if cosmos_actions_path not in path_string:
            paths.append(cosmos_actions_path)

        path_string = ";".join(paths)
        cosmos.prefs.writegenericSettings("scriptPath", path_string)


def init_hotkeys():
    if not "hotkeys" in cmds.hotkeySet(q=True, hotkeySetArray=True):
        cmds.hotkeySet(
            edit=True, ip=os.path.join(os.path.dirname(__file__), "hotkeys.mhk")
        )


def init_viewport():
    cmds.grid(
        divisions=10,
        displayAxes=True,
        displayAxesBold=True,
        displayDivisionLines=True,
        displayGridLines=True,
        displayOrthographicLabels=True,
        displayPerspectiveLabels=False,
        size=100,
        spacing=10,
    )
    cmds.displayColor("gridAxis", 12)  # Axes color
    cmds.displayColor("gridHighlight", 1)  # Grid lines & numbers color
    cmds.displayColor("grid", 2)  # Subdivision lines color
    cmds.displayRGBColor("background", 0.168, 0.168, 0.168)

    try:
        cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 1)
    except:
        logger.warning("Couldn't set Anti-aliasing")
