from talon import Context, actions

ctx = Context()
@ctx.action_class("main")
class MainActions:
    def insert(text: str):
        #actions.key("i")
        # TODO: Silently switch to insert mode
        for char in text:
            actions.key(char)
        # TODO: Silently go back to old mode, if it makes sense

