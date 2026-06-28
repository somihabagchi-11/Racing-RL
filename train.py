from stable_baselines3 import PPO
from environment import RacingEnv

env = RacingEnv()

model = PPO("MlpPolicy",env,verbose=1)

model.learn(total_timesteps=200000)

model.save("models/racing_ppo")

env.close()