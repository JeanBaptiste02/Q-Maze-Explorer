import tkinter as tk

# Dimensions du labyrinthe
maze_size = 10
maze_width = 500
maze_height = 500

# Initialisation de l'interface
root = tk.Tk()
root.title("Labyrinthe Dynamique avec Q-Learning")
canvas = tk.Canvas(root, width=maze_width, height=maze_height)
canvas.pack()

# Lancer l'application
root.mainloop()