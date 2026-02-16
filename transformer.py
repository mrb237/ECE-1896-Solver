class Transformer:
    def __init__(self, name: str, bus1_name: str, bus2_name, r: float, x: float):
        self.name = name
        self.bus1_name = bus1_name
        self.bus2_name = bus2_name
        self.r = r
        self.x = x

if __name__ == "__main__":
    t1 = Transformer("t1", "bus1","bus2", 0.01, 0.10)
    print(t1.name, t1.bus1_name, t1.bus2_name, t1.r, t1.x)