# rpi-led
Display light shows on a Raspberry Pi microcontroller!
This project utilizes the [Flickerstrip Lightwork Editor](https://hohmbody.com/flickerstrip/lightwork/?browse) that returns JSON of LED patterns created by users of the site.

### Dependencies:
- [rpi-ws281x](https://pypi.org/project/rpi-ws281x/) *(Note that I have WS2811 LEDs)*
- [adafruit-circuitpython-neopixel](https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython)

### To Run:
`sudo python3 main.py`

The other files are tests and color calibration that were used in debugging.
