import sys, pygame, random
from pygame.locals import *

# Global constants
WHITE = 255, 255, 255
BLUE = 25,25,250
BLACK = 0,0,0

class character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((100,100))
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = 475
        self.rect.y = 600
        self.move = 0
        self.speed = 20
        self.otherCharacter = None

    def moveLeft(self):
        self.move += -self.speed
       

    def moveRight(self):
        self.move += self.speed

    def update(self): # Run when group update is called - inherited from pygame.sprite.Sprite
        self.rect = self.rect.move((self.move,0))
    
        # Collision
        if self.rect.left < 15:
            self.rect.left = 15
        if self.rect.right > 1000 - 15:
            self.rect.right = 1000 - 15


        
    def stop(self):
        self.move = 0


class Wall(pygame.sprite.Sprite):

    def __init__(self, dimensions):
       
        super().__init__()

        x, y, width, height = dimensions
       
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)

        # Make the top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Game():
    arenaWalls = [(0, 0, 15, 800), (0, 0, 1000, 15), (0, 0, 15, 800), (985, 0, 15, 800) ]
    def __init__(self):
        self.all_sprite_list = pygame.sprite.Group()
        self.character = character()
        self.walls = self.buildArena(Game.arenaWalls)

    def buildArena(self, walls):
        wall_list = pygame.sprite.Group()
        for wall in walls:
            wall = Wall(wall)
            wall_list.add(wall)
            self.all_sprite_list.add(wall)
        self.character.walls = wall_list
        wall_list.add(self.character)
        self.all_sprite_list.add(self.character)
        return wall_list


    def mainLoop(self, screen):
        clock = pygame.time.Clock()
        fps = 60

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return True
                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT: # Stop moving if key released
                        self.character.stop()

                if pygame.key.get_pressed()[K_LEFT]:
                    self.character.moveLeft()
                elif pygame.key.get_pressed()[K_RIGHT]:
                    self.character.moveRight()

            screen.fill(WHITE)
            self.all_sprite_list.update()
            self.all_sprite_list.draw(screen)
            pygame.display.flip()
            
            clock.tick(fps)
        pygame.quit()

def initialisePygame():

    pygame.init()

    size = width, height = 1000, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Fight")

    return screen


if __name__ == "__main__":
    test = Game()

    test.mainLoop(initialisePygame())












