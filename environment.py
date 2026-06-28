import numpy as np
import pygame
import math
import gymnasium as gym
from gymnasium import spaces

class RacingEnv(gym.Env):

    def __init__(self):
        
        super().__init__()
        pygame.init()

        self.WIDTH = 1000
        self.HEIGHT = 700

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Racing RL Environment")

        # Load the track image created using OpenCV
        self.track_image = pygame.image.load("track.png")

        # Colors
        self.GREEN = (0, 180, 0)
        self.GRAY = (120, 120, 120)
        self.BLACK = (0, 0, 0)

        # Track
        self.outer_track = pygame.Rect(100, 100, 800, 500)
        self.inner_track = pygame.Rect(250, 250, 500, 200)

        # Car
        self.car_x = 150
        self.car_y = 150
        self.car_angle = 0

        # Physics
        self.speed = 0
        self.max_speed = 6
        self.acceleration = 0.15
        self.friction = 0.05
        self.rotation_speed = 3

        # Sensors
        self.sensor_angles = [-60, -30, 0, 30, 60]
        self.sensor_length = 150

        # Gymnasium spaces
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0,high=self.sensor_length,shape=(5,),dtype=np.float32)

        self.clock = pygame.time.Clock()
    
    def reset(self, seed=None, options=None):
     super().reset(seed=seed)

     self.car_x = 150
     self.car_y = 150
     self.car_angle = 0
     self.speed = 0

     return self.get_observation(), {}
    
    def step(self, action):

      # Action meanings:
      # 0 = do nothing
      # 1 = left
      # 2 = right
      # 3 = accelerate

     if action == 1:
        self.car_angle += self.rotation_speed

     if action == 2:
        self.car_angle -= self.rotation_speed

     if action == 3:
        self.speed += self.acceleration
        if self.speed > self.max_speed:
            self.speed = self.max_speed
     else:
        self.speed -= self.friction
        if self.speed < 0:
            self.speed = 0

    # Move car
     self.car_x += self.speed * math.sin(math.radians(self.car_angle))
     self.car_y -= self.speed * math.cos(math.radians(self.car_angle))

    # Collision
     inside_outer = self.outer_track.collidepoint(self.car_x, self.car_y)
     inside_inner = self.inner_track.collidepoint(self.car_x, self.car_y)

     crashed = (not inside_outer) or inside_inner

     if crashed:
      reward = -10

     elif self.speed < 0.1:
      reward = -0.05
 
     else:
      reward = 0.01 + 0.05 * (self.speed / self.max_speed)

     terminated = crashed
     truncated = False

     return (self.get_observation(),reward,terminated,truncated,{})
    
    def cast_sensor(self, angle):

     total_angle = self.car_angle + angle

     for distance in range(self.sensor_length):

        test_x = self.car_x + distance * math.sin(math.radians(total_angle))
        test_y = self.car_y - distance * math.cos(math.radians(total_angle))

        if (not self.outer_track.collidepoint(test_x, test_y)) or self.inner_track.collidepoint(test_x, test_y):
            return distance

     return self.sensor_length
    
    def get_observation(self):

     readings = []

     for angle in self.sensor_angles:
        readings.append(self.cast_sensor(angle))

     return np.array(readings, dtype=np.float32)
    
    def render(self):

     self.screen.blit(self.track_image, (0, 0))
     
    # Car triangle
     car_points = [(0, -20), (-10, 10), (10, 10)]
     rotated = []

     for x, y in car_points:
        rx = x * math.cos(math.radians(self.car_angle)) - y * math.sin(math.radians(self.car_angle))
        ry = x * math.sin(math.radians(self.car_angle)) + y * math.cos(math.radians(self.car_angle))
        rotated.append((self.car_x + rx, self.car_y + ry))

     pygame.draw.polygon(self.screen, self.BLACK, rotated)

     pygame.display.flip()
     self.clock.tick(60)