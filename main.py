
from run import *
import pygame
import pygame.freetype
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('PacMan - 7805ICT Principles of Software Engineering')
GAME_FONT = pygame.freetype.Font("animo.ttf", 18)
GAME_FONT1 = pygame.freetype.Font ("animo.ttf", 18)
GAME_FONT2 = pygame.freetype.Font("animo.ttf", 18)
mixer.music.load('pacman_beginning.wav')
mixer.music.play(-1)


class Button():
    def __init__(self,x,y,image,scale):
        width=image.get_width()
        height=image.get_height()

        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False

    def draw(self):
        action=False
        pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked=False
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action


config_button = pygame.image.load('option.png').convert_alpha()
play_img = pygame.image.load('play.png').convert_alpha()
exit_img = pygame.image.load('exit.png').convert_alpha()
logo = pygame.image.load('pmlogo.png').convert_alpha()

logo_button=Button(9,20,logo,0.42)
play_button=Button(120,160,play_img,0.5)

config=Button(135,240,config_button,0.5)
exit_button=Button(141,330,exit_img,0.5)


game_start=False
flag=True
game = GameController()
while flag:
    text_surface, rect = GAME_FONT.render("Created by: ", (230, 97, 29))
    screen.blit(text_surface, (20, 490))

    text_surface, rect = GAME_FONT1.render("Prashanna Malla s5235405 ", (230, 97, 29))
    screen.blit(text_surface, (20, 520))

    text_surface, rect = GAME_FONT2.render("Christian Basco s5252422 ", (230, 97, 29))
    screen.blit(text_surface, (20, 550))

    text_surface, rect = GAME_FONT2.render("7805ICT", (230, 97, 29))
    screen.blit(text_surface, (370, 555))

    if config.draw():
        import option
       # game_start = True
        #flag = True
    if play_button.draw():
        game_start = True
        flag = False
    logo_button.draw()
    if exit_button.draw():
        game_start = False
        flag = False
    if game_start == True:
        game.startGame()
        while True:
            game.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    pygame.display.update()
