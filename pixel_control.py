from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255, 0, 0)     # red
o = (255, 128, 0)   # orange
y = (255, 255, 0)   # yellow
g = (0, 255, 0)     # green
c = (0, 255, 255)   # cyan
b = (0, 0, 255)     # blue
p = (255, 0, 255)   # purple
n = (255, 128, 128) # pink
w =(255, 255, 255)  # white
k = (0, 0, 0)       # blank

rainbow = [r, o, y, g, c, b, p, n]
image = [
        k, k, k, k, k, k, k, k,
        k, b, b, k, k, b, b, k,
        k, b, b, k, k, b, b, k,
        k, k, k, k, k, k, k, k,
        b, k, k, k, k, k, k, b,
        k, b, k, k, k, k, b, k,
        k, k, b, b, b, b, k, k,
        k, k, k, k, k, k, k, k,
        ]



while True:
    sense.clear()
    sense.set_pixels(image)
    sleep(3)

    for y in range(8):
        colour = rainbow[y]
        for x in range(8):
            sense.set_pixel(x, y, colour)

    sleep(3)
