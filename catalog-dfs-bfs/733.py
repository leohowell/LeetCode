# 733. 图像渲染
# https://leetcode-cn.com/problems/flood-fill/


# 我的解答 (40 ms)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        cache = set()
        origin_color = image[sr][sc]
        blocks = [(sr, sc)]
        while blocks:
            row, col = blocks.pop()
            if (row, col) not in cache:
                cache.add((row, col))
                image[row][col] = newColor
                blocks += self.get_blocks_around_me(image, row, col, origin_color)

        row_len, col_len = len(image), len(image[0])
        for row in range(row_len):
            for col in range(col_len):
                if (row, col) in cache:
                    image[row][col] = newColor
        return image

    @classmethod
    def get_blocks_around_me(cls, image, sr, sc, color):
        row_len, col_len = len(image), len(image[0])
        cand = [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]
        for row, col in cand:
            if 0 <= row < row_len and 0 <= col < col_len:
                if image[row][col] == color:
                    yield row, col


# 我的解答 不使用set缓存(48 ms)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        if origin_color == newColor:
            return image

        blocks = [(sr, sc)]
        while blocks:
            row, col = blocks.pop()
            image[row][col] = newColor
            blocks += self.get_blocks_around_me(image, row, col, origin_color)
        return image

    @classmethod
    def get_blocks_around_me(cls, image, sr, sc, color):
        row_len, col_len = len(image), len(image[0])
        cand = [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]
        for row, col in cand:
            if 0 <= row < row_len and 0 <= col < col_len:
                if image[row][col] == color:
                    yield row, col


# 测试用例
"""
[[0,0,0],[0,1,1]]
1
1
1
[[0,0,0],[1,0,0]]
1
1
2
[[1,1,1],[1,1,0],[1,0,1]]
1
1
2
[[0,0,0],[0,0,0]]
0
0
2
"""
