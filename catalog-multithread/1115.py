# 1115. 交替打印 FooBar
# https://leetcode.cn/problems/print-foobar-alternately/

from typing import Callable


import threading

lock01 = threading.Condition()


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_executed = False
        self.bar_executed = False

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        with lock01:
            for i in range(self.n):
                if self.foo_executed:
                    pass

                if self.foo_executed and not self.bar_executed:
                    lock01.wait()

                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.foo_executed = True
                self.bar_executed = False
                lock01.notify()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        with lock01:
            for i in range(self.n):
                if self.bar_executed or not self.foo_executed:
                    lock01.wait()
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.bar_executed = True
                self.foo_executed = False
                lock01.notify()



def printFoo():
    print("foo")


def printBar():
    print("bar")


foobar = FooBar(10)
t1 = threading.Thread(target=foobar.foo, args=(printFoo, ))
t2 = threading.Thread(target=foobar.bar, args=(printBar, ))

t2.start()
t1.start()
