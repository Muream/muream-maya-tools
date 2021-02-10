import maya.cmds as cmds


def get_deformers_by_type(mesh, deformer_type):
    deformers = [
        d for d in cmds.listHistory(mesh) or [] if cmds.nodeType(d) == deformer_type
    ]
    return deformers
