import maya.cmds as cmds


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