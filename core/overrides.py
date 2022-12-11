from talon import Context, actions
from .vim import Vim

ctx = Context()
@ctx.action_class("main")
class MainActions:
    def insert(text: str):
        #actions.key("i")
        changed = Vim.set_mode_without_notify_with("a")
        for char in text:
            actions.key(char)
        if changed:
            Vim.set_mode_without_notify_with("esc")



