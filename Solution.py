# Michael Bliesath - Solution

# import numpy as np
# import pandas as pd

from Circuit import Circuit
from Breaker import Breaker


class Solution:
    def __init__(self, circuit:Circuit):
        self.circuit = circuit

    def do_power_flow(self):
        c = self.circuit

        if c.vsource is None:
            raise ValueError("Circuit must contain a voltage source.")
        if len(c.resistors) != 1:
            raise ValueError("This solver expects exactly ONE resistor.")
        if len(c.loads) != 1:
            raise ValueError("This solver expects exactly ONE load.")
        if "A" not in c.buses or "B" not in c.buses:
            raise ValueError("Circuit must contain buses 'A' and 'B'.")
        if not c.is_connection_closed("A", "B"):
            c.set_i(0.0)
            c.buses["B"].v = 0.0
        else:
            pass

        r_series = next(iter(c.resistors.values()))
        load = next(iter(c.loads.values()))

        va = float(c.buses["A"].v)

        g_series = float(r_series.g)
        g_load = float(load.g)

        if g_series <= 0 or g_load <= 0:
            raise ValueError("Conductances must be > 0.")

        i = va * (g_series * g_load) / (g_series + g_load)
        c.set_i(i)

        vb = i / g_load
        c.buses["B"].v = vb