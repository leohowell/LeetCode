from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        max_x = len(matrix[0])
        max_y = len(matrix)
        size = max_x * max_y
        cnt = 0

        output = []
        x, y = -1, 0

        cached = set()
        directions = ("x+", "y+", "x-", "y-")
        current = 0
        while cnt < size:
            current %= 4
            direction = directions[current]
            if direction == "x+":
                if (y, x + 1) in cached or x + 1 >= max_x:
                    current += 1
                    continue
                x += 1
            elif direction == "y+":
                if (y + 1, x) in cached or y + 1 >= max_y:
                    current += 1
                    continue
                y += 1
            elif direction == "x-":
                if (y, x - 1) in cached or x - 1 < 0:
                    current += 1
                    continue
                x -= 1
            else:
                if (y - 1, x) in cached or y - 1 < 0:
                    current += 1
                    continue
                y -= 1

            cached.add((y, x))
            output.append(matrix[y][x])
            cnt += 1

        return output


if __name__ == "__main__":
    s = Solution()
    result = s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)

    s = Solution()
    result = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(result)
