from collections import defaultdict

def water_jug_solver(x, y):
    if (x, y) in visited:
        return False
    print(f"({x}, {y})")
    visited[(x, y)] = True
    if x == aim or y == aim:
        return True

    return (
        water_jug_solver(0, y) or  # Empty Jug1
        water_jug_solver(x, 0) or  # Empty Jug2
        water_jug_solver(jug1, y) or  # Fill Jug1
        water_jug_solver(x, jug2) or  # Fill Jug2
        water_jug_solver(x + min(y, jug1 - x), y - min(y, jug1 - x)) or  # Pour Jug2 → Jug1
        water_jug_solver(x - min(x, jug2 - y), y + min(x, jug2 - y))    # Pour Jug1 → Jug2
    )

jug1 = int(input("Enter capacity of jug1: "))
jug2 = int(input("Enter capacity of jug2: "))
aim = int(input("Enter the desired amount: "))
visited = defaultdict(bool)

print("\nSteps:")
if not water_jug_solver(0, 0):
    print("No solution found.")
