
max = __builtins__['max']
import collections

from pprint import pprint as pp

def knapsack(values, weights, capacity):
    #n = len(values)
    #p = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    dp = collections.defaultdict(int)
    
    for i, (weight, value) in enumerate(zip(weights, values)):  # Loop through items (1 to n)
        #i = tmp + 1
        for w in range(1, capacity + 1):  # Loop through capacities (0 to capacity)
            # If the current item can fit in the knapsack (weight[i-1] <= w),
            # we have two choices: include it or exclude it.
            excluded_value = dp[ (i - 1, w) ]
            if weight <= w:
                # If we include the current item, update the maximum value.
                included_value = dp[(i-1, w - weight)] + value
                print("Included %s %s %s+%s = %s exc=%s" % (i,w, dp[(i, w - weight)], value, included_value, excluded_value) )

                #if included_value > excluded_value:
                #    print("Including!")
                
                # If we exclude the current item, the maximum value remains the same.
                #print("%s %s inc = %s exc = %s" %
                 #     (i, w, included_value, excluded_value))
                # Choose the maximum of the two values.

                dp[(i,w)] = max(included_value, excluded_value)
            else:
                dp[(i,w)] = excluded_value
                print("%s %s Can't fit %s" % (i, w, weight) )

    print()

    for tmp, (weight, value) in enumerate( zip(weights, values) ):
        print( "%3s : " % tmp, end = '')
        for w in range(1, capacity + 1):
            print("%4d" % dp[tmp, w] , end = '')
        print()
            
    # The final value in dp table represents the maximum value achievable

    print("i=%s capacity=%s" % (i, capacity))
    max_value = dp[ (i,capacity)] 

    # Find the items that were selected to achieve the maximum value.
    selected_items = []
    i, w = len(weights)-1, capacity
    while i >= 0 and w > 0:
        #print( "%s %s" % (i,w))
        # If the value changed when the current item was included,
        # it means the item was selected. Add its index to the list.
        if dp[(i,w)] != dp[(i - 1, w)]:
            print("Adding %s %s value = %s (%s vs %s)" % (i, w, weights[i], dp[(i,w)], dp[(i-1,w)]))
            selected_items.append(weights[i])
            # Subtract the weight of the selected item from the capacity.
            w -= weights[i]
        # Move to the previous item.
        i -= 1

    print()
    pp(dp)
        
    return max_value, selected_items, dp

# Example usage:

if 1:
    values = [60, 100, 120]
    weights = [1, 2, 3]
    capacity = 5

elif 0:
    values = [1,2,3,4,5]
    weights = [1,1,1,1,1]
    capacity = 3
elif 1:
    values = [3,2,3,4,5]
    weights = [1,1,1,1,7]
    capacity = 10
    
    
max_value, selected_items, dp = knapsack(values, weights, capacity)

print("Maximum Value:", max_value)
print("Selected Items:", selected_items)


