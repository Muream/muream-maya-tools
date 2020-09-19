import maya.cmds as cmds
from shapeshifter import shapeshifter


def copy_shape():
    sel = cmds.ls(sl=True)

    source = sel[0]
    targets = sel[1:]
    shape_data = shapeshifter.get_shape_data(source)
    for target in targets:
        shapeshifter.change_controller_shape(target, shape_data)


if __name__ == "__main__":
    copy_shape()
