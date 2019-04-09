""" The PygamePlus audio module """

import pygame

true  = True
false = False

master_volume = 0.5

def newBackgroundMusic(filename):
    return "music", pygame.mixer.music.load(filename)

def newSound(filename):
    return "sound", pygame.mixer.Sound(filename)

def play(audio, *args):
    global master_volume

    pygame.mixer.music.set_volume(master_volume)

    if audio[0] == "music":
        pygame.mixer.music.play()
    elif audio[0] == "sound":
        audio[1].set_volume(master_volume)
        audio[1].play()

    for arg in args:
        if arg[0] == "music":
            pygame.mixer.music.play()
        elif arg[0] == "sound":
            arg[1].set_volume(master_volume)
            arg[1].play()

    def stop(audio, *args):
        if audio[0] == "music":
            pygame.mixer.music.stop()
        elif audio[0] == "sound":
            audio[1].stop()

        for arg in args:
            if arg[0] == "music":
                pygame.mixer.music.stop()
            elif arg[0] == "sound":
                arg[1].stop()

    # Sets the volume ranging from 0.0 to 1.0.
    def setVolume(volume):
        global master_volume

        master_volume = volume

    def getVolume():
        global master_volume
        return master_volume
        
