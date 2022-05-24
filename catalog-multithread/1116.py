from typing import Callable

import threading

lock01 = threading.Condition()

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n

        self.last_printed = None
        self.second_to_last_printed = None

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        """
        1. 首先打印
        2. 在奇数、偶数打印完成后打印
        """
        with lock01:
            for i in range(self.n):
                # 等待的情况
                lock01.wait_for(lambda: self.last_printed != 0)

                printNumber(0)
                self.second_to_last_printed = self.last_printed
                self.last_printed = 0
                lock01.notify_all()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        """
        1. 在 奇数 0 之后打印
        """
        with lock01:
            for i in range(2, self.n+1, 2):
                # 等待的情况
                lock01.wait_for(lambda: self.second_to_last_printed is not None and self.second_to_last_printed + 1 == i)
                printNumber(i)
                self.second_to_last_printed = self.last_printed
                self.last_printed = i
                lock01.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        """
        1. 在0之后打印
        """
        with lock01:
            for i in range(1, self.n+1, 2):
                lock01.wait_for(lambda: self.second_to_last_printed is None or self.second_to_last_printed + 1 == i)
                printNumber(i)
                self.second_to_last_printed = self.last_printed
                self.last_printed = i
                lock01.notify_all()


def printNumber(x):
    print(x)


z = ZeroEvenOdd(10)

t1 = threading.Thread(target=z.zero, args=(printNumber, ))
t2 = threading.Thread(target=z.even, args=(printNumber, ))
t3 = threading.Thread(target=z.odd, args=(printNumber, ))

t1.start()
t2.start()
t3.start()
