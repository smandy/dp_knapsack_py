
max = __builtins__['max']

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):  # Loop through items (1 to n)
        for w in range(capacity + 1):  # Loop through capacities (0 to capacity)
            # If the current item can fit in the knapsack (weight[i-1] <= w),
            # we have two choices: include it or exclude it.
            if weights[i - 1] <= w:
                # If we include the current item, update the maximum value.
                included_value = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                # If we exclude the current item, the maximum value remains the same.
                excluded_value = dp[i - 1][w]

                print("%s %s inc = %s exc = %s" %
                      (i, w, included_value, excluded_value))
                # Choose the maximum of the two values.
                dp[i][w] = max(included_value, excluded_value)
            else:
                print("%s %s Can't fit %s vs %s" % (i, w, weights[i-1], w))

    print()

    # The final value in dp table represents the maximum value achievable
    max_value = dp[n][capacity]

    # Find the items that were selected to achieve the maximum value.
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        print( "%s %s" % (i,w))
        # If the value changed when the current item was included,
        # it means the item was selected. Add its index to the list.
        if dp[i][w] != dp[i - 1][w]:
            print("Adding %s (%s vs %s)" % ((i-1), dp[i][w], dp[i-1][w]))
            selected_items.append(i - 1)
            # Subtract the weight of the selected item from the capacity.
            w -= weights[i - 1]
        # Move to the previous item.
        i -= 1

    print()
    for i, x in enumerate( dp ):
        if i == 0:
            continue
        print("%s %s" % (i,  x[1:]) )
        
    return max_value, selected_items, dp

# Example usage:
values = [60, 100, 120]
weights = [1, 2, 3]
capacity = 5
max_value, selected_items, dp = knapsack(values, weights, capacity)

print("Maximum Value:", max_value)
print("Selected Items:", selected_items)


