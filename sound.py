import pygame


class SoundManager: 

    def __init__(self):
        self.sounds = {
            'tir':pygame.mixer.Sound("assets/sounds/tir.ogg"),
            'game_over':pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'click':pygame.mixer.Sound("assets/sounds/click.ogg"),
            'boum':pygame.mixer.Sound("assets/sounds/boum.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()

    # fonction play qupon appelle la ou on veut lancer le son
    #dictionnaire = tableau de cle / valeurs