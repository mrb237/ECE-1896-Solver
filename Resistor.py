# Michael Bliesath - Resistor

import numpy as np
import pandas as pd

from Bus import Bus

class Resistor:
    def __init__(self, name:str, bus1:Bus, bus2:Bus, r:float):
        self.name = name
        self.bus1 = bus1
        self.bus2 = bus2
        self.r = r

        if self.r <= 0:
            raise ValueError("Resistor resistance r must be > 0.")

        self.g = self._calc_g()# Default until calculated with calc_g()


    def _calc_g(self):
        return 1.0/self.r

if __name__ == '__main__':
    a = Bus("A")
    b = Bus("B")
    resistor1 = Resistor("Resistor1", a, b, 100.0)

    print(f"Resistor1 Name: {resistor1.name}")
    print(f"Resistor1 First Bus: {resistor1.bus1.name}")
    print(f"Resistor1 Second Bus: {resistor1.bus2.name}")
    print(f"Resistor1 Resistance: {resistor1.r} Ohms")
    print(f"Resistor1 Conductance: {resistor1.g} Siemens")
