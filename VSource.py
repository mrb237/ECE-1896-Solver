# Michael Bliesath - VSource

import numpy as np
import pandas as pd

from Bus import Bus

class VSource:
    def __init__(self, name:str, bus1:Bus, v:float):
        self.name = name
        self.bus1 = bus1
        self.v = v

        self.bus1.v = self.v # Possibly change

if __name__ == '__main__':
    a = Bus("A")
    vsource1 = VSource("VSource1", a, 9.0)

    print(f"VSource Name: {vsource1.name}")
    print(f"Connected Bus: {vsource1.bus1.name}")
    print(f"Source Voltage: {vsource1.v} Volts")
    print(f"Bus Voltage after source creation: {a.v} Volts")
