from talon import Module, actions
from enum import Enum
from .events import Events
from ..lib.delegate import Delegate

mod = Module()
mod.tag("wyrm_vim", desc="CodeWyrm currently has VIM features enabled")

# We want to have it so instead we have a "change mode" function
# where you pass in a character and it figures out the rest

class Vim:
    
    class Mode(Enum):
        command = 0
        ex_command = 1
        insert = 2
        search = 4
        visual = 5

    letterMap = {
        Mode.command: ["escape", "esc"],
        Mode.ex_command: [":"],
        Mode.insert: ["i", "I", "a", "A", "o", "O", "R"],
        Mode.search: ["/", "?"],
        Mode.visual: ["v", "V", "ctrl-v"]
    }

    _currentMode = Mode.command

    def parse(input: str):
        map = Vim.letterMap
        for mode in map.keys():
            if input in map[mode]:
                return mode

        return None

    def get_mode() -> Mode:
        return Vim._currentMode

    def _enter_mode_with(key: str):
        if Vim.get_mode() != Vim.Mode.command:
            actions.key("esc")
        actions.key(key)

    def _can_set_mode(newMode: Mode) -> bool:
        return newMode is not None and Vim.get_mode() != newMode

    def set_mode_without_notify(newMode: Mode) -> bool:
        result = Vim._can_set_mode(newMode)
        if result:
            Vim._currentMode = newMode
        return result

    def set_mode(newMode: Mode) -> bool:
        result = Vim._can_set_mode(newMode)
        if result:
            Vim._currentMode = newMode
            Events.change_vim_mode.call(newMode)
        return result

    def set_mode_without_notify_with(key: str) -> bool:
        result = Vim.set_mode_without_notify(Vim.parse(key))
        if result:
            Vim._enter_mode_with(key)
        return result

    def set_mode_with(key: str) -> bool:
        result = Vim.set_mode(Vim.parse(key))
        if result:
            Vim._enter_mode_with(key)
        return result

        






