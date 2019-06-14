"""This is based on: https://bindpose.com/scripting-custom-shelf-in-maya-python"""

import maya.cmds as cmds
import abc
import os


def _null(*args):
    pass


class AbstractShelf(object):
    """
    A simple class to build shelves in maya. Since the build method is empty,
    it should be extended by the derived class to build the necessary shelf elements.
    By default it creates an empty shelf called "customShelf".
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, name="customShelf", icon_path=""):
        self.name = name

        self.icon_path = icon_path

        self.labelBackground = (0, 0, 0, 0.5)
        self.labelColour = (0.9, 0.9, 0.9)

        self._clean_old_shelf()
        cmds.setParent(self.name)
        self.build()

    @abc.abstractmethod
    def build(self):
        """
        This method should be overwritten in derived classes to actually build the shelf
        elements. Otherwise, nothing is added to the shelf.
        """

    def add_button(
        self, label, icon="commandButton.png", command=_null, doubleCommand=_null
    ):
        """Add a shelf button with the specified label, command, double click command and image."""
        cmds.setParent(self.name)
        if icon:
            icon = os.path.join(self.icon_path, icon)
        cmds.shelfButton(
            width=64,
            height=32,
            image=icon,
            l=label,
            command=command,
            dcc=doubleCommand,
            imageOverlayLabel=label,
            olb=self.labelBackground,
            olc=self.labelColour,
        )

    def add_menu_item(self, parent, label, command=_null, icon=""):
        """Adds a shelf button with the specified label, command, double click command and image."""
        if icon:
            icon = os.path.join(self.icon_path, icon)
        return cmds.menuItem(p=parent, l=label, c=command, i="")

    def add_sub_menu(self, parent, label, icon=None):
        """Adds a sub menu item with the specified label and icon to the specified parent popup menu."""
        if icon:
            icon = os.path.join(self.icon_path, icon)
        return cmds.menuItem(p=parent, l=label, i=icon, subMenu=1)

    def _clean_old_shelf(self):
        """Checks if the shelf exists and empties it if it does or creates it if it does not."""
        if cmds.shelfLayout(self.name, ex=1):
            if cmds.shelfLayout(self.name, q=1, ca=1):
                for each in cmds.shelfLayout(self.name, q=1, ca=1):
                    cmds.deleteUI(each)
        else:
            cmds.shelfLayout(self.name, p="ShelfLayout")
