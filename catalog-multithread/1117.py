from typing import Callable

import threading


class H2O:
    def __init__(self):
        self.barrier01 = threading.Barrier(3)
        self.s1 = threading.Semaphore(1)
        self.s2 = threading.Semaphore(2)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.s2.acquire()
        self.barrier01.wait()
        releaseHydrogen()
        self.s2.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.

        self.s1.acquire()
        self.barrier01.wait()
        releaseOxygen()
        self.s1.release()


def releaseHydrogen():
    print("H")


def releaseOxygen():
    print("O")


z = H2O()
t1 = threading.Thread(target=z.hydrogen, args=(releaseHydrogen,))
t2 = threading.Thread(target=z.hydrogen, args=(releaseHydrogen,))
t3 = threading.Thread(target=z.oxygen, args=(releaseOxygen,))

t1.start()
t2.start()
t3.start()
