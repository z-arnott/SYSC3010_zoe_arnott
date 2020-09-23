import sense_hat
import random

s = sense_hat.SenseHat()
s.clear()

purple = (184, 0, 235)
blue = (0, 232, 255)
orange = (252, 140, 3)
green = (0, 255, 17)
black = (0, 0, 0)

def letter_Z(color):
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

def letter_A(color):
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
letters = [letter_A, letter_Z]
i = 0

while True:
  s.set_pixels(letters[i](colors[0]))
  events = s.stick.get_events()
  for e in events:
    if e.action == sense_hat.ACTION_PRESSED:
      random.shuffle(colors)
      i = int(not bool(i))
    