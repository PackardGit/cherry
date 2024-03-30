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
        self.collisions = {"up": False, "down": False, "right": False, "left": False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0]*3, self.size[1])

    def update_position(self, tilemap: any, movement: tuple = (0, 0)) -> None:
        """
        :param tilemap: Object of background and foreground objects and its position
        :param movement: Movement of the object to be made
        :return: None
        """
        self.collisions = {"up": False, "down": False, "right": False, "left": False}
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.pyhsics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # Collision while moving right
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions["right"] = True
                # Collision while moving left
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions["left"] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.pyhsics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # Collision while falling down
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions["down"] = True
                # Collision while going up
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions["up"] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.collisions["down"] or self.collisions["up"]:
            self.velocity[1] = 0

    def render(self, surface: pygame.display, asset: str, offset: tuple = (0, 0)) -> None:
        """
        :param surface: Place on which player is displayed
        :param asset: Asset to be rendered
        :param offset: Camera offset
        :return: None
        """
        surface.blit(self.game.assets[asset], (self.pos[0] - offset[0], self.pos[1] - offset[1]))

