from .lib.delegate import Delegate
from talon import Module

class Events():
    def Init():
        Events.wake = Delegate()
        Events.sleep = Delegate()

Events.Init()

mod = Module()

@mod.action_class
class Actions:
    def sleep_event(): 
        "Triggered when system goes to sleep"
        Events.sleep.call()

    def wake_event():
        "Triggered when system wakes up"
        Events.wake.call()