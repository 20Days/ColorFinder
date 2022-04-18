from PIL import Image, ImageGrab
import pynput.mouse as ms
from pynput.mouse import Listener

mouse = ms.Controller()

def on_click(x, y, button, pressed):
    if str(button) == "Button.left" and pressed == True:
        image = ImageGrab.grab()
        color = image.getpixel((x, y))
        print(color)


with Listener(on_click=on_click) as listener:
    listener.join()