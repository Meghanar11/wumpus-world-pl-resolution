# Wumpus-world-pl-resolution

# Project Overview
The Wumpus World is a grid-based environment used to illustrate intelligent agent behavior in uncertain conditions. The agent must find gold while avoiding pits and the Wumpus (a monster), using percepts and logical inference.
This implementation uses:
- A propositional knowledge base (KB)
-Inference using the Resolution algorithm
- Percepts such as stench and breeze
- Logical rules to derive safe paths

  # Dependencies
Python 3.x
Jupyter Notebook
No additional libraries required (uses built-in Python)
To install Jupyter (if not already installed):
``` bash
pip install notebook
```
# How to Run
- Clone the repository:
  ``` bash
  git clone https://github.com/yourusername/wumpus-world-resolution.git
  cd wumpus-world-resolution
  ```
- Launch Jupyter Notebook:
  ``` bash
  jupyter notebook
  ```
-  Open and run the notebook Wumpus World Puzzle by PL-Resolution Algorithm.ipynb.

# Key Concepts
- Knowledge Representation: Percepts are converted into logical sentences in propositional form.
- Inference by Resolution: The system checks entailment of new facts by trying to derive contradictions.
- Safe Path Identification: Logical deduction is used to identify safe moves in the grid.

# Sample Output
``` bash
Inference: There is a pit at (2,3)
Move: Safe move to (2,2)
Gold found at (3,2)!
```

# Future Improvements
- Add visualization for the Wumpus world grid.
- Support for larger grids and multiple golds.
- Integration with SAT solvers for performance.

