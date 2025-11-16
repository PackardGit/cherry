import pygame
import sys

from code_files.textures import ImageLoader
from code_files.background import Tilemap

RENDER_SCALE = 2


class Editor:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('editor')

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.movement = [False, False]
        self.assets = {
            #'decor':  ImageLoader.multiple_load("Tiles/Decor"),
            'grass': ImageLoader.multiple_load("Tiles/Grass"),
            # 'large_decor': ImageLoader.multiple_load("Tiles/Large_decor"),
            'stone': ImageLoader.multiple_load("Tiles/Stone"),
            'mountain': ImageLoader.multiple_load("Tiles/Mountains"),
            'palms': ImageLoader.multiple_load("Tiles/Palms"),
            'stars': ImageLoader.multiple_load("Tiles/Stars"),
        }

        self.movement = [False, False, False, False]
        self.tilemap = Tilemap(self, tile_size=32)

        self.scroll = [0, 0]

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0
        self.clicking = False
        self.right_clicking = False
        self.shift = False
        self.__run()

    @staticmethod
    def __game_exit():
        """ Exiting game """
        pygame.quit()
        sys.exit()

    def __manage_events(self):
        """ Managing events in game """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicking = True
                if event.button == 3:
                    self.right_clicking = True
                if self.shift:
                    if event.button == 4:
                        self.tile_variant = (self.tile_variant - 1) % len(self.assets[self.tile_list[self.tile_group]])
                    if event.button == 5:
                        self.tile_variant = (self.tile_variant + 1) % len(self.assets[self.tile_list[self.tile_group]])
                else:
                    if event.button == 4:
                        self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                    if event.button == 5:
                        self.tile_group = (self.tile_group + 1) % len(self.tile_list)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicking = False
                if event.button == 3:
                    self.right_clicking = False

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.__game_exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    self.shift = True
                if event.key == pygame.K_CAPSLOCK:
                    self.shift = False
                    self.tile_variant = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.movement[0] = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.movement[1] = True
                if event.key == pygame.K_SPACE:
                    self.movement[2] = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.movement[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.movement[0] = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.movement[1] = False
                if event.key == pygame.K_SPACE:
                    self.movement[2] = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.movement[3] = True

    def __screen_management(self):
        """ Managing screen """
        self.screen.fill((0, 0, 0))

        self.scroll[0] += (self.movement[1] - self.movement[0]) * 4
        render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
        self.tilemap.render(self.screen, offset=render_scroll)
        current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant]
        current_tile_img.set_alpha(255)
        mpos = pygame.mouse.get_pos()
        tile_pos = (int((mpos[0] + self.scroll[0]) // self.tilemap.tile_size),
                    int((mpos[1] + self.scroll[1]) // self.tilemap.tile_size))

        self.screen.blit(current_tile_img, (tile_pos[0]*self.tilemap.tile_size-self.scroll[0],
                                            tile_pos[1]*self.tilemap.tile_size-self.scroll[1]))

        if self.clicking:
            self.tilemap.tilemap[str(tile_pos[0]) + ";" + str(tile_pos[1])] = {
                'type': self.tile_list[self.tile_group], "variant": self.tile_variant, "pos": tile_pos}
        if self.right_clicking:
            tile_loc = str(tile_pos[0]) + ";" + str(tile_pos[1])
            if tile_loc in self.tilemap.tilemap:
                del self.tilemap.tilemap[tile_loc]
        self.screen.blit(current_tile_img, (5, 5))

    def __run(self):
        """ Runing game in the loop """
        while True:
            self.__screen_management()
            self.__manage_events()
            pygame.display.update()
            self.clock.tick(120)


Editor()
