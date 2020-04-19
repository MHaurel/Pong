import pygame


class Ball:
    def __init__(self, x, y, radius, x_facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_facing = x_facing
        self.vel = 5
        self.hit_count = 0

    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius)

    def on_screen(self):
        return 0 < self.x < 900