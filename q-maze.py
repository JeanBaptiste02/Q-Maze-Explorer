import tkinter as tk
import numpy as np
import random

# Paramètres du Q-Learning
alpha = 0.1  # Taux d'apprentissage
gamma = 0.9  # Importance des récompenses futures
epsilon = 0.2  # Probabilité d'exploration

# Dimensions du labyrinthe
maze_size = 10
maze_width = 500
maze_height = 500

# Actions possibles : 0 = haut, 1 = droite, 2 = bas, 3 = gauche
actions = ['Up', 'Right', 'Down', 'Left']
num_actions = len(actions)

# Q-table (état = position (x, y), action = mouvement)
Q_table = np.zeros((maze_size, maze_size, num_actions))

# Labyrinthe initialisé
maze = np.zeros((maze_size, maze_size))  # 0 = libre
agent_pos = (0, 0)  # Position de l'agent

# Fonction pour générer un labyrinthe parfait
def generate_perfect_maze():
    global maze
    maze = np.ones((maze_size, maze_size))  # Toutes les cases sont des murs

    def carve(x, y):
        maze[x, y] = 0  # On commence par creuser à la position (x, y)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < maze_size and 0 <= ny < maze_size and maze[nx, ny] == 1:
                maze[x + dx, y + dy] = 0
                carve(nx, ny)

    carve(1, 1)  # On commence à creuser à partir de (1, 1)
    maze[0, 1] = 0  # Entrée du labyrinthe
    maze[maze_size - 1, maze_size - 2] = 0  # Sortie du labyrinthe
    maze[maze_size - 1, maze_size - 1] = 2  # Marquer la sortie

# Fonction de visualisation
def draw_maze():
    canvas.delete('all')
    cell_width = maze_width // maze_size
    cell_height = maze_height // maze_size
    
    for i in range(maze_size):
        for j in range(maze_size):
            x0, y0 = j * cell_width, i * cell_height
            x1, y1 = (j + 1) * cell_width, (i + 1) * cell_height
            if maze[i, j] == 1:  # Obstacle
                canvas.create_rectangle(x0, y0, x1, y1, fill='brown', outline='brown')
            elif maze[i, j] == 2:  # Sortie
                canvas.create_rectangle(x0, y0, x1, y1, fill='green', outline='green')
            else:  # Case vide
                canvas.create_rectangle(x0, y0, x1, y1, fill='white', outline='lightgray')
    
    # Dessiner l'agent
    x, y = agent_pos
    agent_x0, agent_y0 = y * cell_width + 5, x * cell_height + 5
    agent_x1, agent_y1 = (y + 1) * cell_width - 5, (x + 1) * cell_height - 5
    canvas.create_oval(agent_x0, agent_y0, agent_x1, agent_y1, fill='red', outline='darkred')

# Initialisation de l'interface
root = tk.Tk()
root.title("Labyrinthe Dynamique avec Q-Learning")
canvas = tk.Canvas(root, width=maze_width, height=maze_height)
canvas.pack()

generate_perfect_maze()  # Crée le labyrinthe parfait
draw_maze()  # Dessine le labyrinthe

# Lancer l'application
root.mainloop()