"""
integrations

Contains definitions for script integrations, allowing the Universal Controller
Script to interface with FL Studio
"""

__all__ = [
    'IMappingStrategy',
    'NoteStrategy',
    'PedalStrategy',
    'WheelStrategy',
    'Integration',
    'CoreIntegration',
    'PluginIntegration',
    'WindowIntegration',
    'IntegrationPager',
]

# Register all integrations
from . import (
    core,
    plugin,
    window,
)
from .integration import (
    CoreIntegration,
    Integration,
    PluginIntegration,
    WindowIntegration,
)
from .mapping_strategies import (
    NoteStrategy,
    PedalStrategy,
    WheelStrategy,
)
from .pager import IntegrationPager

del (
    core,
    window,
    plugin,
)
