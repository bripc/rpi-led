import binascii
import board
import neopixel
import urllib.request, json

from time import sleep

LIGHTWORK_URL = 'https://lightwork.hohmbody.com/pattern/1161'
DEBUG = True
LED_STRIP_LENGTH = 50
BRIGHTNESS = .25

class LightWork():
    pixel_length = 0
    frames = 0
    fps = 0
    pixel_data = []


    def get_from_url(self):
        with urllib.request.urlopen(LIGHTWORK_URL) as url:
            data = json.loads(url.read().decode())

            self.pixel_length = data['pixels']
            self.frames = data['frames']
            self.fps = data['fps']
            self.pixel_data = list(binascii.b2a_base64(
                bytearray(data['pixelData'], 'utf-8')))

            if DEBUG:
                print('pixel_length', self.pixel_length)
                print('frames', self.frames)
                print('fps', self.fps)
                # print('pixel data', self.pixel_data)


# initialize the lightwork from remote source
lightwork = LightWork()
lightwork.get_from_url()

# initialize the LEDs
pixels = neopixel.NeoPixel(
    board.D18, LED_STRIP_LENGTH, brightness=BRIGHTNESS)
pixels.fill((0, 0, 0))
sleep(2)

# loop the lightwork
current_frame = 0
while(True):
    for i in range(LED_STRIP_LENGTH):
        pixel_index = i % lightwork.pixel_length
        index = ((current_frame * lightwork.pixel_length * 3) +
                (pixel_index * 3))
        pixels[i] = (
            lightwork.pixel_data[index + 1], # green
            lightwork.pixel_data[index], # red
            lightwork.pixel_data[index + 2]) # blue
    pixels.show()
    current_frame += 1
    if current_frame >= lightwork.frames:
        current_frame = 0
    sleep(1 / lightwork.fps)
    
