from rpi_ws281x import PixelStrip, Color
import time

strip = PixelStrip(54, 18, 800000, 10, False, 255, 0)
strip.begin()

for i in range(strip.numPixels()):
    strip.setPixelColor(i, Color(0, 255, 0))
strip.show()

time.sleep(5)