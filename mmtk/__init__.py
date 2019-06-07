import logging
import os
import sys

import maya.cmds as cmds


logger = logging.getLogger(__name__)


def setup():
    # add the vendored dir to the python path
    vendor_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vendor'))
    sys.path.append(vendor_dir)
    
    # create the shelf
    shelf_icon_path = os.path.join(os.path.dirname(__file__), 'common', 'shelf', 'icons')
    cmds.evalDeferred("import mmtk.common.shelf as shelf; shelf.ShelfMMTK('MMTK', icon_path='{}/')".format(shelf_icon_path))

    logger.info("Setup for Muream Maya Toolkit done.")

