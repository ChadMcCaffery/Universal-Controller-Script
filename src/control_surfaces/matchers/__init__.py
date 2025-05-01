"""
devices > matchers

Contains definitions for objects related to control matching

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'IControlMatcher',
    'BasicControlMatcher',
    'IndexedMatcher',
    'ShiftMatcher',
    'ShiftView',
    'NoteMatcher',
    'NoteAfterTouchMatcher',
    'PedalMatcher',
]

from .basic_matcher import BasicControlMatcher
from .control_matcher import IControlMatcher
from .indexed_matcher import IndexedMatcher
from .notes import NoteAfterTouchMatcher, NoteMatcher
from .pedals import PedalMatcher
from .shift_matcher import ShiftMatcher, ShiftView
