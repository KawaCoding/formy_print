
# formy_print V. 0.1.0

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
def formy_print(text,text_color='white',bg_color='none',text_format='none',reset=True):
    print(f'{format_codes[text_format]+text_color_codes[text_color]+bg_color_codes[bg_color]+text+format_reset}')
    
