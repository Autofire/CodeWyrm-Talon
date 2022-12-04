from talon import Context, actions
from .vim import Vim

ctx = Context()
@ctx.action_class("main")
class MainActions:
    def insert(text: str):
        #actions.key("i")
        # TODO: Silently switch to insert mode
        changed = Vim.set_mode_without_notify_with("a")
        for char in text:
            actions.key(char)
        # TODO: Silently go back to old mode, if it makes sense
        if changed:
            Vim.set_mode_without_notify_with("esc")

