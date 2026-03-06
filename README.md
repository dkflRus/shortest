shortest – Clustering & Pathfinding Visualisation

An interactive educational tool for exploring clustering algorithms and shortest‑path search – my first real programming project, created at age 14 during a summer camp at the HSE University (Moscow), where it became a laureate of the project competition.


![Python3.7](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

📌 Overview

shortest is a simple GUI application that lets users interactively explore two fundamental families of algorithms:

- Clustering (unsupervised learning) – K‑means and DBSCAN.
- Shortest‑path search – Dijkstra and A*.

I wrote the first version of this program in 2022, when I was 14 years old, during a summer programming camp organised by the HSE University (Moscow). That same year, the project was recognised as a Laureate in the camp's project competition. It was my first real attempt to build something that combined algorithmic thinking with a graphical interface – and it sparked my lasting interest in software development and AI.

The original code was a bit messy (as you might expect from a teenager's first project), so I have recently rewritten it completely while preserving the original idea and algorithms. The current version is clean, well‑structured, and thoroughly documented – making it suitable for inclusion in my portfolio.

---

✨ Features

- Add points by clicking on the canvas.
- K‑means clustering – specify the number of clusters (K) and watch the algorithm group points in real time.
- DBSCAN clustering – set the neighbourhood radius (eps) and minimum samples to see density‑based clusters (noise points are shown separately).
- Shortest‑path search – select two points (Shift+click) and run Dijkstra or A* to find the optimal route. The graph is fully connected with Euclidean distances as edge weights.
- Interactive visualisation – clusters are shown in distinct colours; paths are drawn as red lines.
- Reset and random points – clear the canvas or generate 10 random points for quick experiments.

---

🛠️ Technologies Used

- Python 3.7+ – all algorithms are implemented from scratch, without external ML libraries.
- Tkinter – for the graphical user interface (standard library, no extra dependencies).
- Math / Random – for distance calculations and random initialisation.

---

🧠 What I Learned

Even though this project is simple, it taught me several valuable lessons that I still carry with me:

- Translating mathematical concepts into code – implementing K‑means and DBSCAN from scratch gave me a deep understanding of how these algorithms really work.
- GUI event handling – managing mouse clicks, drawing shapes, and updating the canvas in real time.
- Code organisation – even in the original messy version, I tried to separate the algorithmic logic from the interface; the new version takes this much further.
- Debugging and testing – visualising algorithms helps spot mistakes immediately (e.g., wrong clustering assignment, incorrect path calculation).

Most importantly, shortest showed me that programming can be fun and creative – and it encouraged me to keep learning, eventually leading to more complex projects like REA and CarML.

---

🔗 Connection to My Later Work

The modular thinking behind shortest (separate components for clustering and pathfinding) directly influenced the design of REA, where Apps, Extensions, and Renders can be composed arbitrarily. Moreover, the idea of visualising algorithmic output paved the way for the interactive dashboard in CarML.

---
```
📂 Repository Structure

shortest/
├── shortest.py       # The entire application (clean, rewritten version)
├── README.md         # This file
└── (original legacy code is kept in a separate branch for history)
```
---

🚀 Getting Started

1. Clone the repository:
  
   git clone https://github.com/dkflRus/shortest.git
   cd shortest
   
2. Run the application:
  
   python shortest.py
   
   (No external libraries are needed – only Python's standard library.)

---

📄 License

This project is open source under the MIT License – feel free to use, modify, and learn from it.

---

🙋‍♂️ About the Author

shortest holds a special place in my heart – it was my first real programming project, written when I was 14 years old at a summer camp organised by HSE University (Moscow), and it was honoured as a Laureate in the camp's project competition. Although I've since learned much more about software architecture and algorithm design, this little program reminds me where my passion began.

Today, I am an Electrical Engineering and Information Technology student in Munich, working on advanced projects in Rust and Python. But I'm still grateful for that summer camp experience that set me on this path.
