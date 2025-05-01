"""
common > plug_indexes

Type definitions for plugin and window indexes.

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
__all__ = [
    'FlIndex',
    'PluginIndex',
    'WindowIndex',
    'GeneratorIndex',
    'EffectIndex',
]


from .effect import EffectIndex
from .fl_index import FlIndex
from .generator import GeneratorIndex
from .plugin import PluginIndex
from .window import WindowIndex
