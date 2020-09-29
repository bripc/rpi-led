import board
import neopixel

from time import sleep

pixels = neopixel.NeoPixel(board.D18, 50, brightness=1)
pixels.fill((0, 0, 0))
sleep(2)
pixels.fill((0, 200, 150)) # green, red, blue

pixels.show()
sleep(5)
pixels.fill((0, 0, 0))
pixels.show()
