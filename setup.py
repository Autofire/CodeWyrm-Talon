from talon import Module

mod = Module()
# this declares a tag in the user namespace (i.e. 'user.tabs')
mod.mode("wyrm", desc="CodeWyrm features are active (including overrides)")
mod.tag("wyrm", desc="CodeWyrm features are active (including overrides)")


#@ctx.action_class("main")
#class MainActions:
#   def insert(text: str):