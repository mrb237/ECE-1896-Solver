#!/usr/bin/env python3
"""
gpio_trigger.py
Monitors GPIO 13 (input) and drives GPIO 26 (output) to match its state.
GPIO 13 HIGH  →  GPIO 26 HIGH
GPIO 13 LOW   →  GPIO 26 LOW
"""

import RPi.GPIO as GPIO
import time

INPUT_PIN  = 13
OUTPUT_PIN = 26

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(INPUT_PIN,  GPIO.IN,  pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)

def on_edge(channel):
    state = GPIO.input(INPUT_PIN)
    GPIO.output(OUTPUT_PIN, state)
    label = "ON" if state else "OFF"
    print(f"GPIO {INPUT_PIN} changed -> GPIO {OUTPUT_PIN}: {label}")

def on_rising(channel):
    """Called when GPIO 13 goes HIGH."""
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    print(f"GPIO {INPUT_PIN} HIGH  →  GPIO {OUTPUT_PIN} ON")

def on_falling(channel):
    """Called when GPIO 13 goes LOW."""
    GPIO.output(OUTPUT_PIN, GPIO.LOW)
    print(f"GPIO {INPUT_PIN} LOW   →  GPIO {OUTPUT_PIN} OFF")

def main():
    setup()
    GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=on_edge, bouncetime=50)

    print(f"Monitoring GPIO {INPUT_PIN}. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        GPIO.output(OUTPUT_PIN, GPIO.LOW)
        GPIO.cleanup()

if __name__ == "__main__":
    main()