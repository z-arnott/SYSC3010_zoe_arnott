import sense_emu
import random

s = sense_emu.SenseHat()
s.clear()

purple = (184, 0, 235)
blue = (0, 232, 255)
orange = (252, 140, 3)
green = (0, 255, 17)
black = (0, 0, 0)


# Lights necessary LEDs in LED matrix to form a letter 'Z' in chosen color
def letter_z(color):
    Y = color
    O = black
    Z = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, O, O, O, Y, Y, O, O,
    O, O, O, Y, Y, O, O, O,
    O, O, Y, Y, O, O, O, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    ]
    return Z


# Lights necessary LEDs in LED matrix to form a letter 'A' in specified color
def letter_a(color):
    Y = color
    O = black
    A = [
    O, O, O, O, O, O, O, O,
    O, O, O, Y, Y, O, O, O,
    O, O, Y, Y, Y, Y, O, O,
    O, Y, Y, O, O, Y, Y, O,
    O, Y, Y, Y, Y, Y, Y, O,
    O, Y, Y, O, O, Y, Y, O,
    O, Y, Y, O, O, Y, Y, O,
    O, Y, Y, O, O, Y, Y, O,
    ]
    return A


colors = [purple, blue, orange, green]
letters = [letter_a, letter_z]
i = 0

while True:
    s.set_pixels(letters[i](colors[0]))
    events = s.stick.get_events()
    for e in events:
        if e.action == sense_hat.ACTION_PRESSED:
            # change LEDs to random color
            random.shuffle(colors)
            # toggle letters
            i = int(not bool(i))