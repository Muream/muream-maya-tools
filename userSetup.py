import os
import sys
import logging
import site


logger = logging.getLogger(__name__)

sys.dont_write_bytecode = True

try:
    import cosmos
except:
    logger.error("Couldn't load Cosmos")


try:
    home_dir = os.path.expanduser("~")
    mmtk_dir = os.path.join(home_dir, "projects", "maya", "muream-maya-toolkit")
    site.addsitedir(mmtk_dir)
    import mmtk

    mmtk.setup()
except:
    logger.error("Couldn't load Muream Maya Toolkit")
