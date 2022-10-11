"""
Python version 3
"""
from collections import OrderedDict
import json


class LRUClass:
    """

    """

    def __init__(self, capacity):
        """
        initialize LRUCLASS object
        cache is declared as OrderedDict to conserve the order of the element
        operations, cache_after, return_value, side_effect are used to store the report data Extra to Test
        :param capacity:
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        self.operations = []
        self.cache_after = []
        self.return_value = []
        self.side_effect = []

    def put(self, key, value):
        """
         Add or updates the value for the key
        :param key:
        :param value:
        :return:
        """
        # if cache is empty add without any check
        if not len(self.cache):
            self.cache[key] = value
            # Save The Data to generate report
            self.cache_after.append(json.dumps(dict({key: value}), indent=1))
            self.return_value.append(str(key) + "->" + str(value))
            self.side_effect.append("added to cache")
        else:
            # If the new key exists in the cache delete it and add it again to be inserted in the top of
            # the cache as LRU
            if key in self.cache.keys():
                del self.cache[key]
                self.cache[key] = value
                # Save The Data to generate report
                self.cache_after.append(json.dumps(dict(reversed(list(self.cache.items()))), indent=1))
                self.return_value.append(str(key) + "->" + str(value))
                self.side_effect.append("Key " + str(key) + " updated,became the most recently used(MRU)")
            else:
                # if cache reached the max size delete last unused element
                if len(self.cache) >= self.capacity:
                    x = self.cache.popitem(last=False)
                    self.cache[key] = value
                    # Save The Data to generate report
                    self.cache_after.append(json.dumps(dict(reversed(list(self.cache.items()))), indent=1))
                    self.return_value.append(str(key) + "->" + str(value))
                    self.side_effect.append(str(x) + "got evicted")
                else:
                    self.cache[key] = value
                    # Save The Data to generate report
                    self.cache_after.append(json.dumps(dict(reversed(list(self.cache.items()))), indent=1))
                    self.return_value.append(str(key) + "->" + str(value))
                    self.side_effect.append(str(list(self.cache.keys())[-1]) + "->" + str(
                        self.cache[(list(self.cache.keys()))[-1]]) + " became LRU")

    def get(self, key):
        """
        returns either the cached value or -1
        :param key:
        :return: Int cached element
        """
        if key not in self.cache.keys():
            self.cache_after.append(json.dumps(dict(reversed(list(self.cache.items()))), indent=1))
            self.return_value.append(str(-1))
            self.side_effect.append("access order unchanged")
            return -1
        else:
            # delete Searched key  and add it again to be inserted in the top of cache
            exist_value = self.cache[key]
            key_of_index_0 = list(self.cache.keys())[-1]
            del self.cache[key]
            self.cache[key] = exist_value
            # check Used to Generate the report
            if key_of_index_0 == key:
                # Save The Data to generate report
                self.cache_after.append(json.dumps(dict(reversed(list(self.cache.items()))), indent=1))
                self.return_value.append(str(key) + "->" + str(self.cache[key]))
                self.side_effect.append("No change " + str(key) + " already was the MRU")
            else:
                # Save The Data to generate report
                self.cache_after.append(json.dumps(dict(reversed(list(self.cache.items()))), indent=1))
                self.return_value.append(str(self.cache[key]))
                self.side_effect.append(str(list(self.cache.keys())[-1]) + "->" + str(
                    self.cache[(list(self.cache.keys()))[-1]]) + " became LRU")
            return self.cache[key]
