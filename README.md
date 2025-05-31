#  Wumpus World Solver using PL-Resolution
This project implements an intelligent agent that navigates the classic Wumpus World environment. The agent uses percept-based reasoning and logical inference to find the gold, avoid pits and the Wumpus, and exit the cave safely.

## Project Overview

Wumpus World is a grid-based environment where the agent must:
- Explore safely based on limited percepts (`stench`, `breeze`, `glitter`)
- Infer safe and unsafe cells using propositional logic
- Plan actions (move, shoot, grab, climb) to achieve its goal

## Features

- Logic-based inference engine using SAT (e.g., PycoSAT)
- Percept handling and knowledge base updates
- Agent decision-making with safe cell detection
- Optional visualization of the environment and agent moves

## Files

- `wumpus_agent.py` – Core logic for the agent’s reasoning
- `world_generator.py` – Random or predefined Wumpus World maps
- `visualizer.py` – (Optional) Plotting/animation of the agent’s path
- `main.py` – Entry point to simulate agent behavior

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-wumpus-world.git
   cd ai-wumpus-world
   ```

2. Install dependencies:
   ``` bash
   pip install -r requirements.txt
   ```

3. Run the simulation:
   ``` bash
   python main.py
  ```


