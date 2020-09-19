import maya.cmds as cmds

def get_shape_type(transform):
    """Get the shape type of the transform node.

    :param transform: the name of the transform node.
    :type transform: str
    """

    if not cmds.objExists(transform):
        raise ValueError("{} does not exist".format(transform))

    shapes = cmds.listRelatives(transform, shapes=True)

    if not shapes:
        raise TypeError("{} is not a shaped node.".format(transform))

    return cmds.nodeType(shapes[0])
