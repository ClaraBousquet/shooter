import pygame
import animation
from bullet import Bullet


class Player(animation.AnimateSprite):
    def __init__(self, game):
        #def init itialise la classe et permets de lutiliser (sans ça on ne peut pas l'utiliser)
        #super : classe mere, initialise la classe mere
        #self= objet courrant, ici player
        super().__init__("player") 
        self.game = game
        self.image = pygame.image.load('assets/player.png')
        #déclaration de la variable rectangle pour mettre l'image dedans
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 525
        self.health = 100
        self.max_health = 100
        self.attack = 10
        #vitesse
        self.velocity = 5
        self.all_bullets = pygame.sprite.Group()
        self.lives = 3
        

#les fonctions qui correpszondent au player sont toujours dans la classe player
#fonction qui permet de bouger le player
#definition de la fonction avec def
#nom de la fonction en snake case
#on saute une ligne entre les fonctions quand on est dans la classe, hors de la classe cest deux lignes
    def move_right(self):
        self.rect.x += self.velocity
        #si je ne rentre pas en collision avec ennemies, je peux avancer
        if not self.game.check_collision(self, self.game.all_ennemies):
            self.rect.x += self.velocity
        print(self.rect.x)

    def move_left(self):
        self.rect.x -= self.velocity
        

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        bar_color = (37, 208, 85) 
        bg_bar_color = (193, 0, 0)

        bar_position = [self.rect.x, self.rect.y -20, self.health, 5]
        bg_bar_position = [self.rect.x, self.rect.y -20, self.max_health, 5]

        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


            


    def damage(self,attack):
        self.health -= attack
        if self.health <= 0 :
            self.health = self.max_health
            self.rect.x = 300
            self.lives -= 1
        if self.lives == 0:
            self.lives = 3
            self.health = self.max_health
            self.rect.x = 300
            self.game.game_over()

        

    def launch_bullet(self):
        # fonction pour charger les balles
        # cest le personnage qui fait spawn les balles
        self.all_bullets.add(Bullet(self))
        self.images = self.load_animation_images("spell")
        self.speed = 0.25

    