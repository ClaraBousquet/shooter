import pygame
from player import Player
from ennemy import Ennemy

class Game:


#ce que je mets dans linit sont les valeurs par defaut
    def __init__(self):
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.all_ennemies = pygame.sprite.Group()
        self.spawn_ennemies(2)
        self.pressed_keys = {}
        self.score = 0

    def spawn_ennemies(self, number):
        for _ in range(number):
            ennemy = Ennemy(self)
            self.all_ennemies.add(ennemy)
#forcément besoin d'un groupe pour la fonction, donc on crée un groupe player dans sa classe
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)