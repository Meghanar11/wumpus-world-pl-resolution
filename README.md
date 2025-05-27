#  Wumpus World Solver using PL-Resolution

This project demonstrates an AI agent solving the **Wumpus World** using **Propositional Logic (PL)** and the **Resolution Algorithm**. It includes a logic-based knowledge base, inference engine, agent decision logic, and an interactive GUI.

## Files Included

- `wumpus_pl_solver.py`  
  → Main Python script with full implementation including GUI, logic rules, agent decision-making, and evaluation.

- `Wumpus World Puzzle by PL-Resolution Algorithm.ipynb`  
  → Jupyter Notebook that explains the logical reasoning, clause construction, and resolution algorithm step-by-step. Ideal for learning and presentation.

## How to Run

### Requirements
- Python 3.x
- No external libraries required (uses `tkinter`, built-in in most Python distributions)

### To Run the GUI (Recommended)
```bash
python wumpus_pl_solver.py
```

- Click on grid cells to cycle between states: Empty, Wumpus, Pit, Gold
- Use Reset World to clear
- Use Simulate Agent to trigger decision logic and simulate inference-based moves

## Key Concepts
- Knowledge Representation: Propositions like P(x,y) for Pit, B(x,y) for Breeze, etc.
- PL-Resolution: Logical inference engine tests if a query (e.g., “Is (2,1) a Pit?”) is entailed by known facts
- Agent Logic: Uses inference results to avoid hazards, grab gold, and make safe moves

## Sample World Configuration
``` bash
world = [
    ["Empty", "Empty", "Pit", "Empty"],
    ["Wumpus", "Empty", "Empty", "Gold"],
    ["Empty", "Pit", "Empty", "Empty"],
    ["Empty", "Empty", "Empty", "Empty"]
]
```
Agent success rate is calculated based on logical decisions and outcomes.

## Future Improvements
- More advanced agent movement logic
- SAT-based reasoning for larger grids
- Pathfinding algorithms with cost optimization
- Enhanced visualization and animation




