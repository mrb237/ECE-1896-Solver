from Bus import Bus
from generator import Generator
from load import Load
from transformer import Transformer
from transmission_line import TransmissionLine

class Circuit:
    def __init__(self, name:str):
        self.name = name
        self.buses = {}
        self.transformers = {}
        self.transmission_lines = {}
        self.generators = {}
        self.loads = {}

    def add_bus(self, name:str):
        if name in self.buses.keys():
            raise ValueError(f"Bus '{name}' already exists.")
        self.buses[name] = Bus(name)