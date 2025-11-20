# 🧩 Rubik's Cube AI Solver (DFS, BFS, A*)

An algorithmic research project exploring classical Artificial Intelligence search strategies to solve simplified **2x2x2** and **3x3x3** Rubik's Cube puzzles.

## 📖 Project Overview
This project implements three fundamental search algorithms from scratch in Python without external solver libraries. The goal was to evaluate their performance trade-offs in a combinatorial optimization problem, measuring execution time, path optimality, and computational limits.

📄 **[Read the Full Research Paper](./ML%20Assignment%201%20-%20Josue%20Pavon%201.pdf)**

---

## 📊 Key Findings & Methodology

* **Algorithms Implemented:**
    * [cite_start]**DFS (Depth-First Search):** Fast for trivial scrambles but produces suboptimal (longer) solution paths [cite: 263-266].
    * **BFS (Breadth-First Search):** Guarantees the shortest path (optimal) but is memory-intensive. [cite_start]Successfully solved 3x3x3 constraints [cite: 274-275].
    * **A* (A-Star):** The most efficient for 2x2x2, utilizing a custom heuristic (misplaced stickers). [cite_start]It solved a 2-move scramble in **0.02s** compared to BFS's **1.41s** [cite: 269-270].

* **Performance Limits:**
    * [cite_start]The project demonstrated the limits of naive heuristics; while A* excelled at shallow depths, it encountered timeouts on complex 4-move scrambles, highlighting the need for advanced pattern databases [cite: 271-273].

---

## 🛠️ Technical Stack

* **Language:** Python 3.10+
* **Data Structures:** `collections.deque`, `heapq` (Priority Queues)
* **Concepts:** State Space Search, Heuristics, Pathfinding, Algorithm Complexity

---

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jpavon-jp/Rubiks-Cube-AI-Solver.git](https://github.com/jpavon-jp/Rubiks-Cube-AI-Solver.git)
    ```
2.  **Run the solver script:**
    ```bash
    python "Assignment 1 Josue Pavon ML.py"
    ```

---

## ⚠️ Context
Developed for the **AI Research Group** at the University of Europe for Applied Sciences.
**Author:** Josue David Pavon Maldonado
