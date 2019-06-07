import os
import pytest

import maya.cmds as cmds

from mmtk.rigging.ngskintools import import_layers

def test_export_layers():
    py_file_path = os.path.abspath(__file__)
    maya_file_path = os.path.join(os.path.dirname(py_file_path), 'test_import_layers.ma')

    cmds.file(maya_file_path, open=True, force=True)

    import_layers()
