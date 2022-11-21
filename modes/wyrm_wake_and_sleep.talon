mode: all
-
tag(): user.wyrm

^dragon sleep [<phrase>]$:
    mode.disable("user.wyrm")
    user.sleep_event()

^dragon wake$:
    mode.enable("user.wyrm")
    user.wake_event()