from microbit import display


class OutputHandler:
    def roll(self, result: int) -> None:
        pass

    def shaking(self) -> None:
        pass

    def die(self, faces: int) -> None:
        pass


class ScrollingOutputHandler(OutputHandler):
    def roll(self, result: int) -> None:
        display.scroll(result)

    def shaking(self) -> None:
        display.show("?")

    def die(self, faces: int) -> None:
        display.scroll("d{}".format(faces), delay=100)


class BCDOutputHandler(OutputHandler):
    brightness = 6

    def __init__(self) -> None:
        display.clear()

    def show_column_value(self, column: int, value: int) -> None:
        for i in range(5):
            if int(value) & (1 << i):
                disp = self.brightness
            else:
                disp = 0
            display.set_pixel(column, 4 - i, disp)

    def roll(self, result: int) -> None:
        self.show_column_value(3, result / 10)
        self.show_column_value(4, result % 10)

    def die(self, faces: int) -> None:
        self.show_column_value(0, faces / 10)
        self.show_column_value(1, faces % 10)
