print("krishna,192211408")
from collections import deque
initial_state = (3, 3, 1) 
goal_state = (0, 0, 0)
def generate_moves(state):
    moves = []
    ml, cl, boat = state
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:
                if (ml - m >= 0 and cl - c >= 0) or (ml + m <= 3 and cl + c <= 3):
                    new_state = (ml - m, cl - c, 1 - boat)
                    if (0 <= new_state[0] <= 3) and (0 <= new_state[1] <= 3):
                        moves.append(new_state)
    return moves
def is_valid(state):
    ml, cl, _ = state
    if (ml == 0 or ml >= cl) and (3 - ml == 0 or 3 - ml >= 3 - cl):
        return True
    return False
def solve_missionaries_and_cannibals(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        if current_state not in visited and is_valid(current_state):
            visited.add(current_state)
            for move in generate_moves(current_state):
                queue.append((move, path + [move]))
    return None
solution = solve_missionaries_and_cannibals(initial_state, goal_state)
if solution:
    print("Solution path:")
    for step, state in enumerate(solution):
        print(f"Step {step + 1}: Missionaries={state[0]}, Cannibals={state[1]}, Boat={state[2]}")
else:
    print("No solution found.")

		
