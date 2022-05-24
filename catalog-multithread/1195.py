from typing import Callable

import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.finish = False
        self.fizzbuzz_event = threading.Event()
        self.fizz_event = threading.Event()
        self.buzz_event = threading.Event()
        self.number_event = threading.Event()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.fizz_event.wait()
            self.fizz_event.clear()
            if self.finish:
                break
            printFizz()
            self.number_event.set()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.buzz_event.wait()
            self.buzz_event.clear()
            if self.finish:
                break
            printBuzz()
            self.number_event.set()


    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fizzbuzz_event.wait()
            self.fizzbuzz_event.clear()
            if self.finish:
                break
            printFizzBuzz()
            self.number_event.set()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            if i % 15 == 0:
                self.fizzbuzz_event.set()
                self.number_event.wait()
                self.number_event.clear()
            elif i % 3 == 0:
                self.fizz_event.set()
                self.number_event.wait()
                self.number_event.clear()
            elif i % 5 == 0:
                self.buzz_event.set()
                self.number_event.wait()
                self.number_event.clear()
            else:
                printNumber(i)
        self.finish = True
        self.fizzbuzz_event.set()
        self.fizz_event.set()
        self.buzz_event.set()
