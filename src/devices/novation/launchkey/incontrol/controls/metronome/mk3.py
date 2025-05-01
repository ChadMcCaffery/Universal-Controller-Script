"""
devices > novation > launchkey > incontrol > controls > metronome > mk3

Authors:
* Maddy Guthridge [hello@maddyguthridge.com, HDSQ#2154]

This code is licensed under the GPL v3 license. Refer to the LICENSE file for
more details.
"""
from control_surfaces import MetronomeButton
from control_surfaces.event_patterns import BasicPattern, ForwardedPattern
from control_surfaces.value_strategies import (
    ButtonData2Strategy,
    ForwardedStrategy,
)


class LkMk3MetronomeButton(MetronomeButton):

    def __init__(
        self,
    ) -> None:
        super().__init__(
            ForwardedPattern(2, BasicPattern(0xBF, 0x4C, ...)),
            ForwardedStrategy(ButtonData2Strategy()),
        )
