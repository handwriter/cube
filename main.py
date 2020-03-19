import pygame


def draw_cube(w, hue):
    screen.fill(pygame.Color('black'))
    color = pygame.Color('black')
    color.hsva = (hue, 100, 75)
    pygame.draw.rect(screen, color, (150 - w // 4 * 3, 150 - w // 4, w, w))
    color.hsva = (hue, 100, 100)
    points = [(150 - w // 4 * 3, 150 - w // 4),
              (150 - w // 4, 150 - w // 4 * 3),
              (150 + w // 4 * 3, 150 - w // 4 * 3),
              (150 + w // 4, 150 - w // 4)]
    pygame.draw.polygon(screen, color, points)
    color.hsva = (hue, 100, 50)
    points = [(150 + w // 4, 150 + w // 4 * 3),
              (150 + w // 4, 150 - w // 4),
              (150 + w // 4 * 3, 150 - w // 4 * 3),
              (150 + w // 4 * 3, 150 + w // 4)]
    pygame.draw.polygon(screen, color, points)


pygame.init()
w, hue = [int(el) for el in input().split()]
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
draw_cube(w, hue)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()