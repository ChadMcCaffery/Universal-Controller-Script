"""
control_surfaces > event_patterns

Contains code for pattern matching with MIDI events, including IEventPattern,
a simple way to match events, and IEventPattern, and interface from which
custom pattern matchers can be derived.

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'ByteMatch',
    'fromNibbles',
    'fulfilByte',
    'IEventPattern',
    'UnionPattern',
    'BasicPattern',
    'ForwardedPattern',
    'ForwardedUnionPattern',
    'NullPattern',
    'TruePattern',
    'NotePattern',
]

from .basic_pattern import BasicPattern
from .byte_match import ByteMatch, fromNibbles, fulfilByte
from .event_pattern import IEventPattern
from .forwarded_pattern import ForwardedPattern, ForwardedUnionPattern
from .note_pattern import NotePattern
from .null_pattern import NullPattern, TruePattern
from .union_pattern import UnionPattern
