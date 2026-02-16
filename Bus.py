class Bus:
    index_counter = 1

    def __init__(self, name:str, nominal_kv:float):
        self.name = name
        self.nominal_kv = nominal_kv
        self.bus_index = Bus.index_counter
        Bus.index_counter += 1

if __name__ == "__main__":
    bus1 = Bus("Bus1", 20.0)

    print(f"Bus1 name: {bus1.name}")
    print(f"Bus1 Nominal Voltage: {bus1.nominal_kv} Volts")
    print(f"Bus1 Index: {bus1.bus_index}")

    bus2 = Bus("Bus2", 230.0)

    print(f"Bus2 name: {bus2.name}")
    print(f"Bus2 Nominal Voltage: {bus2.nominal_kv} Volts")
    print(f"Bus2 Index: {bus2.bus_index}")