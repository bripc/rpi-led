import board
import neopixel

from time import sleep

LED_STRIP_LENGTH = 50
BRIGHTNESS = .25

RED = (0, 255, 0)
GREEN = (255, 0, 0) # my strip is weird in that the first bit is green
BLUE = (0, 0, 255)

pixel_array = [
	255, 0, 0, 0, 255, 0, 0, 0, 255,  # red, green, blue
	0, 255, 0, 0, 0, 255, 255, 0, 0,  # green, blue, red
	0, 0, 255, 255, 0, 0, 0, 255, 0,  # blue, red, green
]

pixels = neopixel.NeoPixel(
    board.D18, LED_STRIP_LENGTH, brightness=BRIGHTNESS)
pixels.fill((0, 0, 0))
sleep(2)

current_frame = 0
while(True):
    print('current_frame', current_frame)
    for i in range(LED_STRIP_LENGTH):
        pixel_index = i % len(pixel_array)
        index = ((current_frame * len(pixel_array) * 3) +
                pixel_index * 3)
        print('pixel index', pixel_index)
        print('index', index)
        pixels[i] = (
			pixel_array[index + 1], # green
			pixel_array[index], # red
			pixel_array[index + 2] # blue
        )
    pixels.show()
    current_frame += 1
    if current_frame >= 3:
        current_frame = 0
    sleep(.5)
            
            
