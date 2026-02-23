# Michael Bliesath - GPIO_Run

import time
from gpiozero import LED, Button

from Circuit import Circuit
from Solution import Solution
from Bus import Bus

# ---------- GPIO CONFIG ----------
BREAKER_PIN = 17
LED_PIN = 27

breaker_switch = Button(BREAKER_PIN, pull_up=False)
status_led = LED(LED_PIN)

# ---------- BUILD CIRCUIT ----------
c = Circuit("SimpleCircuit")
a = Bus("A")
b = Bus("B")

c.add_bus("A")
c.add_bus("B")

c.add_vsource_element("Va", "A", 100.0)
c.add_resistor_element("Rab", "A", "B", 5.0)
c.add_load_element("Lb", "B", 2000.0, 100.0)
c.add_breaker("Breaker1", "A", "B", True)

solution = Solution(c)
solution.do_power_flow()

def open_breaker():
    c.breakers["Breaker1"].open()
    status_led.on()
    solution.do_power_flow()
    print("Breaker Opened:")
    c.print_nodal_voltage()
    c.print_circuit_current()
    print("---------------")

def close_breaker():
    c.breakers["Breaker1"].close()
    status_led.off()
    solution.do_power_flow()
    print("Breaker Closed:")
    c.print_nodal_voltage()
    c.print_circuit_current()
    print("---------------")

breaker_switch.when_pressed = open_breaker
breaker_switch.when_released = close_breaker

# Initial solve
solution.do_power_flow()

print("System running...")

while True:
    time.sleep(0.1)