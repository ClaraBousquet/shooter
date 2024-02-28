import pygame

from game import Game

pygame.init()

clock = pygame.time.Clock()
FPS = 60

game = Game()

# initialisation de la classe toujours avec deux parentheses
# les classes ont des majuscules


# ligne pour donner un nom a ma fenetre
pygame.display.set_caption("IDEM_SHOOTER")
# variable screen parce quon sen servira plusieurs fois
# je mets deux parentheses pour nutiliser que le premier parametre de set mode qui est size
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.png')



running = True


while running:
    # jappelle lecran, la fonction blit applique limage sur lecran
    # le point veut dire je rentre dedans
    screen.blit(background, (0,-300))
    #je mets mon game.player dans ma fenetre
    screen.blit(game.player.image, game.player.rect)
    # la fonction flip est un update, a faire toujours apres
    # creation dune fenetre de score, texte
    font = pygame.font.SysFont('monospace', 16)
    score_text = font.render(f"Score : {game.score}", 1, (0, 0, 0))
    screen.blit(score_text, (20, 20))
    game.player.update_health_bar(screen)
    
    pygame.display.flip()

# j appelle game.player
    game.player.all_bullets.draw(screen)
    #conditions pour aller à droite et à gauche en mainetnant le bouton 
    if game.pressed_keys.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    
    elif game.pressed_keys.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

# boucle pour gérer le mouvement de bul
    for bullet in game.player.all_bullets:
        bullet.move()

    for ennemy in game.all_ennemies:
        ennemy.move()
        ennemy.update_health_bar_ennemy(screen)
        game.all_ennemies.draw(screen)
        

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
        

    clock.tick(FPS)

