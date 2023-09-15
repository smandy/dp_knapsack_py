def knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize a table to store the maximum values for subproblems.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    # Fill the dp table using dynamic programming.
    for i in range(n):
        for w in range(capacity + 1):
            if weights[i] <= w:
                # If the current item can fit in the knapsack, we have two choices:
                # 1. Include the item and add its value to the previous maximum value for the remaining capacity.
                # 2. Exclude the item and keep the maximum value for the same capacity.
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i]] + values[i])
            else:
                # If the current item is too heavy to include, we can't take it, so we keep the maximum value
                # for the same capacity without this item.
                dp[i][w] = dp[i - 1][w]

    # Reconstruct the solution by tracing back through the dp table.
    selected_items = []
    i, j = n - 1, capacity
    while i >= 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            # If the value at dp[i][j] is different from the value above (i.e., item i was included),
            # then include the item in the selected items list and subtract its weight from j.
            selected_items.append(i)
            j -= weights[i]
        i -= 1

    # Return the maximum value and the selected items.
    return dp[n - 1][capacity], selected_items

# Example usage:
weights = [2, 2, 3, 4, 5]
values = [3, 4, 5, 6, 7]
capacity = 10
max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
