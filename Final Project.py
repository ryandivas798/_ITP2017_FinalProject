#I got most of the codes from youtube but i also modified most of the codes.
import os
import random
import pygame
from pygame.sprite import *
from pygame import *

pygame.init()

hitboxes = []
blocks =[]
class textsprite (Sprite): #This code is reusable, just fill in the parameters to reuse
    def __init__(self, fontstyle, text, fontsize, horizontal, vertical, R, G, B):
        Sprite.__init__(self)
        self.font = pygame.font.SysFont(fontstyle, fontsize)
        self.image = self.font.render(text, False, (R, G, B))
        self.rect = self.image.get_rect()
        self.rect.x = horizontal
        self.rect.y = vertical

class Player(object):#Basically the orange box that is moving

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, c, d):
        if c != 0:
            self.move_single_axis(c, 0)
        if d != 0:
            self.move_single_axis(0, d)

    def move_single_axis(self, c, d):

        self.rect.x += c
        self.rect.y += d

        for hitbox in hitboxes:
            if self.rect.colliderect(hitbox.rect):
                if c > 0:
                    self.rect.right = hitbox.rect.left
                if c < 0:
                    self.rect.left = hitbox.rect.right
                if d > 0:
                    self.rect.bottom = hitbox.rect.top
                if d < 0:
                    self.rect.top = hitbox.rect.bottom

        for block in blocks:
            if self.rect.colliderect(block.rect):
                if c > 0:
                    self.rect.right = block.rect.left
                if c < 0:
                    self.rect.left = block.rect.right
                if d > 0:
                    self.rect.bottom = block.rect.top
                if d < 0:
                    self.rect.top = block.rect.bottom

class Block(object):#The designated finish point

    def __init__(self, pos):
        blocks.append(self)
        self.rect= pygame.Rect(pos[0], pos[1], 16, 16)


class Wall(object):#The walls

    def __init__(self, pos):
        hitboxes.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

def stage(stage_number):
    os.environ["SDL_VIDEO_CENTERED"] = "1"#I have no idea since i got this from the video


    pygame.display.set_caption("Boxy Maze")
    screen = pygame.display.set_mode((720, 320))

    clock = pygame.time.Clock()

    player = Player()
    if stage_number == 1:
        stage1 = [
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "ZZ                                          Z",
        "Z  ZZZZZZZZZZZ ZZZZZZZZZZZZZ  ZZZZZZZZZZZZZ Z",
        "Z ZZZZZZZZZZ   ZZZZZZZZZZZZZ  ZZZZZZZZZZZZZ Z",
        "Z ZZZZ       ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ Z",
        "Z ZZZZ ZZZZZ   ZZZZZZZZZZZ   Z              Z",
        "Z  ZZZ ZZZZZZZ    Z     ZZ Z ZZZZZZZZZZZZZZ Z",
        "ZZ ZZZ ZZZZZZZZZZ Z ZZZ ZZ Z ZZZZZZZZZZZZZZ Z",
        "ZZ ZZZ ZZZZZZZZZZ Z ZZZ ZZ Z ZZZZZZZZZZZZZZ Z",
        "ZZ ZZZZZZZZZZZ    Z ZZZ ZZ Z ZZZZZZZZZZZZZZ Z",
        "ZZ     ZZZZZZZ ZZ Z ZZZ ZZ Z ZZZZZZZZZZZZZZ Z",
        "ZZZ ZZ         ZZ Z ZZZ ZZ Z ZZZZZZZZZZZZZZ Z",
        "ZZZ ZZZZZZZZZZ ZZ Z ZZZ ZZ Z                Z",
        "ZZZ ZZZZZZZZZZ ZZ Z ZZZ ZZ ZZZZZZZZZZZZZZZZZZ",
        "ZZZ ZZZZZZZZZZ ZZ Z ZZZ ZZ ZZZZZZZZZZZZZZZZZZ",
        "Z              ZZ   ZZZ  Z                  Z",
        "Z ZZZZZZZZZZZZZZZZZZZZZZZZZZ ZZZZZZZZZZZZZZ Z",
        "Z ZZZZZZZZZZZZZZZZZZZZZZZZZZ ZZZZZZZZZZZZZZ Z",
        "Z                          Z              ZXZ",
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",]

    if stage_number == 2:
        stage2 = [
        "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
        "ZZ                                         ZZ",
        "ZZ  ZZZZZZZZZZZZZZZZZZ ZZZZZZZZZZZZZZZZZZ  ZZ",
        "ZZZZZ                Z Z                ZZZZZ",
        "ZZZZZ ZZZZZZZZZZZZZZ Z Z ZZZZZZZZZZZZZZ ZZZZZ",
        "Z       Z            Z Z          Z         Z",
        "Z ZZZZZ Z ZZZZZZZZZZZZ ZZZZZZZZZZ Z ZZZZZZZ Z",
        "Z Z   Z Z Z                     Z Z Z     Z Z",
        "Z Z   Z Z Z ZZZZZZZZZZZZZZZZZZZ Z Z Z     Z Z",
        "Z Z   Z Z Z Z  Z              Z Z Z Z     Z Z",
        "Z Z   Z Z Z Z ZZZZZZZZ ZZZZZZ Z Z Z Z     Z Z",
        "Z Z   Z Z Z Z Z      Z Z    Z Z Z Z Z     Z Z",
        "Z Z   Z Z Z Z Z      Z      Z Z Z Z Z     Z Z",
        "Z Z   Z Z   Z Z      ZZZ    Z Z   Z Z     Z Z",
        "Z Z   Z  ZZZ  Z      Z      Z  ZZZ  Z     Z Z",
        "Z Z  ZZZ     ZZZ     Z Z   ZZZ     ZZZ    Z Z",
        "Z Z     ZZZZZZZ      Z Z      ZZZZZZZ     Z Z",
        "Z ZZZZZZZZZZZZZZZZZZZZ ZZZZZZZZZZZZZZZZZZZZ Z",
        "Z Z                    Z                    Z",
        "ZZZZZZZZZZZZZZZZZZZZZZXZZZZZZZZZZZZZZZZZZZZZZ",]

    a = b = 0
    if stage_number == 1:
        for row in stage1:
            for col in row:
                if col == "Z":
                    Wall((a, b))
                if col == "X":
                    end_rect = pygame.Rect(a, b, 16, 16)
                    Block((a,b))
                a += 16
            b += 16
            a = 0
    if stage_number == 2:
        for row in stage2:
            for col in row:
                if col == "Z":
                    Wall((a, b))
                if col == "X":
                    end_rect = pygame.Rect(a, b, 16, 16)
                    Block((a,b))
                a += 16
            b += 16
            a = 0
    running = True
    while running:

        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                break
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
                break

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)#These are the speed,i put the speed on 2 because of the tight angles in stage 2
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)

        screen.fill((0, 0, 0))
        for hitbox in hitboxes:
            pygame.draw.rect(screen, (255, 255, 255), hitbox.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.rect)
        pygame.display.flip()
        display.update()


def menu():
    pygame.display.set_caption("Boxy Maze")
    screen = pygame.display.set_mode((720, 320))
    screen.fill((0, 0, 0))
    play = textsprite("Times New Roman", "Play", 60, 100, 100, 255, 255, 255)#For the integers(size,placement(x(The higher the input it basically goes right),y(The higher the input the lower the placement),Colour(R,G,B)
    stages = textsprite("Times New Roman", "Stages", 60, 100, 200, 255, 255, 255)
    while True:
        all_text = Group(play, stages)
        all_text.draw(screen)
        menu_wait = event.wait()
        if play.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                stage(1)
        if stages.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                stage_selection()
        if menu_wait.type == QUIT:
            pygame.quit()
            break
        display.update()

def stage_selection():
    pygame.display.set_caption("Boxy Maze")
    screen = pygame.display.set_mode((720, 320))
    screen.fill((0, 0, 0))
    stage1 = textsprite("Arial", "Stage 1", 45, 50, 50, 255, 255, 255)
    stage2 = textsprite("Arial", "Stage 2", 45, 50, 150, 255, 255, 255)
    back = textsprite("Arial", "Back", 45, 50, 250, 255, 255, 255)
    while True:
        all_text = Group(stage1, stage2, back)
        all_text.draw(screen)
        menu_wait = event.wait()
        if stage1.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                stage(1)
        if stage2.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                stage(2)
        if back.rect.collidepoint(mouse.get_pos()):
            if menu_wait.type == MOUSEBUTTONDOWN:
                menu()
        if menu_wait.type == QUIT:
            pygame.quit()
            break
        display.update()

menu()
