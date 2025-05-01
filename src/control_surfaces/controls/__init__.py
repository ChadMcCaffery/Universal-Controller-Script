"""
control_surfaces > controls

Contains the definitions for all base classes for control surfaces used by the
script.

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""

__all__ = [
    'ControlSurface',
    'NullControl',
    'Note',
    'ModWheel',
    'PitchWheel',
    'StandardModWheel',
    'StandardPitchWheel',
    'Data2PitchWheel',
    'AfterTouch',
    'ChannelAfterTouch',
    'NoteAfterTouch',
    'Pedal',
    'SustainPedal',
    'SostenutoPedal',
    'SoftPedal',
    'Button',
    'TransportButton',
    'PlayButton',
    'StopButton',
    'LoopButton',
    'RecordButton',
    'FastForwardButton',
    'RewindButton',
    'MetronomeButton',
    'NavigationControl',
    'NavigationButton',
    'DpadButtons',
    'DirectionUp',
    'DirectionDown',
    'DirectionLeft',
    'DirectionRight',
    'DirectionSelect',
    'NextPrevButton',
    'DirectionNext',
    'DirectionPrevious',
    'JogWheel',
    'StandardJogWheel',
    'ShiftedJogWheel',
    'MoveJogWheel',
    'GenericFader',
    'Fader',
    'MasterFader',
    'FaderButton',
    'GenericFaderButton',
    'MasterGenericFaderButton',
    'MuteButton',
    'MasterMuteButton',
    'SoloButton',
    'MasterSoloButton',
    'ArmButton',
    'MasterArmButton',
    'SelectButton',
    'MasterSelectButton',
    'GenericKnob',
    'Knob',
    'MasterKnob',
    'Encoder',
    'ModXY',
    'ModX',
    'ModY',
    'DrumPad',
    'ToolSelector',
    'MacroButton',
    'SaveButton',
    'UndoRedoButton',
    'UndoButton',
    'RedoButton',
    'QuantizeButton',
    'CaptureMidiButton',
    'SwitchActiveButton',
    'SwitchActivePluginButton',
    'SwitchActiveWindowButton',
    'SwitchActiveToggleButton',
    'PauseActiveButton',
    'ControlSwitchButton',
    'HintMsg',
    'NotifMsg',
    'Ambient',
    'ActivitySwitcher',
]

from .activity_button import (
    PauseActiveButton,
    SwitchActiveButton,
    SwitchActivePluginButton,
    SwitchActiveToggleButton,
    SwitchActiveWindowButton,
)
from .activity_switcher import ActivitySwitcher
from .after_touch import (
    AfterTouch,
    ChannelAfterTouch,
    NoteAfterTouch,
)
from .ambient import Ambient
from .button import Button, ControlSwitchButton
from .control_surface import ControlSurface
from .drum_pad import DrumPad
from .encoder import Encoder
from .fader import Fader, GenericFader, MasterFader
from .fader_button import (
    ArmButton,
    FaderButton,
    GenericFaderButton,
    MasterArmButton,
    MasterGenericFaderButton,
    MasterMuteButton,
    MasterSelectButton,
    MasterSoloButton,
    MuteButton,
    SelectButton,
    SoloButton,
)
from .hint_msg import HintMsg
from .jog import (
    JogWheel,
    MoveJogWheel,
    ShiftedJogWheel,
    StandardJogWheel,
)
from .knob import GenericKnob, Knob, MasterKnob
from .macro_button import (
    CaptureMidiButton,
    MacroButton,
    QuantizeButton,
    RedoButton,
    SaveButton,
    UndoButton,
    UndoRedoButton,
)
from .mod_xy import ModX, ModXY, ModY
from .navigation import (
    DirectionDown,
    DirectionLeft,
    DirectionNext,
    DirectionPrevious,
    DirectionRight,
    DirectionSelect,
    DirectionUp,
    DpadButtons,
    NavigationButton,
    NavigationControl,
    NextPrevButton,
)
from .note import Note
from .notif_msg import NotifMsg
from .null_control import NullControl
from .pedal import (
    Pedal,
    SoftPedal,
    SostenutoPedal,
    SustainPedal,
)
from .tool_selector import ToolSelector
from .transport import (
    FastForwardButton,
    LoopButton,
    MetronomeButton,
    PlayButton,
    RecordButton,
    RewindButton,
    StopButton,
    TransportButton,
)
from .wheels import (
    Data2PitchWheel,
    ModWheel,
    PitchWheel,
    StandardModWheel,
    StandardPitchWheel,
)
