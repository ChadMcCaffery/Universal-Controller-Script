"""
common

Contains common functions and code required to initialize and manage the
script.

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'getVersionString',
    'exceptions',
    'log',
    'verbosity',
    'ProfilerContext',
    'profilerDecoration',
    'getContext',
    'resetContext',
    'unsafeResetContext',
    'catchContextResetException',
    'ExtensionManager',
]


# Import devices and plugins
import devices
import integrations

from . import exceptions
from .context_manager import (
    catchContextResetException,
    getContext,
    resetContext,
    unsafeResetContext,
)
from .extension_manager import ExtensionManager
from .logger import log, verbosity
from .profiler import ProfilerContext, profilerDecoration

del devices
del integrations
