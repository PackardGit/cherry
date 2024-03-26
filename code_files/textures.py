import pygame


class ImageLoader:
    BASE_IMG_PATH = 'Resources/Images/'

    def __init__(self):
        pass

    @staticmethod
    def load(path):
        img = pygame.image.load(ImageLoader.BASE_IMG_PATH + path).convert()
        img.set_colorkey((0, 0, 0))
        return img

