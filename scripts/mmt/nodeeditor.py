import maya.mel as mel
import maya.cmds as cmds


def graph_hovered_attribute(source, destination):
    """
    Adds outgoing connections for a specific attribute (under the cursor) to the Node Editor.
    1. Gets the plug that the cursor is hovering over
    2. Gets direct output connections (conversion nodes and their outputs if necessary)
    3. Adds these nodes to the Node Editor
    This should obviously only be executed while hovering over the attribute in the Node Editor.
    To test you could:
        * assign it to a hotkey
        * make it a shelf button, execute once and then hit "g" to execute again
    so it is executed while you hover over attributes in the Node Editor

    Originally taken from Niels' script https://kleinhei.nz/2020/12/maya-node-editor-graph-connection-for-single-attribute/
    """
    node_editor = mel.eval("getCurrentNodeEditor")
    item_under_cursor = cmds.nodeEditor(node_editor, feedbackType=True, query=True)
    if item_under_cursor == "plug":
        plug_under_cursor = cmds.nodeEditor(node_editor, feedbackPlug=True, query=True)

        node, plug = plug_under_cursor.split(".")
        nodes = get_connected_nodes(node, plug, source, destination)
        if nodes:
            graph_nodes(nodes)
        else:
            cmds.warning(
                "Attribute '{}' has no outgoing connections.".format(plug_under_cursor)
            )
    else:
        cmds.warning("Hover over attribute in Node Editor while executing.")


def graph_nodes(nodes):
    node_editor = mel.eval("getCurrentNodeEditor")
    cmds.nodeEditor(node_editor, addNode=nodes, layout=False, edit=True)


def get_connected_plugs(node, plug, source, destination):
    connections = set(
        cmds.listConnections(
            ".".join([node, plug]), source=source, destination=destination, plugs=True
        )
        or []
    )
    return connections


def get_connected_plugs_recursive(node, plug, source, destination):
    """Recursively get all the nodes that are affected by the given plug."""
    all_plugs = set()
    connected_plugs = get_connected_plugs(node, plug, source, destination)
    for connected_plug in connected_plugs:
        all_plugs.add(connected_plug)
        node_name, plug_name = connected_plug.split(".")
        node_type = cmds.nodeType(node_name)

        plugs_to_check = [plug_name]
        print(plug_name)
        plugs_to_check.extend(cmds.affects(plug_name, type=node_type) or [])

        for plug_to_check in plugs_to_check:
            all_plugs = all_plugs | get_connected_plugs_recursive(
                node_name,
                plug_to_check,
                source,
                destination,
            )

    return all_plugs


def get_connected_nodes(node, plug, source, destination):
    """Return the nodes affected by the given plug."""
    plugs = get_connected_plugs_recursive(node, plug, source, destination)
    nodes = list(set([p.split(".")[0] for p in plugs]))
    return nodes


if __name__ == "__main__":
    cmds.file(new=True, force=True)

    node1 = cmds.createNode("transform")
    node2 = cmds.createNode("transform")
    node3 = cmds.createNode("transform")
    cmds.connectAttr(
        "{}.translate".format(node1),
        "{}.translate".format(node2),
    )
    cmds.connectAttr(
        "{}.translate".format(node2),
        "{}.translate".format(node3),
    )
    nodes = get_connected_nodes(node1, "translate")
    graph_nodes(nodes)
