# Project Report 

## 1. About the project

This project presents an autonomous racing agent developed using RL techniques. The agent is trained using the Proximal Policy Optimization (PPO) algorithm to use a custom-built simulation environment. The environment is developed using Pygame and follows the Gymnasium interface to enable integration with modern RL libraries.

The agent learns to drive by interacting with the environment, receiving rewards for survival, and penalties for crashing. Over time, it improves its driving behavior through trial and error without any explicit programming of driving rules.

## 2. Objectives

- to build a custom simulation environment for a racing agent
- implementing RL using PPO
- training an agent to navigate without crashing
- understanding environment-agent interaction in RL

## 3. Technologies Used
- Python
- Gymnasium
- Stable-Baselines3
- Pygame
- OpenCV
- NumPy
(mentioned in the requirements.txt file with their versions)

## 4. System Design

The system consists of:
- Car: I could not make a complex car design so I made a car in triangular shape for reference
- Environment: custom racing track made using openCv
- Agent: PPO-based neural network policy
- State Space: car position and sensor-based observations
- Action Space: left, straight and right movement of the car
- Reward Function: reward system is based on survival 
- I also made a track.py file in the extras folder that manually moves the car and looks for crash with sensors for learning purposes without training the model.

## 5. Methodology

1. I first initialized the environment and made the track using openCv
2. the agent takes random actions initially
3. the observations are then collected from environment
4. the reward is calculated based on survival
5. PPO updates policy using collected experiences
6. over time the policy improves driving behavior

## 6. PPO Algorithm

I used PPO (Proximal Policy Optimization) over other algorithms as it ensures stable learning by limiting large updates to the policy network and it also improves training stability and is widely used in continuous and discrete control tasks.

## 7. Reward Function

the reward function used is quite simple:

- +1 for every step survived
- -1 or episode termination on collision

this encourages the agent to maximize the survival time.

## 8. Experimental Results

- Initially, the agent behaved randomly
- Collisions into the grass were frequent in early stages
- After training, the agent learnt to avoid boundaries
- I first trained the model with 50000 timesteps and later with 200000 timesteps
- the performance improved with increased training steps

## 9. Challenges Faced

- it took me a while to design a proper reward function
- stabilizing training with PPO also took time
- figuring out correct environment-agent interaction was tricky
- balancing speed and control of the car

## 10. Improvements made to achieve better performance
- converted the game into a Gymnasium environment
- continuous forward motion model
- fixed movement scaling
- implemented proper episode termination
- added survival-based reward structure
- improved sensor design
- integrated Stable-Baselines3 PPO algorithm
- 

