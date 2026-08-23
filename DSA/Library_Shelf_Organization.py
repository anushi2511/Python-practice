# Library Shelf Organization
# You are a librarian tasked with organizing n books that are currently placed on a long shelf. However, the books are scattered, and some of them are out of order. Your goal is to rearrange the books so they occupy consecutive spots on the shelf, minimizing the effort needed for future access.
# Find the minimum number of moves required to rearrange the books into consecutive spots on the shelf. In one move, you can move one book to any arbitrary position.

# Function Description
# Complete the solve function in the editor below.
# Function Parameters:
# n (INTEGER) – Number of books.
# a (INTEGER ARRAY) – Current positions of the books on the shelf. The positions are unique and represent specific spots.

# Return:

# An INTEGER denoting the minimum number of moves required to rearrange the books into consecutive spots on the shelf.
# Constraints
# 1 ≤ n ≤ 10^5
# 1 ≤ a[i] ≤ 10^9
# Input Format for Debugging
# The first line contains an integer n, denoting the number of elements in a.
# Each of the next n lines contains an integer a[i], representing the current position of a book

def solve(n, a):
    a.sort()
    max_books = 0

    left = 0
    for right in range(n):
        while a[right] - a[left] > n:
            left += 1

        max_books = max(max_books, right - left + 1)

    return n - max_books

a = [1,2,4,7,8]
print(solve(5, a))
