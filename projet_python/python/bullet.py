import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image,(60,60))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width
        self.rect.y = player.rect.y + (player.rect.height *0.5)
        self.velocity = 10
        self.angle = 0
        self.origine = self.image

    def remove(self):
        self.player.all_bullets.remove(self)

        #fonction move pour bouger le bullet

    def move(self):
        self.rect.x += self.velocity
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origine, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)
   
        for ennemy in self.player.game.check_collision(self, self.player.game.all_ennemies):
            self.remove()
            ennemy.damage(self.player.attack)
            
            

#libere la memoire de lordinateur, pas visible a lecran
        if self.rect.x > 10800:
            self.remove()
