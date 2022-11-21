#defines the commands that sleep/wake Talon
mode: user.wyrm
tag: user.wyrm
-
^talon wake all$:
    user.mouse_wake()
    user.history_enable()
    user.talon_mode()
    user.wake_event()

^talon sleep all [<phrase>]$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
    user.sleep_event()

^talon sleep [<phrase>]$:
    speech.disable()
    user.sleep_event()

^talon wake$:
    speech.enable()
    user.wake_event()

