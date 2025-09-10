import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    #setup environment + variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 #delta_time

    #setup groups
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
 
    #add asteroids to group
    Asteroid.containers = (asteroids, updatables, drawables)

    #add player to groups and create player object
    Player.containers = (drawables, updatables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #add asteroidfield to group and create the field
    AsteroidField.containers = {updatables}
    asteroidfield = AsteroidField()

    
    

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #limit game to 24 FPS
        dt = clock.tick(24)/1000

        #clear and fill background
        screen.fill("black")
        
        #update groups
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)

        #update screen
        pygame.display.flip()





if __name__ == "__main__":
    main()