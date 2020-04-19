import pygame

from Player import Player
from Ball import Ball
import random

pygame.font.init()


WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong !")


def main():
    run = True
    FPS = 60
    score_font = pygame.font.SysFont("comicsans", 60)

    # 1 for right and -1 for left
    x_facing = random.choice([-1, 1])
    y_facing = random.choice([-1, 1])

    left_player = Player(10, 250)
    right_player = Player(WIDTH - 30, 250)

    last_hit_count = []

    ball = Ball(450, 300, 10, x_facing)

    lost_count = 0

    clock = pygame.time.Clock()

    def redraw_window():

        left_player_label = score_font.render(f"{left_player.score}", 1, (255, 255, 255))
        right_player_label = score_font.render(f"{right_player.score}", 1, (255, 255, 255))

        WIN.blit(left_player_label, (70, 10))
        WIN.blit(right_player_label, (WIDTH - right_player_label.get_width() - 70, 10))

        left_player.draw(WIN)
        right_player.draw(WIN)

        if ball.on_screen():
            # print("La balle est dans l'écran de jeu")
            ball.draw(WIN)

        if ball.hit_count > 0 and ball.hit_count % 2 == 0:
            if ball.hit_count not in last_hit_count:
                last_hit_count.append(ball.hit_count)
                ball.vel += 1

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if not ball.on_screen():
            # print("La balle doit être repositionnée au centre de l'écran")
            if x_facing == 1:
                left_player.score += 1
            elif x_facing == -1:
                right_player.score += 1

            x_facing = random.choice([-1, 1])
            y_facing = random.choice([-1, 1])
            ball.vel = 5
            ball.x = 450
            ball.y = 300

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ball.x += ball.vel * x_facing
        ball.y += ball.vel * y_facing

        """
        print("balle x:", ball.x)
        print("balle y:", ball.y)
        print("valeur minimum du player droit:", right_player.y)
        print("Valeur maximum du player droit:", right_player.y + right_player.height)
        """

        # Right player lose
        if left_player.score == 5:
            print("Left player won !!")

        # Left player lose
        elif right_player.score == 5:
            print("Right player won !!")

        if right_player.y < ball.y < (right_player.y + right_player.height):
            if ball.x + (ball.vel * x_facing) > right_player.x:
                x_facing = -1
                ball.hit_count += 1

        if left_player.y < ball.y < (left_player.y + left_player.height):
            if ball.x + (ball.vel * x_facing) < left_player.x + left_player.width:
                x_facing = 1
                ball.hit_count += 1

        if ball.y + ball.vel * y_facing < 0:
            y_facing = 1

        if ball.y + ball.vel * y_facing > HEIGHT:
            y_facing = -1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_player.y - left_player.vel > 0:
            left_player.y -= left_player.vel
        if keys[pygame.K_s] and left_player.y + left_player.vel + left_player.height < HEIGHT:
            left_player.y += left_player.vel
        if keys[pygame.K_UP] and right_player.y - right_player.vel > 0:
            right_player.y -= right_player.vel
        if keys[pygame.K_DOWN] and right_player.y + right_player.vel + right_player.height < HEIGHT:
            right_player.y += right_player.vel

        WIN.fill((0, 0, 0))

    pygame.quit()


def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        title_label = title_font.render("Press the mouse button to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, HEIGHT / 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()
