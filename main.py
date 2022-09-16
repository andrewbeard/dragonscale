from microbit import accelerometer, button_a, button_b
import random

from output import ScrollingOutputHandler, BCDOutputHandler

DIE_FACES = [3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 20, 24, 30, 100]


def roll_result(faces: int) -> int:
    return random.randint(1, faces)


if button_a.is_pressed():
    output = BCDOutputHandler()
else:
    output = ScrollingOutputHandler()

die_index = DIE_FACES.index(20)
while True:
    a_presses = button_a.get_presses()
    if a_presses > 0:
        # Switch die size
        die_index = (die_index + a_presses) % len(DIE_FACES)
        output.die(DIE_FACES[die_index])
    elif button_b.was_pressed() or accelerometer.was_gesture("shake"):
        # Wait for any shaking to end first
        while accelerometer.is_gesture("shake"):
            output.shaking()
        # Roll the die
        result = roll_result(DIE_FACES[die_index])
        output.roll(result)
