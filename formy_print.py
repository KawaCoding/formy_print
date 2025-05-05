
# formy_print V. 0.1.1
"""
A simple module to style text in terminal output. It uses ANSI code to choose between 8 different colors,
background colours and format.

"""
import os

__version__ = '0.1.0'

# Enable ANSI support on Windows
if os.name == 'nt':
    os.system('')


# Stores the ANSI code for the format reset
format_reset = '\033[0m'
# Stores the ANSI code for the text format
format_codes = {
    'none': '\033[0m',
    'bold' : '\033[1m',
    'dim' : '\033[2m',
    'italic' : '\033[3m',
    'underline' : '\033[4m',
    'blink' : '\033[5m',
    'reverse' : '\033[7m',
    'strike' : '\033[9m'
}
# Stores the ANSI code for text colors
text_color_codes = {
    'black' : '\033[30m',
    'red' : '\033[31m',
    'green' : '\033[32m',
    'yellow' : '\033[33m',
    'blue' : '\033[34m',
    'magenta' : '\033[35m',
    'cyan' : '\033[36m',
    'white' : '\033[37m'
}
# Stores the ANSI code for background colors
bg_color_codes = {
    'black' : '\033[40m',
    'red' : '\033[41m',
    'green' : '\033[42m',
    'yellow' : '\033[43m',
    'blue' : '\033[44m',
    'magenta' : '\033[45m',
    'cyan' : '\033[46m',
    'white' : '\033[47m',
    'none':'\033[49m'
}
# Defines the main function
def formy_print(text,text_color='white',bg_color='none',text_format='none'):
    """
    Prints styled text to the terminal using ANSI escape codes
    Args:
    
    text (str): The text to be printed
    text_color (str): black, red, green, yellow, blue, magenta, cyan, white. Default is white. 
    bg_color (str): black, red, green, yellow, blue, magenta, cyan, white. Default is none.
    text_format (str): none, bold, dim, italic, underline, blink, reverse, strike. Default is none.  
    
    """
    if text_color not in text_color_codes:
        raise ValueError(
            f"Invalid text color: {text_color_codes['yellow']}'{text_color}'{format_reset}."
            f' Choose from {list(text_color_codes.keys())}'
        )
    if bg_color not in bg_color_codes:
        raise ValueError(
            f"Invalid background color: {text_color_codes['yellow']}'{bg_color}'{format_reset}."
            f' Choose from {list(bg_color_codes.keys())}'
        )
    if text_format not in format_codes:
        raise ValueError(
            f"Invalid format: {text_color_codes['yellow']}'{text_format}'{format_reset}."
            f' Choose from {list(format_codes.keys())}'
        )
    
    print(f'{format_codes[text_format]+text_color_codes[text_color]+bg_color_codes[bg_color]+text+format_reset}')
    
if __name__ == '__main__':
    formy_print('I LOVE YOU', 'red', 'white', 'none')
    
    
    
    