import pygame


class Tilemap:
    """ Class to create environment in the game """
    NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
    PHYSICS_TILES = {'grass', 'stone'}

    def __init__(self, game, tile_size: int = 32):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        for i in range(10):
            self.tilemap[str(3+i)+";10"] = {'type': 'grass', 'variant': 0, 'pos': (3+i, 10)}
            self.tilemap["10;"+str(5+i)] = {'type': 'stone', 'variant': 0, 'pos': (10, 5+i)}

    def tiles_around(self, pos: list) -> list:
        """ Method to check whether the object with the given location has encountered any obstacle
        :param pos: Position of the object
        :return: List of encountered obstacls - tiles
        """
        tiles = []
        tile_location = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in Tilemap.NEIGHBOR_OFFSETS:
            check_location = str(tile_location[0] + offset[0]) + ';' + str(tile_location[1] + offset[1])
            if check_location in self.tilemap:
                tiles.append(self.tilemap[check_location])
        return tiles

    def pyhsics_rects_around(self, pos):
        """ Method to define interaction bewteen object and type of tiles
        Only interaction on this moment is to create rectangle in tile position to prevent object from moving
        :param pos: Position of the object
        :return: List of created rectangles
        """
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in Tilemap.PHYSICS_TILES:
                rects.append(pygame.Rect(int(tile['pos'][0]*self.tile_size), int(tile['pos'][1]*self.tile_size),
                                         int(self.tile_size), int(self.tile_size)))
        return rects

    def render(self, surf, offset: tuple = (0, 0)):
        """ Method to render tile objects
        :param surf: Surface on which rendered items shall appear
        :param offset: Camera offset
        :return:
        """
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']],
                      (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))

        # for x in range(int(offset[0]) // self.tile_size ,
        #                (int(offset[0]) + surf.get_width() // self.tile_size + 1)):
        #     for y in range(int(offset[1]) // self.tile_size,
        #                    (int(offset[1]) + surf.get_height() // self.tile_size + 1)):
        #         loc = str(x) + ";" + str(y)
        #         if loc in self.tilemap:
        #             tile = self.tilemap[loc]
        #             surf.blit(self.game.assets[tile['type']][tile['variant']],
        #                       (int(tile['pos'][0] * self.tile_size) - offset[0],
        #                        int(tile['pos'][1] * self.tile_size) - offset[1]))

        for loc, tile in self.tilemap.items():
            surf.blit(self.game.assets[tile['type']][tile['variant']], (int(tile['pos'][0]*self.tile_size) - offset[0],
                                                                        int(tile['pos'][1]*self.tile_size) - offset[1]))
