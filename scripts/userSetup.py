import logging
import sys
from textwrap import dedent

import maya.cmds as cmds

logger = logging.getLogger(__name__)

sys.dont_write_bytecode = True

try:
    import cosmos
except:
    logger.error("Couldn't load Cosmos")

cmds.evalDeferred(
    dedent(
        """
    from mmtk import setup
    setup()
    """
    ),
    lp=True,
)
