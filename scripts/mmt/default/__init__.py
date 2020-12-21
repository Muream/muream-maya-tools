import logging
import sys
import os

import maya.cmds as cmds
from maya.utils import executeDeferred
from mmt.common.shelf import ShelfMMT

logger = logging.getLogger(__name__)


def initialize():
    init()
    executeDeferred(init_deferred)


def init():
    sys.dont_write_bytecode = True
    init_cosmos()  # cosmos can't be imported in a deferred call


def init_deferred():
    init_hotkeys()
    # init_shelf()
    init_viewport()

    logger.info("Muream Maya Toolkit initialized.")


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


def init_shelf():
    shelf_icon_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "icons")
    )
    ShelfMMT("MMT", icon_path=shelf_icon_path)


def init_hotkeys():
    if not "hotkeys" in cmds.hotkeySet(q=True, hotkeySetArray=True):
        cmds.hotkeySet(
            edit=True, ip=os.path.join(os.path.dirname(__file__), "hotkeys.mhk")
        )


def init_viewport():
    cmds.grid(
        divisions=4,
        displayAxes=True,
        displayAxesBold=True,
        displayDivisionLines=True,
        displayGridLines=True,
        displayOrthographicLabels=True,
        displayPerspectiveLabels=False,
        size=100,
        spacing=10,
    )
    cmds.displayColor("gridAxis", 15)  # Axes color
    cmds.displayColor("gridHighlight", 1)  # Grid lines & numbers color
    cmds.displayColor("grid", 2)  # Subdivision lines color

    try:
        cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 1)
    except:
        logger.warning("Couldn't set Anti-aliasing")