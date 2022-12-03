from ..lib.delegate import Delegate
from talon import Module, app

class Events():

    _setup = False
    wake = Delegate()
    sleep = Delegate()
    change_vim_mode = Delegate()

    def Setup():
        if not Events._setup:
            Events._setup = True

            Events.wake = Delegate()
            Events.sleep = Delegate()
            Events.changeVimMode = Delegate()

#app.register("ready", Events.Setup)
#Events.Setup()

mod = Module()

@mod.action_class
class Actions:
    def sleep_event(): 
        "Triggered when system goes to sleep"
        Events.sleep.call()

    def wake_event():
        "Triggered when system wakes up"
        Events.wake.call()
