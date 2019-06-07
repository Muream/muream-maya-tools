import logging
import sys

from mmtk.common.shelf import AbstractShelf


logger = logging.getLogger(__name__)


class ShelfMMTK(AbstractShelf):

    def build(self):
        all_python_modules = sys.modules

        self.add_button(
            "",
            command="from mmtk.common.reload import reload_mmtk; reload_mmtk()",
            icon="refresh.svg"
        )

        if 'ngSkinTools' in all_python_modules:
            self.add_button(
                "Export Layers",
                command="from mmtk.rigging.ngskintools import export_layers; export_layers()",
                icon="layers.svg"
            )
            self.add_button(
                "Import Layers",
                command="from mmtk.rigging.ngskintools import import_layers; import_layers()",
                icon="layers.svg"
            )
            logger.info("Added ngSkinTools buttons.")
        else:
            logger.warning("Could not find 'ngSkinTools', the buttons using it were not added")

        if 'shapeshifter' in all_python_modules:
            self.add_button(
                "",
                command="from mmtk.rigging.shapeshifter import mirror_shape_left_to_right; mirror_shape_left_to_right()",
                icon="flip.svg"
            )
            self.add_button(
                "",
                command="from mmtk.rigging.shapeshifter import copy_shape; copy_shape()",
                icon="copy.svg"
            )
            logger.info("Added shapeshifter buttons.")
        else:
            logger.warning("Could not find 'shapeshifter', the buttons using it were not added")

        if 'mop' in all_python_modules:
            self.add_button(
                "Fields",
                command="from mmtk.rigging.mop import fix_object_list_fields; fix_object_list_fields()",
                icon="mite.svg"
            )
            logger.info("Added MOP buttons.")
        else:
            logger.warning("Could not find MOP, the buttons using it were not added")

        self.add_button(
            "attach",
            command="import ptvsd; ptvsd.enable_attach(address=('localhost', 3000), redirect_output=True); ptvsd.wait_for_attach()",
            icon="mite.svg"
        )


if __name__ == "__main__":
    ShelfMMTK(name="MMTK", icon_path="C:/Users/muream/projects/muream-maya-toolkit/mmtk/common/shelf/icons/")
