class Generator:
    def __init__(self, name:str, bus1_name:str, voltage_setpoint:float, mw_setpoint:float):
        self.name = name
        self.bus1_name = bus1_name
        self.voltage_setpoint = voltage_setpoint
        self.mw_setpoint = mw_setpoint

if __name__ == "__main__":
    gen1 = Generator("G1", "Bus 1", 1.04, 100.0)

    print(f"Generator1 Name: {gen1.name}")
    print(f"Generator1 Bus Name: {gen1.bus1_name}")
    print(f"Generator1 Voltage Setpoint (V): {gen1.voltage_setpoint}")
    print(f"Load1 Real Power Setpoint (MW): {gen1.mw_setpoint}")