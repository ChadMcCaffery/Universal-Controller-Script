"""
control_surfaces > controls > window_switcher

Contains the definition of window switcher control surfaces

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
from .button import Button
from .control_surface import ControlSurface


class ActivitySwitcher(Button):
    """
    Allows users to switch between FL Studio windows and recent plugins
    """
    @staticmethod
    def getControlAssignmentPriorities() -> 'tuple[type[ControlSurface], ...]':
        return tuple()
