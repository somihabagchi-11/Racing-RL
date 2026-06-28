from stable_baselines3 import PPO
from environment import RacingEnv

env = RacingEnv()

model = PPO.load("models/racing_ppo")

obs, info = env.reset()

while True:

    action, _ = model.predict(obs)

    obs, reward, terminated, truncated, info = env.step(action)

    env.render()

    if terminated or truncated:
        obs, info = env.reset()