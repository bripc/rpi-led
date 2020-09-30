import base64
import binascii
import urllib.request, json

LIGHTWORK_URL = 'https://lightwork.hohmbody.com/pattern/1167'


with urllib.request.urlopen(LIGHTWORK_URL) as url:
    data = json.loads(url.read().decode())

    pixel_data = binascii.b2a_base64(bytearray(data['pixelData'], 'utf-8'))
    print(list(pixel_data))
