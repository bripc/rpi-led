import binascii
import board
import neopixel
import urllib.request, json

from time import sleep

LIGHTWORK_URL = 'https://lightwork.hohmbody.com/pattern/1167'
DEBUG = True
LED_STRIP_LENGTH = 50
BRIGHTNESS = 1

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

        

