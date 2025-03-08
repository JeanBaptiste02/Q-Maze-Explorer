import tkinter as tk

def draw_maze(canvas, maze, agent_pos, width, height):
    """ Affiche le labyrinthe et l'agent """
    canvas.delete('all')
    cell_width = width // len(maze)
    cell_height = height // len(maze)
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            x0, y0 = j * cell_width, i * cell_height
            x1, y1 = (j + 1) * cell_width, (i + 1) * cell_height
            color = 'white' if maze[i, j] == 0 else 'brown'
            if maze[i, j] == 2:
                color = 'green'
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='gray')

    x, y = agent_pos
    agent_x0, agent_y0 = y * cell_width + 5, x * cell_height + 5
    agent_x1, agent_y1 = (y + 1) * cell_width - 5, (x + 1) * cell_height - 5
    canvas.create_oval(agent_x0, agent_y0, agent_x1, agent_y1, fill='red', outline='darkred')
