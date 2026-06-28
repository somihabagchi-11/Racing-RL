import pygame
import sys
import math

pygame.init()


WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Racing RL")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (120, 120, 120)
GREEN = (0, 180, 0)


outer_track = pygame.Rect(100, 100, 800, 500)
inner_track = pygame.Rect(250, 250, 500, 200)
clock = pygame.time.Clock()

# position of the car
car_x = 150
car_y = 150

# Car size
car_width = 20
car_height = 40

car_radius = 10

# Car direction (in degrees)
car_angle = 0

# Car movement
speed = 0
max_speed = 6
acceleration = 0.15
friction = 0.05
rotation_speed = 3

sensor_angles = [-60, -30, 0, 30, 60]
sensor_length = 150


def cast_sensor(car_x, car_y, car_angle, angle):
    total_angle = car_angle + angle

    for distance in range(sensor_length):

        test_x = car_x + distance * math.sin(math.radians(total_angle))
        test_y = car_y - distance * math.cos(math.radians(total_angle))

        inside_outer = outer_track.collidepoint(test_x, test_y)
        inside_inner = inner_track.collidepoint(test_x, test_y)

        if (not inside_outer) or inside_inner:
            return distance

    return sensor_length

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
     car_angle += rotation_speed

    if keys[pygame.K_RIGHT]:
     car_angle -= rotation_speed

    if keys[pygame.K_UP]:
     speed += acceleration
      

     if speed > max_speed:
       speed = max_speed
    else:
      speed -= friction

      if speed < 0:
        speed = 0

    car_x += speed * math.sin(math.radians(car_angle))
    car_y -= speed * math.cos(math.radians(car_angle))

    # Is the car inside the outer track?
    inside_outer = outer_track.collidepoint(car_x, car_y)

    # Is the car inside the hole?
    inside_inner = inner_track.collidepoint(car_x, car_y)

    crashed = (not inside_outer) or inside_inner

    screen.fill(GREEN)

    pygame.draw.rect(screen, GRAY, outer_track)

    pygame.draw.rect(screen, GREEN, inner_track)

    # Triangle points (relative to the car's center)
    car_points = [(0, -20),(-10, 10),(10, 10)]

    rotated_points = []

    for x, y in car_points:

      rotated_x = x * math.cos(math.radians(car_angle)) - y * math.sin(math.radians(car_angle))

      rotated_y = x * math.sin(math.radians(car_angle)) + y * math.cos(math.radians(car_angle))

      rotated_points.append((car_x + rotated_x, car_y + rotated_y))
    
    pygame.draw.polygon(screen, BLACK, rotated_points)

    if crashed:
      pygame.draw.circle(screen, (255, 0, 0), (int(car_x), int(car_y)), 12)
      print("Crash!")
    
    for angle in sensor_angles:

     distance = cast_sensor(car_x, car_y, car_angle, angle)

     total_angle = car_angle + angle

     end_x = car_x + distance * math.sin(math.radians(total_angle))
     end_y = car_y - distance * math.cos(math.radians(total_angle))

     pygame.draw.line(screen,(255, 0, 0),(car_x, car_y),(end_x, end_y),2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()