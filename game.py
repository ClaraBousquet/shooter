import pygame
from player import Player
from ennemy import Ennemy
from unicorn import Unicorn


class Game:

#ce que je mets dans linit sont les valeurs par defaut
    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.all_ennemies = pygame.sprite.Group()
        self.pressed_keys = {}
        self.score = 0

    def start(self):
        self.is_playing = True
        self.spawn_ennemies(3)

    def game_over(self):
        self.all_ennemies = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.lives = 3
        self.is_playing = False


    def update (self, screen):
        screen.blit(self.player.image, self.player.rect)
    
        font = pygame.font.SysFont('monospace', 16)
        score_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        lives_text = font.render(f"Life : {self.player.lives}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(lives_text, (35,35))

        self.player.update_health_bar(screen)
        self.player.update_animation()

        self.player.all_bullets.draw(screen)

        if (
            self.pressed_keys.get(pygame.K_RIGHT)
            and self.player.rect.x + self.player.rect.width < screen.get_width()
        ):
            self.player.move_right()
        
        elif self.pressed_keys.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        for bullet in self.player.all_bullets:
            bullet.move()
            

        for ennemy in self.all_ennemies:
            ennemy.move()
            ennemy.update_health_bar_ennemy(screen)
            ennemy.update_animation()
            self.all_ennemies.draw(screen)
        

    def spawn_ennemies(self, number):
        for _ in range(number):
            ennemy = Ennemy(self)
            self.all_ennemies.add(ennemy)

    def spawn_unicorns(self, number):
        for _ in range(number):
            unicorn = Unicorn(self)
            self.all_unicorns.add(unicorn)
#forcément besoin d'un groupe pour la fonction, donc on crée un groupe player dans sa classe
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)