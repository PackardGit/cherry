import pygame


class ObjectPhysics:

    def __init__(self, game, object_type, position, size):
        self.game = game
        self.type = object_type
        self.pos = list(position)
        self.size = size
        self.velocity = [0, 0]

    def update_position(self, movement=(0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surface):
        surface.blit(self.game.assets['player'], self.pos)

