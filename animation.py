import os
import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.sprite_name = sprite_name
        self.image = pygame.image.load(f'{sprite_name}/{sprite_name}01.png')
        self.current_image = 0
        self.images = self.load_animation_images(sprite_name) 
        self.speed = 2


    def animate(self):
        self.current_image += 1
        self.image_to_take= int(self.current_image*self.speed)
        if self.image_to_take >= len(self.images):
            self.restore()
        self.image = self.images[self.image_to_take]
    
    def restore(self):
        self.current_image = 0
        self.speed = 0.1
        self.images = self.load_animation_images(self.sprite_name)
        self.image_to_take = int(self.current_image * self.speed)
    
    def load_animation_images(self,sprite_name):
        images = []
        path = f"{sprite_name}"
        folder = os.listdir(path)
        print(folder)

        for file in folder:
            image_path = path + "/" + file
            print(image_path)
            images.append(pygame.image.load(image_path))
            print(len(images))
        self.current_image = 0
        return images
