#!/usr/bin/env python
# coding: utf-8

# ### Representing the Wumpus World in Propositional Logic

# In[2]:


# Step 1: Define the Propositional Variables
# Each cell in the grid is represented by its coordinates (x, y).
# Propositions:
# - W(x, y): Wumpus in cell (x, y)
# - P(x, y): Pit in cell (x, y)
# - B(x, y): Breeze in cell (x, y)
# - S(x, y): Stench in cell (x, y)
# - G(x, y): Gold in cell (x, y)
# - OK(x, y): Safe cell at (x, y)

# Define a grid size
GRID_SIZE = 4  # 4x4 grid for the Wumpus World

# Initialize the knowledge base (KB) as a list of clauses
knowledge_base = []

# Function to encode logical rules
def add_clause(clause):
    """Add a clause to the knowledge base."""
    knowledge_base.append(clause)

# Logical rules for the Wumpus World
# 1. If there is a breeze in a cell, there is at least one pit in the neighboring cells.
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        neighbors = [
            (x + dx, y + dy)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE
        ]
        clause = f"B({x},{y}) => " + " OR ".join([f"P({nx},{ny})" for nx, ny in neighbors])
        add_clause(clause)

# 2. If there is a stench in a cell, there is at least one Wumpus in the neighboring cells.
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        neighbors = [
            (x + dx, y + dy)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE
        ]
        clause = f"S({x},{y}) => " + " OR ".join([f"W({nx},{ny})" for nx, ny in neighbors])
        add_clause(clause)

# Print initial knowledge base
print("Initial Knowledge Base:")
for clause in knowledge_base:
    print(clause)


# ### Implement the PL-Resolution Algorithm

# In[4]:


# Step 2: Implement the PL-Resolution Algorithm
def pl_resolution(kb, query):
    """
    Implements the Propositional Logic Resolution algorithm.
    Args:
        kb: List of clauses (knowledge base).
        query: Clause to resolve.
    Returns:
        True if the query is entailed by the knowledge base; False otherwise.
    """
    from itertools import combinations

    # Negate the query and add to the KB
    negated_query = f"NOT({query})"
    clauses = kb + [negated_query]

    # Function to resolve two clauses
    def resolve(ci, cj):
        resolved = set()
        for di in ci:
            for dj in cj:
                if di == f"NOT({dj})" or f"NOT({di})" == dj:
                    new_clause = (ci - {di}) | (cj - {dj})
                    resolved.add(frozenset(new_clause))
        return resolved

    # Perform resolution
    new = set()
    while True:
        pairs = combinations(clauses, 2)
        for ci, cj in pairs:
            resolvents = resolve(ci, cj)
            if frozenset() in resolvents:  # Empty clause found
                return True
            new = new.union(resolvents)
        if new.issubset(clauses):  # No new clauses
            return False
        clauses = clauses.union(new)

# Test PL-Resolution
print("\nPL-Resolution Test:")
result = pl_resolution(knowledge_base, "P(1,2)")
print("Query 'P(1,2)' is", "entailed" if result else "not entailed")


# ### Building the Knowledge Base Dynamically

# In[6]:


# Step 3: Update KB Based on Percepts
def update_kb_with_percept(kb, percept, x, y):
    """
    Updates the KB with the agent's percepts.
    Args:
        kb: Knowledge base.
        percept: Percept type (e.g., "Breeze", "Stench").
        x, y: Cell coordinates.
    """
    if percept == "Breeze":
        kb.append(f"B({x},{y})")
    elif percept == "Stench":
        kb.append(f"S({x},{y})")
    print(f"Percept '{percept}' added to KB for cell ({x}, {y}).")

# Simulate receiving a percept
update_kb_with_percept(knowledge_base, "Stench", 1, 1)


# ### Agent Decision-Making

# In[8]:


# Step 4: Agent Decision-Making
def agent_decision(kb, x, y):
    """
    Makes a decision for the agent based on logical inference.
    Args:
        kb: Knowledge base.
        x, y: Current cell of the agent.
    Returns:
        Action (move, shoot, grab, or no-op).
    """
    if pl_resolution(kb, f"P({x},{y})"):
        return "Avoid"  # Don't move to a dangerous cell
    elif pl_resolution(kb, f"G({x},{y})"):
        return "Grab"  # Grab gold
    elif pl_resolution(kb, f"W({x},{y})"):
        return "Shoot"  # Shoot Wumpus
    else:
        return "Move"  # Safe to move

# Test agent decision
decision = agent_decision(knowledge_base, 1, 2)
print(f"Agent decision for cell (1,2): {decision}")


# ### Simulation and User Interaction

# In[10]:


import tkinter as tk

# Step 5: Interactive GUI Simulation of Wumpus World

# Define grid size and initialize the world
GRID_SIZE = 4
world = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Possible cell states
CELL_STATES = ["Empty", "Wumpus", "Pit", "Gold"]

def create_gui():
    def update_cell(x, y):
        """
        Update the cell with a new state based on the current selection.
        """
        current_state = world[x][y]
        # Find the next state in the CELL_STATES cycle
        next_state = CELL_STATES[(CELL_STATES.index(current_state) + 1) % len(CELL_STATES)]
        world[x][y] = next_state
        buttons[x][y].config(text=f"{next_state}")
        print(f"Updated cell ({x},{y}) to '{next_state}'")

    def reset_world():
        """
        Reset the grid to the default empty state.
        """
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                world[i][j] = "Empty"
                buttons[i][j].config(text="Empty")
        print("World reset to empty state.")

    # Initialize Tkinter root
    root = tk.Tk()
    root.title("Interactive Wumpus World Simulation")

    # Create buttons for the grid
    buttons = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            # Initialize each cell as "Empty"
            world[x][y] = "Empty"
            btn = tk.Button(
                root, text="Empty", width=10, height=4,
                command=lambda x=x, y=y: update_cell(x, y)
            )
            btn.grid(row=x, column=y)
            buttons[x][y] = btn

    # Add reset button
    reset_button = tk.Button(root, text="Reset World", command=reset_world)
    reset_button.grid(row=GRID_SIZE, column=0, columnspan=GRID_SIZE // 2)

    # Add simulate button
    def simulate_agent():
        """
        Simulate the agent's behavior based on the current world configuration.
        """
        print("Simulating agent in the Wumpus World...")
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                print(f"Cell ({row},{col}): {world[row][col]}")
        print("Simulation complete. (You can replace this with the actual agent logic!)")

    simulate_button = tk.Button(root, text="Simulate Agent", command=simulate_agent)
    simulate_button.grid(row=GRID_SIZE, column=GRID_SIZE // 2, columnspan=GRID_SIZE // 2)

    # Start the main Tkinter loop
    root.mainloop()

# Run the GUI
create_gui()


# ### Evaluation and Testing

# In[21]:


# Step 6: Evaluation - Evaluate Agent's Success
def evaluate_agent(kb, world):
    """
    Evaluates the agent's success in solving the Wumpus World.
    Args:
        kb: Knowledge base.
        world: The grid representing the Wumpus World with its hazards.
    Returns:
        Success rate and the number of actions taken.
    """
    total_actions = 0
    successful_actions = 0
    
    # Iterate through each cell of the world and simulate the agent's decisions.
    for x in range(len(world)):
        for y in range(len(world[x])):
            total_actions += 1
            action = agent_decision(kb, x, y)
            
            # Check if the agent successfully grabs the gold
            if action == "Grab" and world[x][y] == "Gold":
                successful_actions += 1
            # Check if the agent avoids hazardous cells (Wumpus, Pit)
            elif action == "Avoid" and (world[x][y] == "Wumpus" or world[x][y] == "Pit"):
                successful_actions += 1
            # Check if the agent shoots the Wumpus when it's in the correct position
            elif action == "Shoot" and world[x][y] == "Wumpus":
                successful_actions += 1
            # Check if the agent moves to a safe cell
            elif action == "Move" and world[x][y] == "Empty":
                successful_actions += 1

    # Calculate the success rate based on successful actions
    success_rate = successful_actions / total_actions if total_actions > 0 else 0
    print(f"Agent success rate: {success_rate * 100:.2f}%")
    return success_rate


# Example world configuration: Representing a 4x4 grid.
# "Empty", "Wumpus", "Pit", "Gold"
world = [
    ["Empty", "Empty", "Pit", "Empty"],
    ["Wumpus", "Empty", "Empty", "Gold"],
    ["Empty", "Pit", "Empty", "Empty"],
    ["Empty", "Empty", "Empty", "Empty"]
]

# Run evaluation on the knowledge base and the world
evaluate_agent(knowledge_base, world)


# In[ ]:




