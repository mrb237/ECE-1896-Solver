# Michael Bliesath - Breaker

# import numpy as np
# import pandas as pd

class Breaker:
    def __init__(self, name: str, node1: str, node2: str, is_closed: bool = True):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self._closed = bool(is_closed)

    def open(self):
        self._closed = False

    def close(self):
        self._closed = True

    def toggle(self):
        self._closed = not self._closed

    @property
    def is_closed(self) -> bool:
        return self._closed