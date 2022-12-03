from talon import Module, actions
from enum import Enum
from .events import Events

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
            command: ["escape", "esc"],
            ex_command: [":"],
            insert: ["i", "I", "a", "A", "o", "O", "R"],
            search: ["/", "?"],
            visual: ["v", "V", "ctrl-v"]
        }

        def parse(input: str):
            map = Vim.Mode.letterMap
            for mode in map.keys():
                if input in map[mode]:
                    return mode

            return None


    def set_mode_without_notify(newMode: Mode):
        if(newMode is not None and Vim._currentMode != newMode):
            Vim._currentMode = newMode

    def set_mode(newMode: Mode):
        if(newMode is not None and Vim._currentMode != newMode):
            Vim._currentMode = newMode
            Events.change_vim_mode.call(newMode)

    def set_mode_without_notify_with(key: str):
        Vim.set_mode_without_notify(Vim.Mode.parse(key))

    def set_mode_with(key: str):
        Vim.set_mode(Vim.Mode.parse(key))

    def get_mode() -> Mode:
        return Vim._currentMode



