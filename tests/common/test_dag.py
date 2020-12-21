import pytest

from mmt.common.dag import get_shape_type
import maya.cmds as cmds


def test_get_shape_type():
    node = cmds.polyCube()[0]
    shape_type = get_shape_type(node)
    cmds.delete(node)
    assert shape_type == "mesh"


def test_get_shape_type_no_shape():
    node = cmds.createNode("transform")
    with pytest.raises(TypeError):
        shape_type = get_shape_type(node)
    cmds.delete(node)


def test_get_shape_type_transform_doesnt_exist():
    with pytest.raises(ValueError):
        shape_type = get_shape_type("node_that_doesnt_exist")
