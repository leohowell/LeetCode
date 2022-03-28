# -*- coding: utf-8 -*-

"""
You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water. Grid cells are connected
horizontally/vertically (not diagonally). The grid is completely surrounded
by water, and there is exactly one island (i.e., one or more connected land
cells). The island doesn't have "lakes" (water inside that isn't connected
to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the
perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_len = len(grid)
        col_len = len(grid[0]) if row_len else 0
        if not row_len or not col_len:
            return 0

        per_sum = 0

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 0:
                    continue
                per_sum += self.get_adjoin(grid, row_len, col_len, row, col)
        return per_sum

    def get_adjoin(self, grid, row_len, col_len, row, col):
        left = grid[row][col - 1] if col - 1 >= 0 else 0
        right = grid[row][col + 1] if col + 1 < col_len else 0
        up = grid[row - 1][col] if row - 1 >= 0 else 0
        down = grid[row + 1][col] if row + 1 < row_len else 0
        return 4 - sum([left, right, up, down])
