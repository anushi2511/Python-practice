# Smart City Traffic Toll System
# Background
# In a smart city, there are an infinite number of traffic control hubs numbered with positive integers starting from 1. Each hub is connected by smart roads in a unique tree-like structure:
# There is a bidirectional road between hub i and 2i.
# Another direct road exists between hub i and 2i + 1.

# Given this structure, there is always a unique shortest path between any two traffic control hubs. Initially, passing through any road is toll-free. However, to optimize traffic flow and manage congestion, the city traffic authority occasionally imposes toll fees on certain roads along specific paths.

# The traffic authority will introduce a series of changes:

# Toll Fee Update: An update described by integers x, y, and t imposes a toll of t units on all roads along the shortest path from hub y to hub x.
# Travel Cost Calculation: A commuter travels from hub x to hub y using the shortest path, and you need to calculate the total toll fees they incur.
# Input
# The first line contains an integer q (1 ≤ q ≤ 10^5), representing the number of events.
# The next q lines contain details of the events.
# 1 x y t describes a toll update where all roads on the shortest path between hubs x and y increase their toll by t units.
# 2 x y 0 represents a travel event where a commuter moves from hub x to hub y.

# The events are given in the form of a 2D integer array with q rows and 4 columns.

# Output
# For each travel event (2 x y 0), add its total toll cost to a running sum. Return the final sum.
# Function Description
# Complete the solve function in the editor below.

# Parameters
# q (INTEGER) – Number of events.
# a (INTEGER 2D ARRAY) – Details of all events.

# Returns

# INTEGER – Sum of toll costs for all travel events.

def solve(events):
    cost = {}
    total = 0

    for typ, x, y, t in events:
        if typ == 1:
            while x != y:
                if x > y:
                    cost[x] = cost.get(x, 0) + t
                    x = x // 2
                else:
                    cost[y] = cost.get(y, 0) + t
                    y = y // 2

        else:
            curr = 0
            while x != y:
                if x > y:
                    curr += cost.get(x, 0)
                    x = x // 2
                else:
                    curr += cost.get(y, 0)
                    y = y // 2

            total += curr

    return total

events = [[1,13,14,5], [2,13,14,0]]
print(solve(events))


