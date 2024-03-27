import pygame


class ObjectPhysics:
    """ Class to support rendering objects on the screen """

    def __init__(self, game, object_type, position, size):
        """
        :param game: Object that represent the game
        :param object_type: Type of the object
        :param position: Position of the object
        :param size: Size of the object
        """
        self.game = game
        self.type = object_type
        self.pos = list(position)
        self.size = size
        self.velocity = [0, 0]

    def update_position(self, movement: tuple = (0, 0)) -> None:
        """
        :param movement: Movement of the object to be made
        :return: None
        """
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

    def render(self, surface: pygame.display, asset: str) -> None:
        """
        :param surface: Place on which player is displayed
        :param asset: Asset to be rendered
        :return: None
        """
        surface.blit(self.game.assets[asset], self.pos)

