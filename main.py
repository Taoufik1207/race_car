import pygame
import random

# Initialiser Pygame
pygame.init()

# Définir la taille de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Course de voitures")

# Définir les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Définir la taille des voitures
car_width = 30
car_height = 10

# Définir la position de départ des voitures
car1_position = (50, 50)
car2_position = (50, 100)

# Définir la distance de la course
distance_course = 700

# Définir la vitesse de départ des voitures
car1_speed = 0
car2_speed = 0

# Charger les images des voitures
car1_image = pygame.Surface((car_width, car_height))
car1_image.fill(RED)
car2_image = pygame.Surface((car_width, car_height))
car2_image.fill(BLUE)

# Boucle principale
clock = pygame.time.Clock()
game_over = False
started = False
while not game_over:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not started:
                car1_speed += random.uniform(0, 1)
                car2_speed += random.uniform(0, 1)
                started = True
            elif event.key == pygame.K_r:
                # Accélérer la voiture 1
                car1_speed += random.uniform(-1, 1)
            elif event.key == pygame.K_b:
                # Accélérer la voiture 2
                car2_speed += random.uniform(-1, 1)
    # Avancer les voitures
    car1_position = (car1_position[0] + car1_speed, car1_position[1])
    car2_position = (car2_position[0] + car2_speed, car2_position[1])

    if car1_position[0] < 0:
        car1_position = (0, car1_position[1])
    if car2_position[0] < 0:
        car2_position = (0, car2_position[1])
    # Dessiner les éléments du jeu
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (distance_course, 0, 2, screen_height))  # Ligne d'arrivée
    screen.blit(car1_image, car1_position)
    screen.blit(car2_image, car2_position)

    # Mettre à jour l'écran
    pygame.display.update()

    # Déterminer le gagnant
    if car1_position[0] >= distance_course:
        print("La voiture rouge a gagné !")
        game_over = True
    elif car2_position[0] >= distance_course:
        print("La voiture bleue a gagné !")
        game_over = True

    # Limiter la vitesse de rafraîchissement
    clock.tick(60)

# Quitter Pygame
pygame.quit()
