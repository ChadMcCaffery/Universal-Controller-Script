"""
integrations > window

Integrations for interacting with FL Studio windows

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
__all__ = [
    'Mixer',
    'ChannelRack',
    'Playlist',
    'PianoRoll',
    'Browser',
]

from .browser import Browser
from .channel_rack import ChannelRack
from .mixer import Mixer
from .piano_roll import PianoRoll
from .playlist import Playlist
