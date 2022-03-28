# -*- coding: utf-8 -*-


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.__values = {}
        self.__access = []

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.__values:
            self.__access.remove(key)
            self.__access.append(key)
            return self.__values[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if not self.capacity:
            return
        if key in self.__values:
            self.__access.remove(key)
        else:
            while len(self.__values) >= self.capacity:
                self.cleanup()
        self.__access.append(key)
        self.__values[key] = value

    def cleanup(self):
        del self.__values[self.__access.pop(0)]
