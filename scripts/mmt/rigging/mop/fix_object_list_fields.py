from mop.core.rig import Rig
import maya.cmds as cmds


def fix_object_list_fields():
    rig = Rig()

    for module in rig.rig_modules:
        for field in module.fields:
            if field.__class__.__name__ == "ObjectListField":
                values = getattr(module, field.name).get()
                cmds.deleteAttr(module.node_name, attribute=field.name)
                cmds.addAttr(
                    module.node_name,
                    longName=field.name,
                    attributeType="message",
                    multi=True,
                )
                for i, val in enumerate(values):
                    cmds.connectAttr(
                        val + ".message",
                        "{}.{}[{}]".format(module.node_name, field.name, i),
                    )
