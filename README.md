# A* Maze Solver and Pathfinding Visualizer

## Overview

A Python-based visualization of the A* (A-Star) Search Algorithm used to find the shortest path in a grid-based maze. The project demonstrates fundamental Artificial Intelligence search techniques by visualizing node exploration and optimal path generation using heuristic-based pathfinding.
## Features

* A* Search Algorithm implementation
* Manhattan Distance heuristic
* Animated visualization of node exploration
* Optimal path reconstruction
* Grid-based maze representation
* Interactive GUI built using Tkinter
* Color-coded search process

## Technologies Used

- Python
- Tkinter
- heapq (Priority Queue)
## Algorithm

A* is an informed search algorithm that combines:

* **g(n)** – Actual cost from the start node to the current node
* **h(n)** – Estimated cost from the current node to the goal node

The evaluation function is:

```text
f(n) = g(n) + h(n)
```

The heuristic used in this project is the Manhattan Distance:

```text
h(n) = |x₁ − x₂| + |y₁ − y₂|
```

By combining actual and estimated costs, A* efficiently finds the shortest path while exploring fewer nodes than uninformed search algorithms.

## Visualization Legend

| Color     | Description     |
| --------- | --------------- |
| 🟧 Orange | Start Node      |
| 🟥 Red    | Goal Node       |
| ⬛ Black   | Wall / Obstacle |
| 🟦 Blue   | Explored Nodes  |
| 🟩 Green  | Optimal Path    |
| ⬜ White   | Unvisited Cells |

## Project Highlights

- Implemented A* Search Algorithm from scratch
- Utilized Manhattan Distance heuristic
- Visualized node exploration and path reconstruction
- Demonstrated heuristic-based AI search techniques
- Built an interactive GUI using Tkinter

## Screenshots

### Initial Maze

![Initial Maze](screenshots/start.png)

### Explored Nodes

![Explored Nodes](screenshots/explored.png)

### Final Optimal Path

![Final Path](screenshots/finalpath.png)

## Project Structure

```text
a-star-maze-solver/
│
├── maze_solver.py
├── README.md
└── screenshots/
    ├── start.png
    ├── explored.png
    └── finalpath.png
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/sreenidhithota12-dotcom/a-star-maze-solver.git
cd a-star-maze-solver
```

Run the application:

```bash
python maze_solver.py
```

## Learning Outcomes

This project demonstrates:

* Artificial Intelligence search techniques
* Heuristic-based pathfinding
* Graph traversal concepts
* Priority Queue implementation
* Path reconstruction
* GUI development using Tkinter
* Algorithm visualization and animation

## Future Enhancements

* Random maze generation
* Interactive obstacle placement
* BFS (Breadth-First Search)
* DFS (Depth-First Search)
* Dijkstra's Algorithm
* Search algorithm comparison dashboard
* Performance metrics (execution time, nodes explored, path length)

## Author

### Banda Srijay Ram Reddy

Computer Science Engineering (AI & ML)

* GitHub: https://github.com/srijay-095
* LinkedIn:https://www.linkedin.com/in/srijay-ram-reddy-802580376/
* LeetCode: https://leetcode.com/u/srijay95/
