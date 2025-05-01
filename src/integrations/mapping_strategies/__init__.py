"""
integrations > mapping strategies

Contains strategies to create event mappings for commonly used things, such
as pedals

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'PedalStrategy',
    'WheelStrategy',
    'NoteStrategy',
    'DirectionStrategy',
    'JogStrategy',
    'SimpleFaders',
    'ModXYStrategy',
    'MuteSoloStrategy',
    'GridStrategy',
    'PresetNavigationStrategy',
    'CcForwardStrategy',
]

from .cc_forward_strategy import CcForwardStrategy
from .direction_strategy import DirectionStrategy
from .grid_strategy import GridStrategy
from .jog_strategy import JogStrategy
from .mod_xy import ModXYStrategy
from .mute_solo import MuteSoloStrategy
from .note_strategy import NoteStrategy
from .pedal_strategy import PedalStrategy
from .preset_navigation import PresetNavigationStrategy
from .simple_faders import SimpleFaders
from .wheel_strategy import WheelStrategy
