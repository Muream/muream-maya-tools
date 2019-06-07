import sys
import logging


logger = logging.getLogger(__name__)


def reload_mmtk():
    """Remove all mmtk modules from the Python session.

    Use this command to reload the `mmtk` package after
    a change was made.
    """
    search = ["mmtk"]
    mop_modules = []
    for module in sys.modules:
        for term in search:
            if term in module and not 'reload' in module:
                mop_modules.append(module)
                break

    for module in mop_modules:
        del(sys.modules[module])

    logger.info('Reloaded mmtk modules.')


if __name__ == "__main__":
    reload_mmtk()
