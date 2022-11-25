from talon import Context, actions

ctx = Context()
@ctx.action_class("main")
class MainActions:
    def insert(text: str):
        #actions.key("i")
        for char in text:
            actions.key(char)