
# Reinforcement Learning Projects

Welcome to my repository where I explore Reinforcement Learning (RL) through two engaging projects: a version of the classic game "Snake" and a simulation called "Ice". These projects are implemented using Q-learning and Deep Q-Learning (DQL) to demonstrate the effectiveness of these algorithms in different scenarios.

## Projects

### Snake Game

**Objective:** The goal of the Snake game is for the snake to eat food that appears at random points on the screen, growing in length with each piece eaten without running into its own tail or the edges of the play area.

**Algorithm Used:** Deep Q-Learning (DQL)
- **Framework:** TensorFlow/Keras
- **Key Features:** Implementation of a neural network to estimate Q-values, which guide the snake to make optimal decisions at each step.

### Ice Simulation

**Objective:** Navigate through a slippery ice environment where the agent must find the safest path to a designated goal without slipping away.

**Algorithm Used:** Q-Learning
- **Technique:** Utilizes a table of Q-values to represent the environment, updating values as the agent learns from interactions, aiming to maximize the total reward by learning the best actions to take in various states.

## About Reinforcement Learning (RL)

Reinforcement Learning is a type of machine learning where an agent learns to make decisions by performing certain actions and receiving rewards or penalties in return. It is distinguished by its ability to learn optimal actions based on trial and error, which simulates a form of learning similar to natural learning processes found in intelligent beings. RL is widely applicable in various domains such as robotics, automated trading, gaming, and more.

## Requirements

To run the projects in this repository, you will need the following:

- Python 3.6 or higher
- TensorFlow 2.x
- NumPy
- Matplotlib (for visualization)

You can install all required packages using pip:

```bash
pip install tensorflow numpy matplotlib
```
