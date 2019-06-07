from mop.core.rig import Rig
import maya.cmds as cmds

def fix_object_list_fields():
    rig = Rig()

    for module in rig.rig_modules:
        print module.name.get()
        for field in module.fields:
            if field.__class__.__name__ == 'ObjectListField':
                values = getattr(module, field.name).get()
                print 'field:', field.name
                print "values found:", values
                cmds.deleteAttr(module.node_name, attribute=field.name)
                print "deleted Attribute"
                cmds.addAttr(module.node_name, longName=field.name, attributeType='message', multi=True)
                print "re-created attribute"
                for i, val in enumerate(values):
                    cmds.connectAttr(
                        val + '.message',
                        '{}.{}[{}]'.format(module.node_name, field.name, i)
                    )
                print "new_values:", getattr(module, field.name).get()
        print

    print "Done!"
