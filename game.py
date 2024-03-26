""" Cherry Game v1.00 """

import pygame
import sys
# internal files...
from code_files.objects import ObjectPhysics
from code_files.textures import ImageLoader


class CherryGame:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Cherry')

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.assets = {
            'player': ImageLoader.load("Player/player_1.png")
        }
        self.player = ObjectPhysics(self, 'player', (20, 400), (10, 20))
        self.movement = [False, False]
        self.__run()

    @staticmethod
    def __game_exit():
        pygame.quit()
        sys.exit()

    def __manage_events(self):
        """ Managing events in game """
        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.__game_exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.movement[0] = True
                if event.key == pygame.K_RIGHT:
                    self.movement[1] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.movement[0] = False
                if event.key == pygame.K_RIGHT:
                    self.movement[1] = False

    def __screen_management(self):
        """ Managing screen """
        self.screen.fill((0, 0, 0))
        self.player.update_position((self.movement[1] - self.movement[0], 0))
        self.player.render(self.screen)

    def __run(self):
        """ Runing game in the loop """
        while True:
            self.__screen_management()
            self.__manage_events()
            pygame.display.update()
            self.clock.tick(60)


CherryGame()