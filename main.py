import pygame,sys
from constants import *  
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt=0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers =(asteroids,updatable,drawable)
    Player.containers=(updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for obj in updatable:
            obj.update(dt)
    
        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.is_collision(player):
                sys.exit("GAME OVER!")
        
        pygame.display.flip()  
        dt = clock.tick(60)     
        dt = dt/1000

if __name__ == "__main__":
    main()

