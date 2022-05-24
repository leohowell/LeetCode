# 1114. 按序打印
# https://leetcode.cn/problems/print-in-order/

from typing import Callable

def printFirst():
    print("first")

def printSecond():
    print("second")

def printThird():
    print("third")

import threading

lock01 = threading.Condition()
lock02 = threading.Condition()


class Foo:
    def __init__(self):
        self.first_executed = False
        self.second_executed = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with lock01:
            printFirst()
            self.first_executed = True
            lock01.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with lock01:
            lock01.wait_for(lambda: self.first_executed)
            with lock02:
                printSecond()
                self.second_executed = True
                lock02.notify_all()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with lock02:
            lock02.wait_for(lambda: self.second_executed)
            printThird()


foo = Foo()
t1 = threading.Thread(target=foo.first, args=(printFirst, ))
t2 = threading.Thread(target=foo.second, args=(printSecond, ))
t3 = threading.Thread(target=foo.third, args=(printThird, ))

t3.start()
t2.start()
t1.start()


# [1,2,3]
# [1,3,2]
# [2,3,1]
# [2,1,3]
# [3,2,1]
# [3,1,2]
