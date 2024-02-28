import random
import pygame

class Ennemy(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__() 
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.velocity = random.randint(1,5)
        self.image = pygame.image.load('assets/ennemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 525

    def move(self):
        # self.rect.x -= self.velocity
        # if self.rect.x < 0:
        #     self.remove()
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)  

        if self.rect.x < 0:
            self.remove()

    def update_health_bar_ennemy(self, surface):
        bar_color = (37, 208, 85) 
        bg_bar_color = (193, 0, 0)

        bar_position = [self.rect.x, self.rect.y -20, self.health, 5]
        bg_bar_position = [self.rect.x, self.rect.y -20, self.max_health, 5]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def damage(self, attack):
        self.health -= attack
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1,5)
            self.health = self.max_health
            self.game.score += 20

    
