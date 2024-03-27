import pygame
import os


class ImageLoader:
    """ Class to support loading Images """

    BASE_IMG_PATH = 'Resources/Images/'

    def __init__(self):
        pass

    @staticmethod
    def load(path: str) -> pygame.image:
        """
        :param path: Path to image
        :return: Image
        """
        img = pygame.image.load(ImageLoader.BASE_IMG_PATH + path).convert()
        img.set_colorkey((0, 0, 0))
        return img

    @staticmethod
    def multiple_load(path: str) -> list:
        """
        :param path: Path to images
        :return: List of images path in given path
        """
        images = []
        for img_name in os.listdir(ImageLoader.BASE_IMG_PATH + path):
            images.append(ImageLoader.load(path + '/' + img_name))
        return images

