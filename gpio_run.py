# Michael Bliesath - GPIO_Run (updated)

import time
import signal
import sys
from gpiozero import LED, Button
from rpi_ws281x import PixelStrip, Color

from Circuit import Circuit
from Solution import Solution
from Bus import Bus

# ---------- GPIO CONFIG ----------
# Input: physical switch wired to 3.3V; other leg to this pin.
# Internal pull-down keeps the pin LOW until the switch is pressed.
SWITCH_PIN   = 26          # <-- change if you wire to a different pin

# Output: signal pins that fire when the breaker opens
SIGNAL_PINS  = [4, 17, 27, 22, 23, 24, 25]

# NeoPixel (addressable LED) config on GPIO 18
LED_COUNT    = 8           # adjust to your strip length
LED_PIN      = 18
LED_FREQ_HZ  = 800_000
LED_DMA      = 10
LED_INVERT   = False
LED_CHANNEL  = 0
LED_BRIGHTNESS = 128       # 0-255

# ---------- HARDWARE INIT ----------
breaker_switch = Button(SWITCH_PIN, pull_up=False)
signal_leds    = [LED(p) for p in SIGNAL_PINS]

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ,
                   LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# ---------- LED HELPERS ----------
def _fill(color):
    """Set every pixel to *color* and show immediately."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def sequence_blue_green():
    """
    Sequence: each pixel steps from blue to green one at a time,
    matching the previous blue→green animation style.
    """
    BLUE  = Color(0,   0,   255)
    GREEN = Color(0,   255, 0)
    _fill(BLUE)
    time.sleep(0.3)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, GREEN)
        strip.show()
        time.sleep(0.1)

def solid_green():
    _fill(Color(0, 255, 0))

def leds_off():
    _fill(Color(0, 0, 0))

# ---------- BUILD CIRCUIT ----------
c = Circuit("SimpleCircuit")
c.add_bus("A")
c.add_bus("B")
c.add_vsource_element("Va", "A", 100.0)
c.add_resistor_element("Rab", "A", "B", 5.0)
c.add_load_element("Lb", "B", 2000.0, 100.0)
c.add_breaker("Breaker1", "A", "B", True)

solution = Solution(c)
solution.do_power_flow()

# ---------- BREAKER ACTIONS ----------
def _signal_pins_on():
    for led in signal_leds:
        led.on()

def _signal_pins_off():
    for led in signal_leds:
        led.off()

def open_breaker():
    c.breakers["Breaker1"].open()
    solution.do_power_flow()

    _signal_pins_on()        # Assert all 7 output signals
    sequence_blue_green()    # Blue → green NeoPixel sequence on GPIO 18

    print("Breaker Opened:")
    c.print_nodal_voltage()
    c.print_circuit_current()
    print("---------------")

def close_breaker():
    c.breakers["Breaker1"].close()
    solution.do_power_flow()

    _signal_pins_off()       # De-assert all 7 output signals
    solid_green()            # Steady green while closed

    print("Breaker Closed:")
    c.print_nodal_voltage()
    c.print_circuit_current()
    print("---------------")

# ---------- CLEAN SHUTDOWN ----------
def shutdown(sig, frame):
    print("\nShutting down...")
    _signal_pins_off()
    leds_off()
    sys.exit(0)

signal.signal(signal.SIGINT,  shutdown)
signal.signal(signal.SIGTERM, shutdown)

# ---------- ATTACH SWITCH ----------
breaker_switch.when_pressed  = open_breaker   # switch HIGH  → open
breaker_switch.when_released = close_breaker  # switch LOW   → close

# ---------- STARTUP ----------
solution.do_power_flow()
solid_green()   # Nominal state: steady green
print("System running...  (Ctrl+C to stop)")

while True:
    time.sleep(0.1)