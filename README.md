# rpi-led
Display light shows on a Raspberry Pi microcontroller!
This project utilizes the [Flickerstrip Lightwork Editor](https://hohmbody.com/flickerstrip/lightwork/?browse) that returns JSON of LED patterns created by users of the site.

### Dependencies:
- [rpi-ws281x](https://pypi.org/project/rpi-ws281x/) *(Note that I have WS2811 LEDs)*
- [adafruit-circuitpython-neopixel](https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython)

### To Run:
1. Have the Data Input attached to PIN 18 of the Pi and the ground attched to a Ground PIN of the Pi.
2. Hook up the power source of the LED strip to an external 5V power source
3. Make sure the dependencies are installed
4. Run `sudo python3 main.py`. Sudo is required to access the pins on the Pi's board

**Note**: The other files are tests and color calibration that were used in debugging.
