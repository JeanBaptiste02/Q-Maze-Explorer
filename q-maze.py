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
maze = np.zeros((maze_size, maze_size))  # 0 = libre, 1 = obstacle
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

# Fonction pour choisir l'action selon l'epsilon-greedy
def choose_action(x, y):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, num_actions - 1)  # Exploration (action aléatoire)
    else:
        return np.argmax(Q_table[x, y])  # Exploitation (meilleure action apprise)

# Fonction pour obtenir la récompense (1 pour gagner, -1 pour perdre, 0 pour continuer)
def get_reward(x, y):
    if (x, y) == (maze_size - 1, maze_size - 1):  # Arrivé à la sortie
        return 1
    elif maze[x, y] == 1:  # Si on tombe sur un obstacle
        return -1
    return 0  # Si on est encore en jeu

# Fonction pour mettre à jour la Q-table
def update_Q_table(x, y, action, reward, next_x, next_y):
    max_q_next = np.max(Q_table[next_x, next_y])  # La meilleure récompense future
    Q_table[x, y, action] += alpha * (reward + gamma * max_q_next - Q_table[x, y, action])

# Mise à jour de la position de l'agent
def move_agent(action):
    global agent_pos
    x, y = agent_pos
    if action == 0:  # Haut
        if x > 0 and maze[x - 1, y] != 1:
            agent_pos = (x - 1, y)
    elif action == 1:  # Droite
        if y < maze_size - 1 and maze[x, y + 1] != 1:
            agent_pos = (x, y + 1)
    elif action == 2:  # Bas
        if x < maze_size - 1 and maze[x + 1, y] != 1:
            agent_pos = (x + 1, y)
    elif action == 3:  # Gauche
        if y > 0 and maze[x, y - 1] != 1:
            agent_pos = (x, y - 1)

# Fonction de visualisation
def draw_maze():
    canvas.delete('all')
    cell_width = maze_width // maze_size
    cell_height = maze_height // maze_size
    
    # Dessiner les murs et la sortie
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

# Fonction de mise à jour du jeu
def update_game():
    global agent_pos
    x, y = agent_pos
    action = choose_action(x, y)
    move_agent(action)
    reward = get_reward(agent_pos[0], agent_pos[1])
    next_x, next_y = agent_pos
    update_Q_table(x, y, action, reward, next_x, next_y)

    draw_maze()

    # Affichage des récompenses
    reward_label.config(text=f"Récompense : {reward}")

    # Continuer tant que le jeu n'est pas fini
    if reward != 1:
        root.after(100, update_game)  # Met à jour toutes les 100ms
    else:
        result_label.config(text="Gagné !")

# Initialisation de l'interface
root = tk.Tk()
root.title("Labyrinthe Dynamique avec Q-Learning")
canvas = tk.Canvas(root, width=maze_width, height=maze_height)
canvas.pack()

# Labels pour afficher les résultats
reward_label = tk.Label(root, text="Récompense : 0", font=("Arial", 14))
reward_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Initialisation du jeu
generate_perfect_maze()  # Crée le labyrinthe parfait
draw_maze()  # Dessine le labyrinthe
update_game()  # Lance l'update du jeu

# Lancer l'application
root.mainloop()