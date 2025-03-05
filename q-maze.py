import tkinter as tk
import numpy as np

# Dimensions du labyrinthe
maze_size = 10
maze_width = 500
maze_height = 500

# Labyrinthe initialisé
maze = np.zeros((maze_size, maze_size))  # 0 = libre

# Fonction de visualisation
def draw_maze():
    canvas.delete('all')
    cell_width = maze_width // maze_size
    cell_height = maze_height // maze_size
    
    for i in range(maze_size):
        for j in range(maze_size):
            x0, y0 = j * cell_width, i * cell_height
            x1, y1 = (j + 1) * cell_width, (i + 1) * cell_height
            canvas.create_rectangle(x0, y0, x1, y1, fill='white', outline='lightgray')

# Initialisation de l'interface
root = tk.Tk()
root.title("Labyrinthe Dynamique avec Q-Learning")
canvas = tk.Canvas(root, width=maze_width, height=maze_height)
canvas.pack()

draw_maze()  # Dessine le labyrinthe

# Lancer l'application
root.mainloop()