import logging
import os

import maya.cmds as cmds

from ngSkinTools.mllInterface import MllInterface
from ngSkinTools.importExport import JsonExporter, LayerData, InfluenceInfo

from mmtk.common.dag import get_shape_type
from mmtk.common.path import get_scene_dir


logger = logging.getLogger(__name__)


def export_layers(path=None):
    """Export the ngskintools of the selected meshes.

    if `path` is not specified, the files will be exported in
    a "skin_data" directory next to the file.

    :param path: absolute path where to save the files.
    :type path: str
    """

    if path is None:
        path = os.path.join(get_scene_dir(), "skin_data")

    if not os.path.exists(path):
        os.makedirs(path)

    # initiate stuff before looping over the meshes
    exporter = JsonExporter()
    mll = MllInterface()
    sel = cmds.ls(sl=True)

    for mesh in sel:
        # a bunch of checks to make sure we really have a mesh in our hands
        try:
            shape_type = get_shape_type(mesh)
        except ValueError as e:
            logger.warning("{} Skipping".format(e))
            continue
        except TypeError as e:
            logger.warning("{} Skipping".format(e))
            continue

        if shape_type != "mesh":
            logger.warning("{} is not a mesh. Skipping".format(mesh))
            continue

        logger.info("Exporting data for {}".format(mesh))

        # initiate ngSkinTools layers in case the mesh doesn't have any
        mll.setCurrentMesh(mesh)
        mll.initLayers()

        # getting and exporting the data
        data = LayerData()

        try:
            data.loadFrom(mesh)
        except TypeError:
            logger.warning("Couldn't export skin data for {}".format(mesh))
            continue

        json = exporter.process(data)
        file_path = os.path.join(path, mesh + ".json")
        with open(file_path, "w") as f:
            f.write(json)


if __name__ == "__main__":
    export_layers()
