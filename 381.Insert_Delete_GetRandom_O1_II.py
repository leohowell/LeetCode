# -*- coding: utf-8 -*-

"""
Design a data structure that supports all following operations
in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements.
The probability of each element being returned is linearly related to the
number of same value the collection contains.

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not
 contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection
contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with
 the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""


import random

class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = {}
        self.dupli = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection
        did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.values:
            key = '%s:%s' % (val, len(self.dupli.get(val, [])))
            self.values[key] = val
            if val in self.dupli:
                self.dupli[val].append(key)
            else:
                self.dupli[val] = [key]
            return False
        else:
            self.values[val] = val
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection
        contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.values:
            dupli_keys = self.dupli.get(val)
            if dupli_keys:
                self.values.pop(dupli_keys.pop())
            else:
                self.values.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.values:
            raise ValueError
        key = random.choice(self.values.keys())
        if isinstance(key, str):
            return int(key.split(':', 1)[0])
        else:
            return key


# Your RandomizedCollection object will be instantiated and called
# as such:
obj = RandomizedCollection()
print obj.insert(4),
print obj.insert(3),
print obj.insert(4),
print obj.insert(2),
print obj.insert(4),
print obj.remove(4),
print obj.remove(3),
print obj.remove(4),
print obj.remove(4)
# param_3 = obj.getRandom()

