from talon import Module, Context, actions
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
        colon = 1
        insert = 2
        search = 4
        visual = 5

    letter_map = {
        Mode.command: ["escape", "esc"],
        Mode.colon: [":"],
        Mode.insert: ["i", "I", "a", "A", "o", "O", "R"],
        Mode.search: ["/", "?"],
        Mode.visual: ["v", "V", "ctrl-v"]
    }

    mode_changed_event = Delegate()

    _current_mode = Mode.command

    def parse(input: str):
        map = Vim.letter_map
        for mode in map.keys():
            if input in map[mode]:
                return mode

        return None

    def get_mode() -> Mode:
        return Vim._current_mode

    def _enter_mode_with(key: str):
        if Vim.get_mode() != Vim.Mode.command:
            actions.key("esc")
        actions.key(key)

    def _can_set_mode(newMode: Mode) -> bool:
        return newMode is not None and Vim.get_mode() != newMode

    def set_mode_without_notify(newMode: Mode) -> bool:
        result = Vim._can_set_mode(newMode)
        if result:
            print("Mode from ", Vim._current_mode, " to ", newMode)
            Vim._current_mode = newMode
        return result

    def set_mode(newMode: Mode) -> bool:
        result = Vim.set_mode_without_notify(newMode)
        if result:
            #Events.change_vim_mode.call(newMode)
            print("Firing event for", newMode)
            Vim.mode_changed_event.call(newMode)
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


mod = Module()
ctx = Context()

"""
mod.list("vim_mode", desc="All modes for VIM")

mode_map = {}
for mode in Vim.Mode:
    mode_map[mode.name] = mode.name

ctx.lists["user.vim_mode"] = mode_map
"""

modeNames = [member.name for member in Vim.Mode]
modeRule = ' | '.join(modeNames)
modeRule = "(" + modeRule + ")"

@mod.capture(rule=modeRule)
def vim_mode(m) -> Vim.Mode:
    "Matches a vim mode"
    return Vim.Mode[str(m)]

@mod.action_class
class Actions:
    def set_vim_mode(s: Vim.Mode):
        "Jumps to the specified VIM mode immediately, overriding the old setting without any inputs"
        #Vim.set_mode(Vim.Mode[s])
        Vim.set_mode(s)


