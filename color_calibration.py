import board
import neopixel

from time import sleep

LED_STRIP_LENGTH = 10
BRIGHTNESS = .25

RED = (0, 255, 0)
GREEN = (255, 0, 0)

pixels = neopixel.NeoPixel(
    board.D18, LED_STRIP_LENGTH, brightness=BRIGHTNESS)
pixels.fill((0, 0, 0))
sleep(2)

color1 = RED
color2 = GREEN

while(True):
	for i in range(LED_STRIP_LENGTH):
		if i % 2 == 0:
			pixels[i] = color1
		else:
			pixels[i] = color2
	pixels.show()
	sleep(.5)
	color1 = RED if color1 == GREEN else GREEN
	color2 = GREEN if color2 == RED else RED
			
			
