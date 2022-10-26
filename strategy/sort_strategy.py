import configparser
import logging
import sys

class SortStrategy:
    
    def __init__(self, strategy):
        self.set_strategy(strategy)

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_sort(self, array):
       strategy = self.strategy(array)
       return strategy.sort()