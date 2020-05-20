import maya.cmds as cmds

def reset_translation(nodes):
    if not isinstance(nodes, list):
        nodes = [list]

    for node in nodes:
        if not cmds.nodeType(node) == "transform":
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "translate" + axis)
            if cmds.getAttr(attr_name, lock=True):
                continue
            cmds.setAttr(attr_name, 0)


def reset_rotation(nodes):
    if not isinstance(nodes, list):
        nodes = [list]

    for node in nodes:
        if not cmds.nodeType(node) == "transform":
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "rotate" + axis)
            if cmds.getAttr(attr_name, lock=True):
                continue
            cmds.setAttr(attr_name, 0)

def reset_scale(nodes):
    if not isinstance(nodes, list):
        nodes = [list]

    for node in nodes:
        if not cmds.nodeType(node) == "transform":
            continue
        for axis in "XYZ":
            attr_name = "{}.{}".format(node, "scale" + axis)
            if cmds.getAttr(attr_name, lock=True):
                continue
            cmds.setAttr(attr_name, 0)

def reset_transformation(nodes):
    reset_translation(nodes)
    reset_rotation(nodes)
    reset_scale(nodes)