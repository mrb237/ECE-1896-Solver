# Michael Bliesath - GPIO_Run

import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    raise SystemExit("RPi.GPIO not found. Run this on a Raspberry Pi with RPi.GPIO installed.")

from Circuit import Circuit

# ---------- GPIO CONFIG ----------
GPIO.setmode(GPIO.BCM)

BREAKER_PIN = 17  # BCM 17 (physical pin 11)
# We'll use internal pull-up: switch connects pin->GND when "closed" (or vice versa)
GPIO.setup(BREAKER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

DEBOUNCE_MS = 80

def read_breaker_closed() -> bool:
    """
    With PUD_UP:
    - pin reads 1 when switch OPEN (not connected to GND)
    - pin reads 0 when switch CLOSED (connected to GND)
    Adjust logic based on your wiring.
    """
    return GPIO.input(BREAKER_PIN) == 0

# ---------- BUILD CIRCUIT ----------
c = Circuit()
# build your circuit elements as your project expects...
# e.g., c.add_bus(...), c.add_line(...), etc.

# Add breaker between nodes A and B
br = c.add_breaker("BR_AB", "A", "B", is_closed=True)

# solver = Solution(c)  # <-- create your solver instance

def run_solver_and_visualize():
    # solver.do_power_flow()   # <-- call your actual solve method
    # results = solver.results  # <-- or however you store results
    # For now, just show breaker state:
    print(f"Breaker {br.name} closed? {br.is_closed}")
    # TODO: update LEDs / display here using solver outputs

def main():
    try:
        # Initialize from switch position
        br._closed = read_breaker_closed()
        run_solver_and_visualize()

        last_state = br.is_closed

        while True:
            current_state = read_breaker_closed()
            if current_state != last_state:
                br._closed = current_state
                run_solver_and_visualize()
                last_state = current_state

            time.sleep(0.05)

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
