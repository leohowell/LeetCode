# 2034. 股票价格波动
# https://leetcode-cn.com/problems/stock-price-fluctuation/

class StockPrice:

    def __init__(self):
        self.values = []
        self.price_order = []

        self.max_list = 0  # 右边边为最大值
        self.min_list = 0  # 右边为最小值
        self.max_ts = 0

    def bfs(self, ts):
        left, right = 0, len(self.values) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if self.values[mid][0] == ts:
                return mid, True
            elif self.values[mid][0] < ts:
                left = mid + 1
            else:
                right = mid - 1
        return left, False

    def bfs2(self, ts):
        left, right = 0, len(self.price_order) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if self.price_order[mid] == ts:
                return mid
            elif self.price_order[mid] < ts:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def update(self, timestamp: int, price: int) -> None:
        # 需要注意的地方
        # 如果某条数据被撤销了，那么相关的最大值最小值同样应该被撤销
        index, exist = self.bfs(timestamp)
        if exist:
            old_price = self.values[index][1]
            self.values[index] = (timestamp, price)
            self.price_order.remove(old_price)
        else:
            self.values.insert(index, (timestamp, price))

        index = self.bfs2(price)
        self.price_order.insert(index, price)

        # print(self.values, "---", self.price_order)

    def current(self) -> int:
        return self.values[-1][1]

    def maximum(self) -> int:
        return self.price_order[-1]

    def minimum(self) -> int:
        return self.price_order[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()