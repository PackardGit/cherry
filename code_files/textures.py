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
        img.set_colorkey((255, 255, 255))
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


class Animation:

    def __init__(self, images: list, img_dur: int = 5, loop: bool = True):
        self.images = images
        self.img_duration = img_dur
        self.loop = loop
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True

    def img(self):
        return self.images[int(self.frame / self.img_duration)]


