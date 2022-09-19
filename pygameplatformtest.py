import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
ACC = 0.35
FRIC = -0.08
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        #self.image = pygame.image.load("character.png")
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
 
    def move(self):
        self.acc = vec(0,0.30)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.30 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
             
        self.rect.midbottom = self.pos
 
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -8
    
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if self.vel.y > 0 :        
            if hits:
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
                 
        
        if self.vel.y < -1 and hits: 
            if self.pos.y > hits[0].rect.bottom and self.jumping is True:
                self.vel.y = 0
                    
                    
                

 
 
class platform(pygame.sprite.Sprite):
    def __init__(self, w, h, w1, h1):
        super().__init__()
        self.surf = pygame.Surface((w, h))
        self.surf.fill((212,238,227))
        self.rect = self.surf.get_rect(center = (w1, h1))
 
    def move(self):
        pass
 
PT1 = platform(WIDTH ,20, WIDTH/2, HEIGHT - 10)
PT2 = platform(50, 10, 300, 380)
PT3 = platform(70, 10, 180, 320)
PT4 = platform(35, 10, 120, 225)
PT5 = platform(35, 10, 340, 290)
PT6 = platform(25, 10, 70, 185)
PT7 = platform(30, 10, 275, 200)
PT8 = platform(60, 10, 195, 140)
PT9 = platform(70, 10, 340, 75)
P1 = Player()

 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(PT2)
all_sprites.add(PT3)
all_sprites.add(PT4)
all_sprites.add(PT5)
all_sprites.add(PT6)
all_sprites.add(PT7)
all_sprites.add(PT8)
all_sprites.add(P1)
all_sprites.add(PT9)

platforms = pygame.sprite.Group()
platforms.add(PT2)
platforms.add(PT1)
platforms.add(PT3)
platforms.add(PT4)
platforms.add(PT5)
platforms.add(PT6)
platforms.add(PT7)
platforms.add(PT8)
platforms.add(PT9)
 
 
while True:
    P1.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()
         
    displaysurface.fill((247,215,215))
    P1.update()
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    
    P1.update()
 
    pygame.display.update()
    FramePerSec.tick(FPS)
    
    P1.update()