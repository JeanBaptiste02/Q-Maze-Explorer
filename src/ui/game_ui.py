import tkinter as tk
from maze_renderer import draw_maze
from maze_generator import generate_perfect_maze
from agent import choose_action, move_agent
from q_learning import update_Q_table
import numpy as np # type: ignore

def start_game():
    root = tk.Tk()
    root.title("Q-Maze Explorer")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    maze = generate_perfect_maze()
    agent_pos = (0, 0)
    Q_table = np.zeros((10, 10, 4))

    def update():
        nonlocal agent_pos
        action = choose_action(Q_table, *agent_pos)
        next_pos = move_agent(maze, agent_pos, action)
        reward = 1 if next_pos == (9, 9) else -1 if maze[next_pos] == 1 else 0
        update_Q_table(Q_table, *agent_pos, action, reward, *next_pos)
        agent_pos = next_pos
        draw_maze(canvas, maze, agent_pos, 500, 500)
        root.after(100, update)

    update()
    root.mainloop()