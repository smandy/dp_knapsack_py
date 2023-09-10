from pprint import pprint as pp

from collections import defaultdict

def knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize a table to store the maximum values for subproblems.
    dp = defaultdict(int) ## Less dragons

    # Fill the dp table.
    for i in range(n):
        for w in range(capacity + 1):
            if weights[i] <= w:
                dp[(i, w)] = max(dp[ (i - 1, w) ], dp[ (i - 1, w - weights[i])] + values[i])
            else:
                dp[ (i,w)] = dp[ (i - 1, w ) ]

    # Reconstruct the solution.
    selected_items = []
    i, j = n - 1, capacity
    while i >= 0 and j > 0:
        if dp[(i,j)] != dp[ (i - 1,j) ]:
            selected_items.append(i)
            j -= weights[i]
        i -= 1

    pp( [(i, x) for i,x in enumerate(dp) ] )
    # Return the maximum value and the selected items.
    return dp[ (n - 1,capacity) ], selected_items

# Example usage:
weights = [2, 2, 3, 4, 5]
values = [3, 4, 5, 6, 7]
capacity = 10
max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
