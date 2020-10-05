import sense_emu
s = sense_emu.SenseHat()
s.clear()

def letter_a(color):
    Y = color
    O = color
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

while True:
    events = s.stick.get_events()
    for e in events:
        if e.direction == 'up':
            # turn LEDs off
            s.set_pixels(letter_a((0,0,0)))

        if e.direction == 'down':
            # turn LEDs off
            s.set_pixels(letter_a((255, 255, 255)))

