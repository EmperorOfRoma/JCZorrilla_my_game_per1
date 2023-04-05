# File created by: Jaime Cesar Zorrilla
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

'''
My goal is:

Player health
When this reaches 0, game ends and restarts.

Goomba mob
A mob that moves slowly and is easily defeated, but can still damage. This comes with way to attack.

Respawning enemies
Unsure if I want this, but an idea.

Invisible wall
Keep player on screen.

Moving screen
Make the map larger than what fits on sceen.

'''

# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file
class Game:
    # initializes the screen
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.SCORE = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        # All sprites appear
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,1):
            m = Mob(20,20,WHITE)
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    # plays game
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    # game inputs
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    # how the game responds to certain situations
    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            if hits[0].variant == "disappearing":
                hits[0].kill()
            elif hits[0].variant == "bouncey":
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = -PLAYER_JUMP
            elif hits[0].variant == "leftwall":
                self.player.pos.x = 10
                self.player.vel.x = PLAYER_PUSH
            elif hits[0].variant == "rightwall":
                self.player.pos.x = WIDTH - 10
                self.player.vel.x = -PLAYER_PUSH    
            else:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()