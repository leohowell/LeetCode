# 1188. 设计有限阻塞队列
# https://leetcode.cn/problems/design-bounded-blocking-queue/

from collections import deque

import threading


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = deque(maxlen=capacity)
        self.full_condition = threading.Condition()
        self.empty_condition = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.full_condition:
            self.full_condition.wait_for(lambda: self.size() < self.capacity)
            self.queue.append(element)
            with self.empty_condition:
                self.empty_condition.notify_all()

    def dequeue(self) -> int:
        with self.empty_condition:
            self.empty_condition.wait_for(lambda: self.size() > 0)
            val = self.queue.popleft()
            with self.full_condition:
                self.full_condition.notify_all()
            return val

    def size(self) -> int:
        return len(self.queue)


my_queue = BoundedBlockingQueue(2)


def consumer():
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()


def producer():
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(3)


t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)


t1.start()
t2.start()


# 3
# 3
# ["BoundedBlockingQueue","dequeue","dequeue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","dequeue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","enqueue","enqueue","enqueue","dequeue","dequeue","dequeue","dequeue","dequeue","dequeue","dequeue","enqueue","enqueue","enqueue","enqueue","enqueue","enqueue","enqueue","enqueue"]
# [[20],[],[],[0],[1],[2],[],[],[],[],[],[],[3],[4],[5],[6],[7],[8],[9],[],[],[],[],[],[],[],[10],[11],[12],[13],[14],[15],[16],[17]]

