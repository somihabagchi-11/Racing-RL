import pygame
from environment import RacingEnv

env = RacingEnv()

obs = env.reset()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action = 3  # always accelerate (for testing)

    obs, reward, done, info = env.step(action)

    env.render()

    if done:
        print("Crashed!")
        env.reset()