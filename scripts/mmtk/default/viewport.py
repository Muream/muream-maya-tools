import logging
import maya.cmds as cmds


logger = logging.getLogger(__name__)


def init_grid():
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


def enable_anti_aliasing():
    try:
        cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 1)
    except:
        print("Couldn't set Anti-aliasing")


def init_viewport():
    init_grid()
    enable_anti_aliasing()
