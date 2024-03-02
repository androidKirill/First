import sys
from abc import ABC, abstractmethod
from math import cos, sin, pi

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))


class Color:
    # Храним цвета
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)


class PGScene(ABC):
    # Сцена
    bgcolor = (0, 0, 0)

    def __init__(self):
        self.screen = screen
        self.sceneover = False
        self.objects = []

    def draw(self):
        # Заливаем черной краской
        # и отрисовываем все объекты
        self.screen.fill(self.bgcolor)
        for item in self.objects:
            item.draw()

    def process_events(self):
        # Обрабатываем события выхода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sceneover = True
            # Для каждого event а,
            # который сейчас пустой
            self.process_event(event)

    def process_event(self, event):
        pass

    @abstractmethod
    def process_logic(self):
        for item in self.objects:
            item.logic()

    def main_loop(self):
        # События, логика, отрисовка
        #  и подождать 10 мили секунд
        while not self.sceneover:
            self.process_events()
            self.process_logic()
            self.draw()
            pygame.display.flip()
            pygame.time.wait(10)


class GameScene(PGScene):
    # Сцена
    def __init__(self):
        # Создание объекта танка и кнопочек
        super().__init__()
        self.panzer = Panzer(200, 200)
        self.buttons = {
            'up': StateRect(100, 500, 20, 20, Color.GREEN, Color.RED),
            'down': StateRect(100, 530, 20, 20, Color.GREEN, Color.RED),
            'left': StateRect(70, 530, 20, 20, Color.GREEN, Color.RED),
            'right': StateRect(130, 530, 20, 20, Color.GREEN, Color.RED),
        }
        self.objects.append(self.panzer)
        self.objects += self.buttons.values()

    def process_logic(self):
        # В этом методе нужно будет ещё что-то дописать)
        super().process_logic()


class PGObject(ABC):
    # Класс отрисовываемых объектов
    def __init__(self):
        self.screen = screen

    @abstractmethod
    def draw(self):
        pass

    def logic(self):
        pass


class Panzer(PGObject):
    # Танк
    def __init__(self, x, y):
        # Картинка, которая находится на какой-то позиции,
        # которая умеет двигаться с какой-то скоростью
        # и она умеет поворачиваться
        super().__init__()
        self.rotated_image = self.image = pygame.image.load("panzer.png")
        self.rotated_rect = self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.direction = 0
        self.speed = 0
        self.max_speed = 1

    def draw(self):
        # Отрисовка
        self.rect.x = self.x - self.rect.width // 2
        self.rect.y = self.y - self.rect.height // 2
        self.rotated_rect = self.rotated_image.get_rect(
            center=self.rect.center)
        self.screen.blit(self.rotated_image, self.rotated_rect)

    def move(self):
        # Установка скорости
        self.speed = self.max_speed

    def stop(self):
        self.speed = 0

    def step(self):
        # Движение
        self.x += cos(self.direction) * self.speed
        self.y += sin(self.direction) * self.speed

    def rotate(self, angle):
        self.direction += angle
        self.rotated_image = pygame.transform.rotate(
            self.image, -self.direction / pi * 180)
        self.rotated_rect = self.rotated_image.get_rect(
            center=self.rect.center)

    def logic(self):
        self.step()


class StateRect(PGObject):
    # Кнопки, на которые нельзя нажимать
    # маленький прямоугольник, если он активирован
    # одним цветом, если нет другим цветом
    def __init__(self, x, y, width, height, color_enabled, color_disabled):
        super().__init__()
        self.rect = (x, y, width, height)
        self.color_enabled = color_enabled
        self.color_disabled = color_disabled
        self.enabled = False

    def draw(self):
        color = self.color_enabled if self.enabled else self.color_disabled,
        pygame.draw.rect(self.screen, color, self.rect, 0)

    def set_enabled(self, enabled):
        self.enabled = enabled


if __name__ == "__main__":
    gs = GameScene()
    gs.main_loop()
    sys.exit()
