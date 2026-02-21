# Michael Bliesath - Main

import numpy as np
import pandas as pd

from Bus import Bus
from Circuit import Circuit
from Solution import Solution


if __name__ == "__main__":
    c = Circuit("SimpleCircuit")

    a = Bus("A")
    b = Bus("B")

    c.add_bus("A")
    c.add_bus("B")

    c.add_breaker("Breaker1", "A", "B", True)

    c.add_vsource_element("Va", "A", 100.0)

    c.add_resistor_element("Rab", "A", "B", 5.0)

    c.add_load_element("Lb", "B", 2000.0, 100.0)

    solution = Solution(c)
    solution.do_power_flow()

    c.print_nodal_voltage()
    c.print_circuit_current()

    print(f"Breaker off scenario")

    c.breakers["Breaker1"].toggle()

    solution = Solution(c)
    solution.do_power_flow()

    c.print_nodal_voltage()
    c.print_circuit_current()