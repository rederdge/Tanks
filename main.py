import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Танки")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def load_image(path, size):
    try:
        image = pygame.image.load(path)
        return pygame.transform.scale(image, size)
    except pygame.error:
        print(f"Помилка завантаження зображення: {path}")
        pygame.quit()
        sys.exit()

player_tank_img = load_image("ptank.png", (50, 50))
enemy_tank_img = load_image("etank.png", (50, 50))
bullet_img = load_image("bullet.png", (10, 10))

class Tank:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.angle = 0
        self.health = 100
    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, new_rect.topleft)
        self.draw_health_bar()

    def draw_health_bar(self):
        bar_width = self.width
        bar_height = 5
        fill = (self.health / 100) * bar_width
        outline_rect = pygame.Rect(self.x, self.y - 10, bar_width, bar_height)
        fill_rect = pygame.Rect(self.x, self.y - 10, fill, bar_height)
        pygame.draw.rect(screen, RED, outline_rect)
        pygame.draw.rect(screen, GREEN, fill_rect)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.boundaries()

    def rotate(self, angle):
        self.angle += angle

    def boundaries(self):
        self.x = max(0, min(WIDTH - self.width, self.x))
        self.y = max(0, min(HEIGHT - self.height, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

class Bullet:
    def __init__(self, x, y, angle, speed=7):
        self.image = bullet_img
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def move(self):
        direction = pygame.math.Vector2(1, 0).rotate(-self.angle)
        self.x += self.speed * direction.x
        self.y += self.speed * direction.y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def main():
    clock = pygame.time.Clock()
    running = True

    player = Tank(player_tank_img, WIDTH // 2, HEIGHT // 2, 5)
    enemy = Tank(enemy_tank_img, random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50), 3)
    bullets = []

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.x + 25, player.y + 25, player.angle))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed, 0)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed, 0)
        if keys[pygame.K_UP]:
            player.move(0, -player.speed)
        if keys[pygame.K_DOWN]:
            player.move(0, player.speed)
        if keys[pygame.K_a]:
            player.rotate(-5)
        if keys[pygame.K_d]:
            player.rotate(5)

        enemy_dx = random.choice([-enemy.speed, 0, enemy.speed])
        enemy_dy = random.choice([-enemy.speed, 0, enemy.speed])
        enemy.move(enemy_dx, enemy_dy)

        player.draw()
        enemy.draw()

        for bullet in bullets[:]:
            bullet.move()
            bullet.draw()
            if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                bullets.remove(bullet)
            elif bullet.rect.colliderect(enemy.rect):
                enemy.health -= 10
                bullets.remove(bullet)

        if enemy.health <= 0:
            print("Ворог знищений")
            running = False

        if player.rect.colliderect(enemy.rect):
            print("Столкновение!")
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()        