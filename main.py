from abc import ABC, abstractmethod


class ComputerColor(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __mul__(self, other) -> str:
        pass

    @abstractmethod
    def __rmul__(self, other) -> str:
        pass


class Color(ComputerColor):
    def __init__(self, red_level: int, green_level: int, blue_level: int) -> None:
        self.red_level = red_level
        self.green_level = green_level
        self.blue_level = blue_level

    def __str__(self) -> str:
        return f'\033[1;38;2;{self.red_level};{self.green_level};{self.blue_level}m●\033[0m'

    def __repr__(self) -> str:
        return f'\033[1;38;2;{self.red_level};{self.green_level};{self.blue_level}m●\033[0m'

    def __eq__(self, other):
        if not isinstance(other, Color):
            raise TypeError('Is not a Color instance')
        return self.red_level == other.red_level and \
            self.green_level == other.green_level and \
            self.blue_level == other.blue_level

    def __add__(self, other):
        if not isinstance(other, Color):
            raise TypeError('Is not a Color instance')
        return Color(
            min(255, self.red_level + other.red_level),
            min(255, self.green_level + other.green_level),
            min(255, self.blue_level + other.blue_level)
        )

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            if 0 <= other and other <= 1:
                return Color(
                    decrease_level(self.red_level, other),
                    decrease_level(self.green_level, other),
                    decrease_level(self.blue_level, other)
                )

    __rmul__ = __mul__

    def __hash__(self):
        return hash((self.red_level, self.green_level, self.blue_level))


class HSLColor(ComputerColor):
    def __init__(self, hue: int, saturation: int, lightness: int) -> None:
        self.hue = hue
        self.saturation = saturation
        self.lightness = lightness

    def __repr__(self) -> str:
        return '\033[1;38;2;0;0;0m●\033[0m'

    def __mul__(self, other) -> str:
        if isinstance(other, float) or isinstance(other, int):
            if 0 <= other and other <= 1:
                return self

    __rmul__ = __mul__


def decrease_level(source_level, c):
    cl = -256 * (1 - c)
    F = (259 * (cl + 255)) / (255 * (259 - cl))
    return int(F * (source_level - 128) + 128)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] *
        3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] *
        7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] *
        9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)

    list_of_colors = [red, orange1, green, orange2]
    print(list_of_colors)
    set_of_colors = set(list_of_colors)
    print(set_of_colors)

    print(0.5 * red)

    print_a(green)

    hsl = HSLColor(352, 122, 55)
    print(hsl*0.5)

    print(0.5 * hsl)
    print('----')
    print_a(hsl)
