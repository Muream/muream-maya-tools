from shapeshifter import shapeshifter
import maya.api.OpenMaya as om2
import maya.cmds as cmds

SCALE_MIRROR_MAT = om2.MMatrix([
    -1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 1,
])
local_reflexion_mat = om2.MMatrix([
    -1.0,  0.0,  0.0, 0.0,
     0.0, -1.0,  0.0, 0.0,
     0.0,  0.0, -1.0, 0.0,
     0.0,  0.0,  0.0, 1.0
])

def mirror_shape_left_to_right():

    for node in cmds.ls(sl=True):
        if '_L_' in node:
            mirror_node = node.replace('_L_', '_R_')
        if '_R_' in node:
            mirror_node = node.replace('_R_', '_L_')

        node_world_mat = om2.MMatrix(cmds.xform(node, q=True, matrix=True, worldSpace=True))

        mirror_node_world_mat = om2.MMatrix(cmds.xform(mirror_node, q=True, matrix=True, worldSpace=True))

        shape_data = shapeshifter.get_shape_data(node)
        mirror_shape_data = shapeshifter.get_shape_data(mirror_node)

        for i, (shape, mirror_shape) in enumerate(zip(shape_data, mirror_shape_data)):
            mirror_cvs = []
            for cv in shape['cvs']:
                cv_mat = om2.MMatrix([
                    1, 0, 0, 0,
                    0, 1, 0, 0,
                    0, 0, 1, 0,
                    cv[0], cv[1], cv[2], 1,
                ])
                mirror_cv_mat = cv_mat * node_world_mat  * SCALE_MIRROR_MAT
                loc = cmds.spaceLocator()
                cmds.xform(loc, matrix=mirror_cv_mat * mirror_node_world_mat.inverse(), worldSpace=True)
                cv_pos = cmds.xform(loc, q=True, translation=True, worldSpace=True)
                cmds.delete(loc)
                mirror_cvs.append(cv_pos)
            mirror_shape['cvs'] = mirror_cvs
            mirror_shape_data[i] = mirror_shape
        shapeshifter.change_controller_shape(mirror_node, mirror_shape_data)


if __name__ == "__main__":
    mirror_shape_left_to_right()
