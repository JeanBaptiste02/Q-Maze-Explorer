# Dynamic Maze Solver with Q-Learning

## Overview

This program implements a dynamic maze-solving algorithm using Q-Learning, a type of reinforcement learning. The agent learns to navigate a maze by trial and error, balancing exploration and exploitation. The maze is generated randomly using a perfect maze generation algorithm.

## Features

- **Maze Generation**: A perfect maze is generated, where all paths are connected, and there are no loops.
- **Q-Learning**: The agent uses Q-Learning to learn the optimal path through the maze, adjusting its actions based on the rewards it receives.
- **Real-time Visualization**: The current state of the maze, including the agent's position, is displayed in real-time.

## Parameters

- **Learning Rate (alpha)**: Determines how much the Q-values are updated based on the new information.
- **Discount Factor (gamma)**: Controls the importance of future rewards.
- **Exploration Rate (epsilon)**: Probability of the agent exploring new actions rather than exploiting learned actions.

## Installation

1. Install Python 3.x if not already installed.
2. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

## Running the Program

1. Run the Python script.
2. A graphical interface will open showing the maze and the agent’s movement.
3. The agent will explore the maze and gradually learn the optimal path to the exit.
