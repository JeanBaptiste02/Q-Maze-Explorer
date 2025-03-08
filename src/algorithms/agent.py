import random
import numpy as np # type: ignore
from q_maze_config import EPSILON, NUM_ACTIONS

def choose_action(Q_table, x, y):
    """ Choisit l'action avec la stratégie epsilon-greedy """
    if random.uniform(0, 1) < EPSILON:
        return random.randint(0, NUM_ACTIONS - 1)  
    return np.argmax(Q_table[x, y])

def move_agent(maze, agent_pos, action):
    """ Déplace l'agent dans le labyrinthe """
    x, y = agent_pos
    if action == 0 and x > 0 and maze[x - 1, y] != 1:  
        return (x - 1, y)
    if action == 1 and y < len(maze) - 1 and maze[x, y + 1] != 1:  
        return (x, y + 1)
    if action == 2 and x < len(maze) - 1 and maze[x + 1, y] != 1:  
        return (x + 1, y)
    if action == 3 and y > 0 and maze[x, y - 1] != 1:  
        return (x, y - 1)
    return agent_pos  # Si l'action n'est pas valide, on ne bouge pas