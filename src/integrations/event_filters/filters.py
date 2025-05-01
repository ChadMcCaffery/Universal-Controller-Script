"""
integrations > event_filters > filters

Decorators to filter out events based on the type of event

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    "filterButtonLift",
]

from control_surfaces import Button, ControlShadowEvent

from .decorator import do_filter


@do_filter
def filterButtonLift(control: ControlShadowEvent, index, *args, **kwargs):
    """
    Filter out button lifts so that only presses are processed
    """
    return not (
        isinstance(control.getControl(), Button) and control.value == 0.0
    )
