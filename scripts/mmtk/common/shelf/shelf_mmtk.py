import os
import logging
import sys

from mmtk.common.shelf import AbstractShelf


logger = logging.getLogger(__name__)


def _get_available_modules():
    available_modules = []
    for path in sys.path:
        if os.path.isdir(path):
            available_modules.extend(os.listdir(path))
    return available_modules


class ShelfMMTK(AbstractShelf):
    def build(self):
        available_modules = _get_available_modules()
        self.add_button(
            "",
            command="from mmtk.common.reload import reload_mmtk; reload_mmtk()",
            icon="refresh.svg",
        )

        if "ngSkinTools" in available_modules:
            self.add_button(
                "Export Layers",
                command="from mmtk.rigging.ngskintools import export_layers; export_layers()",
                icon="layers.svg",
            )
            self.add_button(
                "Import Layers",
                command="from mmtk.rigging.ngskintools import import_layers; import_layers()",
                icon="layers.svg",
            )
            logger.info("Added ngSkinTools buttons.")
        else:
            logger.warning(
                "Could not find 'ngSkinTools', the buttons using it were not added"
            )

        if "shapeshifter" in available_modules:
            self.add_button(
                "",
                command="from mmtk.rigging.shapeshifter import mirror_shape_left_to_right; mirror_shape_left_to_right()",
                icon="flip.svg",
            )
            self.add_button(
                "",
                command="from mmtk.rigging.shapeshifter import copy_shape; copy_shape()",
                icon="copy.svg",
            )
            logger.info("Added shapeshifter buttons.")
        else:
            logger.warning(
                "Could not find 'shapeshifter', the buttons using it were not added"
            )

        if "ptvsd" in available_modules:
            self.add_button(
                "attach",
                command="import ptvsd; ptvsd.enable_attach(address=('localhost', 3000), redirect_output=True); ptvsd.wait_for_attach()",
                icon="mite.svg",
            )
        else:
            logger.warning("could not find ptvsd, the buttons using it were not added")


if __name__ == "__main__":
    ShelfMMTK(
        name="MMTK",
        icon_path="C:/Users/muream/projects/muream-maya-toolkit/mmtk/common/shelf/icons/",
    )
