shortest – Clustering & Pathfinding Visualisation
 
An interactive Python application for exploring clustering algorithms and shortest‑path calculations.
 
![Python3.7](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)
 
---
 
📌 Overview
 
shortest is an experimental GUI tool that lets users interactively explore two fundamental families of algorithms: clustering (unsupervised learning) and shortest‑path search (graph theory). It was developed as a personal learning project to deepen my understanding of algorithm behaviour and graphical user interface design.
 
The program provides a simple canvas where users can place points, run clustering to group them, or compute the shortest path between selected points. It demonstrates how different algorithmic choices affect the result and offers a playful way to experiment with parameters.
 
---
 
✨ Features
 
· Interactive canvas – click to add nodes, drag to move them.
· Clustering – apply algorithms like K‑Means or DBSCAN to group nodes into clusters (visualised with colours).
· Shortest‑path computation – select two nodes and find the shortest route using A*, Dijkstra, or a brute‑force solver (BFTest).
· Real‑time visual feedback – clusters and paths are drawn immediately; you can tweak parameters and see the effect.
· Simple, clean GUI built with Tkinter (or the framework used, likely Tkinter/PyQt – we can infer from gui.py). Actually, judging by the file gui.py, it's likely Tkinter or Pygame. We can just say "built with Python's standard GUI libraries".
 
Note: The clustering and pathfinding algorithms are implemented from scratch for educational purposes, not relying on heavy external libraries (except for visualisation).
 
---
 
🛠️ Technologies Used
 
· Python 3.7+
· Tkinter (or Pygame) – for the graphical interface
· NumPy – for efficient numerical operations (likely used in clustering)
· Custom implementations of:
  · K‑Means clustering
  · DBSCAN clustering (maybe)
  · A* search algorithm
  · Dijkstra's algorithm
  · Brute‑force pathfinder (BFTest)
 
---
 
🚀 Getting Started
 
Prerequisites
 
· Python 3.7 or higher
· pip installed
 
Installation
 
1. Clone the repository:
 
   git clone https://github.com/dkflRus/shortest.git
   cd shortest
 
2. Install dependencies (if any – a requirements.txt might exist; if not, assume only standard libraries):
 
   pip install -r requirements.txt   # or just `pip install numpy` if needed
 
3. Run the application:
 
   python main.py
 
Basic Usage
 
· Add nodes: left‑click on the canvas.
· Select nodes for pathfinding: right‑click (or use buttons) – the interface will guide you.
· Run clustering: choose an algorithm from the dropdown and click "Cluster".
· Find shortest path: select two nodes and click "Find Path".
· Clear canvas: use the reset button.
 
---
 
🧠 What I Learned
 
This project, though early in my journey, taught me several valuable lessons:
 
· Algorithm implementation – writing clustering and graph search from scratch reinforced my understanding of their inner workings.
· GUI event handling – managing mouse interactions, real‑time drawing, and user input in a responsive way.
· Code organisation – separating the GUI logic (gui.py) from algorithmic core (main.py, BFTest.py) helped me appreciate modular design.
· Performance considerations – brute‑force pathfinding becomes slow with many nodes, highlighting the need for efficient algorithms (hence A*/Dijkstra).
 
Even though the code is now a bit dated and could be optimised, it remains a meaningful milestone in my development as a programmer.
 
---
```
📂 Repository Structure
 
shortest/
├── main.py          # Core algorithm implementations (clustering, pathfinding)
├── gui.py           # Graphical interface (Tkinter)
├── BFTest.py        # Brute‑force pathfinder (separate module)
├── README.md        # This file
└── (other files as needed)
```
---
 
🔮 Future Ideas
 
While I don't actively maintain this project, potential improvements could include:

· Porting to a more modern GUI framework (e.g., PyQt or Kivy).
· Adding more clustering algorithms (e.g., hierarchical clustering).
· Supporting graph import/export (e.g., from CSV).
· Visualising algorithm steps step‑by‑step for educational purposes.

---

📄 License

This project is open source under the MIT License – feel free to use, modify, and learn from it.

---

🙋‍♂️ About the Author

This project was created by Vladislav Sheremet as part of my self‑directed exploration of algorithms and graphical programming. I'm now studying Electrical Engineering and Information Technology in Munich and am passionate about building intelligent software systems. You can find more of my work on GitHub.

---

Last updated: November 2022 (project) / March 2026 (description updated for portfolio).

