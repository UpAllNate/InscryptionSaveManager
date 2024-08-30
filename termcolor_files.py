from termcolor import colored
import colorama
from enum import Enum

class Color(Enum):
    BLACK = 'black'
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'
    BLUE = 'blue'
    MAGENTA = 'magenta'
    CYAN = 'cyan'
    WHITE = 'white'
    LIGHT_GREY = 'light_grey'
    DARK_GREY = 'dark_grey'
    LIGHT_RED = 'light_red'
    LIGHT_GREEN = 'light_green'
    LIGHT_YELLOW = 'light_yellow'
    LIGHT_BLUE = 'light_blue'
    LIGHT_MAGENTA = 'light_magenta'
    LIGHT_CYAN = 'light_cyan'

class Attribute(Enum):
    BOLD = 'bold'
    DARK = 'dark'
    UNDERLINE = 'underline'
    BLINK = 'blink'
    REVERSE = 'reverse'
    CONCEALED = 'concealed'

# Initialize colorama for cross-platform support
colorama.init()


def color_text(text, color, on_color=None, *, attrs=None) -> str:
    color_value = color.value if isinstance(color, Color) else color
    on_color_value = f"on_{on_color.value}" if isinstance(on_color, Color) else on_color
    # Manage whether attrs is a single Attribute or a list of Attributes
    if attrs is not None:
        if isinstance(attrs, Attribute):
            attr_values = [attrs.value]
        elif isinstance(attrs, list) and all(isinstance(attr, Attribute) for attr in attrs):
            attr_values = [attr.value for attr in attrs]
        else:
            attr_values = []
    else:
        attr_values = []

    return colored(text, color=color_value, on_color=on_color_value, attrs=attr_values)

def color_text_numbers(text : str) -> str:
    return color_text(text, color= Color.LIGHT_BLUE, on_color= None, attrs= [])

def color_text_object_description(text : str) -> str:
    return color_text(text, color= Color.GREEN, on_color= None, attrs= [])

def color_text_sequence_description(text : str) -> str:
    return color_text(text, color= Color.WHITE, on_color= None, attrs= [])

def color_text_tag_name(text : str) -> str:
    return color_text(text, color= Color.MAGENTA, on_color= None, attrs= [])

def color_text_alarm_name(text : str) -> str:
    return color_text(text, color= Color.LIGHT_YELLOW)

def color_text_word_Alarm(text : str) -> str:
    return color_text(text, color= Color.LIGHT_YELLOW)

def color_text_word_Sequence(text : str) -> str:
    return color_text(text, color= Color.LIGHT_MAGENTA)

if __name__ == "__main__":

    import inspect

    test_text = "Testing color output"
    print(test_text)

    # Call each method with the test text
    for color in Color:

        print(f"{color.name}: {color_text(test_text, color= color)}")

    print("\n\n        BOLD         \n\n")

    for color in Color:

        print(f"{color.name} bold: {color_text(test_text, color= color, attrs= [Attribute.BOLD])}")

    print("\n\n        UNDERLINE         \n\n")

    for color in Color:

        print(f"{color.name} underline: {color_text(test_text, color= color, attrs= [Attribute.UNDERLINE])}")

    print("\n\n        BOLD UNDERLINE         \n\n")

    for color in Color:

        print(f"{color.name} bold underline: {color_text(test_text, color= color, attrs= [Attribute.BOLD, Attribute.UNDERLINE])}")

    print("\n\n        ON COLOR         \n\n")

    for color in Color:
        for on_color in Color:

            print(f"{color.name} on {on_color.name}: {color_text(test_text, color= color, on_color= on_color,)}")