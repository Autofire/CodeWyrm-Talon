from ..events import Events
#from talon import Module
from playsound import playsound
import os

########################################################################
# global settings
########################################################################
# This is where the built-in list of sound files exists.
# It provides a list of the valid sounds that can be found, along with
# any relevant attributes on them.
cwd = os.path.dirname(os.path.realpath(__file__))
homophones_file = os.path.join(cwd, "sound.csv")

soundPackPath = os.path.join(os.path.expanduser('~'), ".WyrmSounds")
soundPackName = "mmbn"
########################################################################

class sounds():

    #blip = "blip.wav"
    class text():
        delete = "delete.wav"
        paste = "paste.wav"
        yank = "yank.wav"
    class mode():
        cmd = "mode-cmd.wav"
        imm = "mode-imm.wav"
        vis = "mode-vis.wav"
    
    class shift():
        on = "shift-on.wav"
        off = "shift-off.wav"

    error = "error.wav"
    refresh = "refresh.wav"
    write = "write.wav"

print(soundPackPath)

def GetSoundFolder():
    return os.path.join(soundPackPath, soundPackName)

def GetSound(name):
    return os.path.join(soundPackPath, soundPackName, name).replace("\\", "/")

def Play(name):
    playsound(GetSound(name), False)

#os.chdir(GetSoundFolder())
#file = "./CodeWyrm-Talon/sounds/local/mmbn/blip.wav"
#file = "C:/Users/Daniel/AppData/Roaming/talon/user/CodeWyrm-Talon/sounds/local/mmbn/blip.wav"


Events.wake += lambda : Play(sounds.shift.on)
Events.sleep += lambda : Play(sounds.shift.off)

#playsound(file)

