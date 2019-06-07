import logging
import glob
import os


import maya.cmds as cmds

from ngSkinTools.importExport import JsonImporter

from mmtk.common.path import get_scene_dir


logger = logging.getLogger(__name__)


def import_layers(path=None):
    """Import the ngskintools on the meshes that correspond to the files in path.

    if `path` is not specified, the files will be exported in
    a "skin_data" directory next to the file.

    :param path: absolute path to the skin data files.
    :type path: str
    """
    if path is None:
        path = os.path.join(get_scene_dir(), 'skin_data')

    if not os.path.exists(path):
        raise ValueError("Provided path {} does not exist.".format(path))

    # initiate stuff before looping over the meshes
    importer = JsonImporter()

    for f in glob.iglob(os.path.join(path, '*.json')):
        # get the mesh name from the absolute path of the file.
        mesh_name = os.path.splitext(os.path.basename(f))[0]

        # make sure the object exists.
        if not cmds.objExists(mesh_name):
            logging.warning("Object {} does not exist. Skipping".format(mesh_name))
            continue

        # import the data
        with open(f, "r") as f:
            json = f.read()
        data = importer.process(json)
        data.saveTo(mesh_name)
        logger.info("Imported Skinning data on {}".format(mesh_name))



if __name__ == "__main__":
    import_layers()
