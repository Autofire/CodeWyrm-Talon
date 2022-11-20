mode: all
-
tag(): user.wyrm

^dragon sleep [<phrase>]$:
    mode.disable("user.wyrm")

^dragon wake$:
    mode.enable("user.wyrm")