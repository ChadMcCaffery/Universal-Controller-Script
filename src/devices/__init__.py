"""
devices

Contains definitions for devices, allowing the script to interface with them

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'Device',
    'DeviceShadow',
    'EventCallback',
]

# Device manufacturers
from . import (
    akai,
    korg,
    maudio,
    novation,
)
from .device import Device
from .device_shadow import DeviceShadow, EventCallback

del (
    akai,
    novation,
    maudio,
    korg,
)
