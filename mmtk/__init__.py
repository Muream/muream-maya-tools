import logging
import os
import maya.cmds as cmds
import mmtk.common.shelf as shelf


logger = logging.getLogger(__name__)


def setup():
    shelf_icon_path = os.path.join(os.path.dirname(__file__), 'common', 'shelf', 'icons')
    cmds.evalDeferred("shelf.ShelfMMTK('MMTK', icon_path='{}/')".format(shelf_icon_path))
    logger.info("Setup for Muream Maya Toolkit done.")

