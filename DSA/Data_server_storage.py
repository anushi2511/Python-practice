#  Data Server Storage Consolidation Concepts: Greedy Algorithms, Sorting, Knapsack Question: 
# You are given n servers with available capacities and m applications with storage needs. Minimize the number of servers used to deploy all applications. 
# Input: Server capacities and application storage requirements 
# Output: Allocation of applications to servers

def solve(cap, apps):
    apps.sort(reverse = True)

    remaining = cap[:]
    alloc = [[] for _ in range(len(cap))]
    used = 0

    for i in apps:
        placed = False
        for k in range(used):
            if remaining[k] >= i:
                alloc[k].append(i)
                remaining[k] -= i
                placed = True
                break

        if not placed:
            if used == len(cap):
                return -1, []

            alloc[used].append(i)
            remaining[used] -= i
            used += 1

    return used, alloc

print(solve([10,8,6], [5,5,4,3,2]))