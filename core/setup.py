from talon import Module, app, actions
from ..sounds.sound import Play, Sounds

mod = Module()
# this declares a tag in the user namespace (i.e. 'user.tabs')
mod.mode("wyrm", desc="CodeWyrm features are active (including overrides)")
mod.tag("wyrm", desc="CodeWyrm features are active (including overrides)")

def activate():
    actions.mode.enable("user.wyrm")
    Play(Sounds.startup)
    

app.register("launch", activate)


