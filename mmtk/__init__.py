import logging
import os
import site

import maya.cmds as cmds
from maya.utils import executeDeferred
from .default import init_defaults
import mmtk.common.shelf as shelf


logger = logging.getLogger(__name__)


def setup():
    add_vendors_to_path()
    add_cosmos_action_path()
    executeDeferred(create_mmtk_shelf)
    executeDeferred(init_defaults)
    load_bifrost()

    logger.info("Setup for Muream Maya Toolkit done.")


def add_vendors_to_path():
    vendor_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "vendor")
    )

    site.addsitedir(vendor_dir)


def add_cosmos_action_path():
    try:
        import cosmos
    except:
        pass
    else:
        cosmos_actions_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "cosmos-actions")
        )
        path_string = cosmos.prefs.getGenericSettings("scriptPath")
        path_string += ";" + cosmos_actions_path
        cosmos.prefs.writegenericSettings("scriptPath", path_string)


def create_mmtk_shelf():
    shelf_icon_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "icons")
    )
    shelf.ShelfMMTK("MMTK", icon_path=shelf_icon_path)


def load_bifrost():
    config_path = os.path.join(os.path.dirname(__file__), "bifrost", "config.json")
    os.environ["BIFROST_LIB_CONFIG_FILES"] += ";" + config_path
