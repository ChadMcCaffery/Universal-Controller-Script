"""
integrations > core > activity_switcher

Contains the definition for the activity switcher plugin

## Limitations

Currently doesn't handle cases where plugins have been rearranged, which may
lead to confusing behavior.

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
import contextlib

from common.extension_manager import ExtensionManager
from common.plug_indexes import (
    FlIndex,
    PluginIndex,
)
from common.types import Color
from control_surfaces import (
    ActivitySwitcher as ActivitySwitchControl,
)
from control_surfaces import (
    ControlShadow,
    ControlShadowEvent,
)
from devices import DeviceShadow
from integrations.event_filters import filterButtonLift
from integrations.integration import CoreIntegration


def getActivityColor(activity: FlIndex) -> Color:
    """
    Returns the color associated with a particular activity

    ### Args:
    * `activity` (`SafeIndex`): activity

    ### Returns:
    * `Color`: color
    """
    if isinstance(activity, PluginIndex):
        try:
            return activity.track.color
        except TypeError:
            # Prevent issues if we deleted stuff
            # FIXME: Do we need this check? What could we have deleted?
            return Color.BLACK
    else:
        return Color.ENABLED


class ActivitySwitcher(CoreIntegration):
    @classmethod
    def shouldBeActive(cls) -> bool:
        return True

    @classmethod
    def create(cls, shadow: DeviceShadow) -> 'CoreIntegration':
        return cls(shadow)

    def __init__(self, shadow: DeviceShadow) -> None:
        shadow.setMinimal(True)
        shadow.bindMatches(
            ActivitySwitchControl,
            self.eActivity,
            self.tActivity,
            args_generator=...,
        )
        super().__init__(shadow)

    @filterButtonLift()
    def eActivity(
        self,
        control: ControlShadowEvent,
        _,
        c_index: int,
    ) -> bool:
        from common import getContext
        with contextlib.suppress(IndexError):
            getContext().activity.getHistoryActivity(c_index).focus()
        return True

    def tActivity(
        self,
        control: ControlShadow,
        _,
        c_index: int,
    ):
        from common import getContext
        try:
            activity = getContext().activity.getHistoryActivity(c_index)
            control.color = getActivityColor(activity)
            control.annotation = activity.getName()
        except IndexError:
            pass


ExtensionManager.super_special.register(ActivitySwitcher)
