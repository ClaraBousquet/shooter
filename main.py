import math
import pygame

from game import Game
from sound import SoundManager
pygame.init()

clock = pygame.time.Clock()
FPS = 60

game = Game()

sound = SoundManager()

# initialisation de la classe toujours avec deux parentheses
# les classes ont des majuscules


# ligne pour donner un nom a ma fenetre
pygame.display.set_caption("IDEM_SHOOTER")
# variable screen parce quon sen servira plusieurs fois
# je mets deux parentheses pour nutiliser que le premier parametre de set mode qui est size
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.png')

banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner,(600, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
banner_rect.y = math.ceil(screen.get_height() / 8)

play_button = pygame.image.load("assets/play.png")
play_button = pygame.transform.scale(play_button,(400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

running = True


while running:
    # jappelle lecran, la fonction blit applique limage sur lecran
    # le point veut dire je rentre dedans
    screen.blit(background, (0,-300))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banner,(banner_rect.x, banner_rect.y))
        screen.blit(play_button,(play_button_rect.x, play_button_rect.y))
    #screen.blit(play_button, (X, Y))


    #je mets mon game.player dans ma fenetre
    

    pygame.display.flip()


    # boucle for pour chaque evenement
    for event in pygame.event.get():
        # si le type est la constante QUIT, on arrete la boucle et on quitte le jeu
        if  event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Bye")
            # c ondition pour quand on presse les boutons KEYDOWN 
            # si le bouton est appuyé, KEYUP il est relaché 
            # on applique l'action a la sortie de la bouche for
        elif event.type == pygame.KEYDOWN:   
            game.pressed_keys[event.key] = True
            
            if event.key == pygame.K_SPACE :
                game.player.launch_bullet()

        elif event.type == pygame.KEYUP:
            game.pressed_keys[event.key] = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()

    clock.tick(FPS)

