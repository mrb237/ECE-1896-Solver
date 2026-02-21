# Michael Bliesath - Circuit

import numpy as np
import pandas as pd

from Bus import Bus
from Resistor import Resistor
from load import Load
from VSource import VSource
from Breaker import Breaker

class Circuit:
    def __init__(self, name:str):
        self.name = name

        self.buses = {}
        self.resistors = {}
        self.loads = {}
        self.breakers = {}

        self.vsource = None # Default
        self.i = None # Default


    def add_bus(self, name:str):
        if name in self.buses.keys():
            raise ValueError(f"Bus '{name}' already exists.")
        self.buses[name] = Bus(name)


    def add_resistor_element(self, name:str, bus1_name:str, bus2_name:str, r:float):
        try:
            bus1 = self.buses[bus1_name]
            bus2 = self.buses[bus2_name]
        except KeyError as e:
            raise KeyError(f"Buses '{e.args[0]}' do not exist.")

        if name in self.resistors.keys():
            raise ValueError(f"Resistor '{name}' already exists.")
        self.resistors[name] = Resistor(name, bus1, bus2, r)


    def add_load_element(self, name:str, bus1_name:str, p:float, v:float):
        try:
            bus1 = self.buses[bus1_name]
        except KeyError as e:
            raise KeyError(f"Buses '{e.args[0]}' do not exist.")

        if name in self.loads.keys():
            raise ValueError(f"Load '{name}' already exists.")
        self.loads[name] = Load(name, bus1, p, v)


    def add_vsource_element(self, name:str, bus1_name:str, v:float):
        try:
            bus1 = self.buses[bus1_name]
        except KeyError as e:
            raise KeyError(f"Buses '{e.args[0]}' do not exist.")
        self.vsource = VSource(name, bus1, v)

    def add_breaker(self, name: str, node1: str, node2: str, is_closed: bool = True):
        br = Breaker(name, node1, node2, is_closed=is_closed)
        self.breakers[name] = br
        return br

    def is_connection_closed(self, node1: str, node2: str) -> bool:
        for br in self.breakers.values():
            a = br.node1
            b = br.node2
            if((a==node1 and b==node2) or (a==node2 and b==node1)):
                return br.is_closed
        return True

    def set_i(self, i:float):
        self.i = i


    def print_nodal_voltage(self):
        for bus_name, bus_obj in self.buses.items():
            print(f"Bus {bus_name} Voltage: {bus_obj.v} V")


    def print_circuit_current(self):
        print(f"Circuit Current: {self.i} A")


if __name__ == "__main__":
    c = Circuit("SimpleCircuit")

    # a = Bus("A")
    # b = Bus("B")

    c.add_bus("A")
    c.add_bus("B")

    c.add_vsource_element("V1", "A", 10.0)
    c.add_resistor_element("R1", "A", "B", 5.0)
    c.add_load_element("L1", "B", 20.0, 10.0)

    r_series = next(iter(c.resistors.values()))
    load = next(iter(c.loads.values()))

    Vs = c.vsource.v
    R1 = r_series.r
    RL = load.r

    I = Vs / (R1+RL)
    c.set_i(I)

    Vb = I * RL
    c.buses["B"].v = Vb

    print("Buses:", list(c.buses.keys()))
    print("Resistors:")
    for r_name, r_obj in c.resistors.items():
        print(f"  {r_name}: R = {r_obj.r} Ohms, G = {r_obj.g} Siemens")
    print("Loads:")
    for l_name, l_obj in c.loads.items():
        print(f"  {l_name}: P = {l_obj.p} W, V_nom = {l_obj.v} V, R = {l_obj.r} Ohms, G = {l_obj.g} Siemens")
    print(f"VSource: {c.vsource.name}, V = {c.vsource.v} V, Bus = {c.vsource.bus1.name}")

    c.print_nodal_voltage()
    c.print_circuit_current()