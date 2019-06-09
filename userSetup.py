import os
import sys
import logging
from maya import utils


logger = logging.getLogger(__name__)

sys.dont_write_bytecode = True

try:
    import cosmos
except:
    logger.error("Couldn't load Cosmos")


try:
    home_dir = os.path.expanduser("~")
    mmtk_dir = os.path.join(home_dir, "projects", "muream-maya-toolkit")
    sys.path.append(mmtk_dir)
    import mmtk

    mmtk.setup()
except:
    logger.error("Couldn't load Muream Maya Toolkit")

try:
    import mop.ui.menu

    utils.executeDeferred(mop.ui.menu.build_menu)
except:
    logger.error("Couldn't load Master Of Puppets")
