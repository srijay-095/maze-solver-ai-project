import tkinter as tk
from heapq import heappush, heappop

CELL_SIZE = 70

maze = [
 [0,0,0,0,0,0],
 [1,1,0,1,1,0],
 [0,0,0,0,1,0],
 [0,1,1,0,0,0],
 [0,0,0,1,1,0],
 [0,1,0,0,0,0]
]

start = (0, 0)
end = (5, 5)

ROWS = len(maze)
COLS = len(maze[0])

# Heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* with visited tracking
def astar():
    open_set = []
    heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}
    visited_order = []

    while open_set:
        _, current = heappop(open_set)

        if current not in visited_order:
            visited_order.append(current)

        if current == end:
            path = []
            while current:
                path.append(current)
                current = came_from.get(current)
            return path[::-1], visited_order

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if 0 <= nx < ROWS and 0 <= ny < COLS and maze[nx][ny] == 0:
                temp_g = g_score[current] + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, end)
                    heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current

    return [], visited_order


# Animation function
def draw_maze(step_v=0, step_p=0):
    canvas.delete("all")

    for i in range(ROWS):
        for j in range(COLS):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            color = "white"

            if maze[i][j] == 1:
                color = "black"
            elif (i, j) == start:
                color = "orange"
            elif (i, j) == end:
                color = "red"

            # 🔵 explored nodes
            if (i, j) in visited[:step_v]:
                color = "#4da6ff"

            # 🟢 final path (overrides blue)
            if (i, j) in path[:step_p]:
                color = "green"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    # Phase 1: exploration
    if step_v < len(visited):
        root.after(80, lambda: draw_maze(step_v + 1, step_p))

    # Phase 2: path
    elif step_p < len(path):
        root.after(200, lambda: draw_maze(step_v, step_p + 1))


# Create window
root = tk.Tk()
root.title("A* Maze Solver")

canvas = tk.Canvas(
    root,
    width=COLS * CELL_SIZE,
    height=ROWS * CELL_SIZE
)
canvas.pack()

# Run algorithm
path, visited = astar()

# Start animation
draw_maze(0, 0)

root.mainloop()
