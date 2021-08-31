import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from intersection import *
from ghosts import Ghost
from sprites import MazeSprites

from run import *

class GameController(object):
    def __init__(self):


        self.background = None
        self.clock = pygame.time.Clock()

    def setBackground(self):
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)


    def startGame(self):

        self.setBackground()
        self.nodes = NodeGroup("maze1.txt")
        #self.ghosts = GhostGroup((7,5), self.pacman)
        self.pacman = Pacman(self.nodes.getStartTempNode())
        self.ghost = Ghost(self.nodes.getStartTempNode())
        self.mazesprites = MazeSprites("maze1.txt","maze1_rotation.txt")
        self.background = self.mazesprites.constructBackground(self.background, 4)



    def update(self,screen):

        dt = self.clock.tick(30) / 1000.0
        self.pacman.update(dt)
        self.ghost.update(dt)
        self.checkEvents()
        self.render(screen)

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

    def render(self,screen):
        screen.blit(self.background, (0, 0))

        self.pacman.render(screen)
        self.ghost.render(screen)
        pygame.display.update()

