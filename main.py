from microbit import *
import random

DIE_FACES = [3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 20, 24, 30, 100]


def roll_result(faces):
    return random.randint(1, faces)


die_index = DIE_FACES.index(20)
while True:
    a_presses = button_a.get_presses()
    if a_presses > 0:
        # Switch die size
        die_index = (die_index + a_presses) % len(DIE_FACES)
        display.scroll("d{}".format(DIE_FACES[die_index]), delay=100)
    elif button_b.was_pressed() or accelerometer.was_gesture("shake"):
        # Wait for any shaking to end first
        while accelerometer.is_gesture("shake"):
            display.show("?")
        # Roll the die
        result = roll_result(DIE_FACES[die_index])
        display.scroll(str(result))
