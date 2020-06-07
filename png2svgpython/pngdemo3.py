import os
import base64
import base64


def stringToBase64(s):
    return base64.b64encode(s.encode('utf-8'))

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

startSvgTag = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1"
xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"
width="240px" height="240px" viewBox="0 0 240 240">"""

endSvgTag = """</svg>"""
for files in os.listdir("."):
    if files.endswith(".png"):
        pngFile = open(files, 'rb')
        base64data = base64.b64encode(pngFile.read())
        base64String = '<image xlink:href="data:image/png;base64,{0}" width="240" height="240" x="0" y="0" />'.format(base64data)
        f = open(os.path.splitext(files)[0] + ".svg", 'w')
        f.write(startSvgTag + base64String + endSvgTag)
        print('Converted ', files, ' to ', os.path.splitext(files)[0], ".svg")