import numpy as np # type: ignore
from q_maze_config import ALPHA, GAMMA

def update_Q_table(Q_table, x, y, action, reward, next_x, next_y):
    """ Met à jour la Q-table selon l'algorithme Q-learning """
    max_q_next = np.max(Q_table[next_x, next_y])  
    Q_table[x, y, action] += ALPHA * (reward + GAMMA * max_q_next - Q_table[x, y, action])