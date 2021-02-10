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
        nodes = [list]

    for node in nodes:
        if not cmds.nodeType(node) in ["transform", "joint"]:
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "translate" + axis)

            is_locked = cmds.getAttr(attr_name, lock=True)
            is_connected = bool(
                cmds.listConnections(attr_name, source=True, destination=False)
            )
            if is_locked or is_connected:
                continue

            cmds.setAttr(attr_name, 0)


def reset_rotation(nodes):
    if not isinstance(nodes, list):
        nodes = [list]

    for node in nodes:
        if not cmds.nodeType(node) in ["transform", "joint"]:
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "rotate" + axis)

            is_locked = cmds.getAttr(attr_name, lock=True)
            is_connected = bool(
                cmds.listConnections(attr_name, source=True, destination=False)
            )
            if is_locked or is_connected:
                continue

            cmds.setAttr(attr_name, 0)


def reset_scale(nodes):
    if not isinstance(nodes, list):
        nodes = [list]

    for node in nodes:
        if not cmds.nodeType(node) in ["transform", "joint"]:
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "scale" + axis)

            is_locked = cmds.getAttr(attr_name, lock=True)
            is_connected = bool(
                cmds.listConnections(attr_name, source=True, destination=False)
            )
            if is_locked or is_connected:
                continue

            cmds.setAttr(attr_name, 1)


def reset_transformation(nodes):
    reset_translation(nodes)
    reset_rotation(nodes)
    reset_scale(nodes)