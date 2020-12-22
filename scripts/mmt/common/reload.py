import sys
import logging


logger = logging.getLogger(__name__)


def reload_mmt():
    """Remove all mmt modules from the Python session.

    Use this command to reload the `mmt` package after
    a change was made.
    """
    search = ["mmt"]
    mop_modules = []
    search = ["mmt", "shapeshifter"]
    for module in sys.modules:
        for term in search:
            if term in module and not "reload" in module:
                mop_modules.append(module)
                break

    for module in mop_modules:
        del sys.modules[module]

    logger.info("Reloaded mmt modules.")


if __name__ == "__main__":
    reload_mmt()
