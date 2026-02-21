# Michael Bliesath - Bus

import numpy as np
import pandas as pd

class Bus:
    def __init__(self, name:str):
        self.name = name
        self._v = None # Change - Default voltage value

    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, new_v:float): # Fix
        if new_v < 0:
            raise ValueError("Bus voltage must be a non-negative value.")
        self._v = new_v

if __name__ == '__main__':
    bus1 = Bus("Bus1")
    print(f"Bus1 Voltage: {bus1.v} Volts")

    bus1.v = 9.0
    print(f"Bus1 Voltage: {bus1.v} Volts")

    bus1.v = -1.0
    print(f"Bus1 Voltage: {bus1.v} Volts")