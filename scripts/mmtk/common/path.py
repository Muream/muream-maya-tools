import maya.cmds as cmds
import os


def get_scene_path():
    """Return the absolute path to the scene's file."""
    return cmds.file(query=True, sceneName=True)


def get_scene_dir():
    """Return the absolute path to the scene's directory."""
    return os.path.dirname(get_scene_path())


def get_scene_name():
    """Return the name of the scene.."""
    return os.path.basename(get_scene_path())


if __name__ == "__main__":
    print get_scene_path()
    print get_scene_dir()
    print get_scene_name()
