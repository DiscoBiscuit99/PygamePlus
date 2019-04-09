""" The PygamePlus audio module """

import pygame

true  = True
false = False

class Audio:
    def __init__(self):
        # The master volume.
        self.master_volume = 0.5

    def newBackgroundMusic(self, filename):
        return "music", pygame.mixer.music.load(filename)

    def newSound(self, filename):
        return "sound", pygame.mixer.Sound(filename)

    def play(self, audio, *args):
        pygame.mixer.music.set_volume(self.master_volume)

        if audio[0] == "music":
            pygame.mixer.music.play()
        elif audio[0] == "sound":
            audio[1].set_volume(self.master_volume)
            audio[1].play()

        for arg in args:
            if arg[0] == "music":
                pygame.mixer.music.play()
            elif arg[0] == "sound":
                arg[1].set_volume(self.master_volume)
                arg[1].play()

    def stop(self, audio, *args):
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
    def setVolume(self, volume):
        self.master_volume = master_volume

    def getVolume(self):
        return self.master_volume
        
