import maya.cmds as cmds

from .deformers import get_deformers_by_type


def select_binding_joints():
    mesh = cmds.ls(sl=True)
    if not mesh:
        raise RuntimeError("No Mesh selected")
    mesh = mesh[0]

    joints = get_binding_joints(mesh)
    cmds.select(joints, replace=True)


def get_binding_joints(mesh):

    skin_cluster = get_deformers_by_type(mesh, "skinCluster")
    if not skin_cluster:
        raise RuntimeError("Mesh '{}' isn't skinned".format(mesh))

    skin_cluster = skin_cluster[0]
    joints = cmds.listConnections("{}.matrix".format(skin_cluster))

    return joints


def reset_translation(nodes):
    if not isinstance(nodes, list):
        nodes = [nodes]

    for node in nodes:
        if not cmds.nodeType(node) in ["transform", "joint"]:
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "translate" + axis)

            try:
                cmds.setAttr(attr_name, 0)
            except RuntimeError as e:
                pass


def reset_rotation(nodes):
    if not isinstance(nodes, list):
        nodes = [nodes]

    for node in nodes:
        if not cmds.nodeType(node) in ["transform", "joint"]:
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "rotate" + axis)

            try:
                cmds.setAttr(attr_name, 0)
            except RuntimeError as e:
                pass


def reset_scale(nodes):
    if not isinstance(nodes, list):
        nodes = [nodes]

    for node in nodes:
        if not cmds.nodeType(node) in ["transform", "joint"]:
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "scale" + axis)

            try:
                cmds.setAttr(attr_name, 1)
            except RuntimeError as e:
                pass


def reset_transformation(nodes):
    reset_translation(nodes)
    reset_rotation(nodes)
    reset_scale(nodes)
