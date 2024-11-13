# def tilingRectangle(n: int, m: int) -> int:
#     from functools import lru_cache

#     max_size = max(n, m)
#     import sys
#     sys.setrecursionlimit(1000000)

#     @lru_cache(None)
#     def dfs(grid):
#         if all(row == (1 << m) - 1 for row in grid):
#             return 0
#         res = float('inf')
#         # Find the first empty cell
#         for i in range(n):
#             if grid[i] != (1 << m) - 1:
#                 break
#         # Find the first empty cell in this row
#         pos = 0
#         while grid[i] & (1 << pos):
#             pos += 1
#         # Try all possible square sizes
#         max_k = min(n - i, m - pos)
#         for k in range(max_k, 0, -1):
#             can_place = True
#             for x in range(i, i + k):
#                 if grid[x] & (((1 << k) - 1) << pos):
#                     can_place = False
#                     break
#             if not can_place:
#                 continue
#             # Place the square
#             new_grid = list(grid)
#             for x in range(i, i + k):
#                 new_grid[x] |= ((1 << k) - 1) << pos
#             new_grid = tuple(new_grid)
#             res = min(res, 1 + dfs(new_grid))
#         return res

#     grid = tuple(0 for _ in range(n))
#     return dfs(grid)

# # Example usage:
# n = int(input("Enter n: "))
# m = int(input("Enter m: "))
# print("Minimum number of squares:", tilingRectangle(n, m))
class Solution:
    def __init__(self):
        self.memo = {}
    
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            n, m = m, n
        return self.dfs(n, m, [0] * n, 0)

    def dfs(self, n: int, m: int, heights: list, count: int) -> int:
        # If all columns are filled up to height m, update result
        if all(height == m for height in heights):
            return count

        # Convert heights to a tuple for memoization
        key = tuple(heights)
        if key in self.memo and self.memo[key] <= count:
            return float('inf')
        
        self.memo[key] = count

        # Find the lowest column to start tiling
        min_height = min(heights)
        pos = heights.index(min_height)

        min_squares = float('inf')
        # Try placing squares of different possible sizes from this position
        for side_length in range(1, min(n - pos, m - min_height) + 1):
            new_heights = heights[:]
            # Place a square of size side_length x side_length
            for i in range(pos, pos + side_length):
                new_heights[i] += side_length
            min_squares = min(min_squares, self.dfs(n, m, new_heights, count + 1))

        return min_squares

# Example usage:
# solution = Solution()
# print(solution.tilingRectangle(2, 3))  # Output: 3
# print(solution.tilingRectangle(5, 8))  # Output: 5
# print(solution.tilingRectangle(11, 13))  # Output: 6

# Example usage:
solution = Solution()
print(solution.tilingRectangle(2, 3))    # Output: 3
print(solution.tilingRectangle(5, 8))    # Output: 5
print(solution.tilingRectangle(11, 13))  # Output: 6
