from itertools import product

# Input graph
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['B'],
    'D': ['A', 'B', 'E'],
    'E': ['B', 'D']
}

colors = ['Red', 'Green', 'Blue']

# Tree decomposition (manually defined for this graph)
tree = {
    'Bag1': {'nodes': ['A', 'B', 'D'], 'neighbors': ['Bag3', 'Bag2']},
    'Bag2': {'nodes': ['B', 'C'], 'neighbors': ['Bag1']},
    'Bag3': {'nodes': ['B', 'D', 'E'], 'neighbors': ['Bag1']}
}

# Store DP solutions
dp = {}

# Utility: check if coloring is valid in a bag
def is_valid_coloring(bag_nodes, coloring):
    for i in range(len(bag_nodes)):
        for j in range(i + 1, len(bag_nodes)):
            a, b = bag_nodes[i], bag_nodes[j]
            if b in graph[a] and coloring[a] == coloring[b]:
                return False
    return True

# Convert tuple to dict for coloring
def tuple_to_dict(bag_nodes, color_tuple):
    return {node: color for node, color in zip(bag_nodes, color_tuple)}

# Run DP on tree decomposition
def process_bag(bag_name, parent=None):
    nodes = tree[bag_name]['nodes']
    dp[bag_name] = []
    
    for coloring in product(colors, repeat=len(nodes)):
        color_map = tuple_to_dict(nodes, coloring)
        if is_valid_coloring(nodes, color_map):
            dp[bag_name].append(color_map)

    # Recursively process children
    for neighbor in tree[bag_name]['neighbors']:
        if neighbor != parent:
            process_bag(neighbor, bag_name)

# Start from Bag1
process_bag('Bag1')

# Print all valid colorings in Bag1
print("Valid colorings for Bag1:")
for c in dp['Bag1']:
    print(c)
