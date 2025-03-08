import numpy as np # type: ignore
import random
from q_maze_config import MAZE_SIZE

def generate_perfect_maze():
    """ Génère un labyrinthe parfait """
    maze = np.ones((MAZE_SIZE, MAZE_SIZE))  

    def carve(x, y):
        maze[x, y] = 0  
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and maze[nx, ny] == 1:
                maze[x + dx, y + dy] = 0
                carve(nx, ny)

    carve(1, 1)
    maze[0, 1] = 0  
    maze[MAZE_SIZE - 1, MAZE_SIZE - 2] = 0  
    maze[MAZE_SIZE - 1, MAZE_SIZE - 1] = 2  

    return maze