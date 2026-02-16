class TransmissionLine:
    def __init__(self, name, bus1_name: str, bus2_name: str, r: float, x: float, g: float, b: float):
        self.name = name
        self.bus1_name = bus1_name
        self.bus2_name = bus2_name
        self.r = r
        self.x = x
        self.g = g
        self.b = b

if __name__ == "__main__":
    line1 = TransmissionLine("line1", "bus1", "bus2", 0.02, 0.25, 0.0, 0.04)
    print(line1.name, line1.bus1_name, line1.bus2_name, line1.r, line1.x, line1.g)