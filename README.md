**FormyPrint** is a Python module designed to enhance terminal output with customizable text formatting, colors, and background colors using ANSI escape codes. This module allows you to create styled text output for your terminal applications.

# Features

- Customizable text format (bold, italic, underline, etc.)
- Text color and background color options
- Easy-to-use function for styled text output

# Requirements

- Python 3.x

# Installation

1. **Save the Code:**

   Save the provided code snippet into a file named `formy_print.py`.
   
3. Import the Module:

In your Python script, import the formy_print function from formy_print.py
  from formy_print import formy_print

# Usage

The formy_print function allows you to print styled text to the terminal. You can customize the text color, background color, and text format by passing parameters to the function.
Function Signature:

  formy_print(text, text_color='white', bg_color='none', text_format='none', reset=True)

# Parameters:

  text (str): The text you want to print.

  text_color (str): The color of the text. Options: 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'. Default is 'white'.

  bg_color (str): The background color of the text. Options: 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'none'. Default is 'none'.

  text_format (str): The format of the text. Options: 'none', 'bold', 'dim', 'italic', 'underline', 'blink', 'reverse', 'strike'. Default is 'none'.

  reset (bool): Whether to reset the formatting after printing. Default is True.

# Examples:

## Print bold red text on a yellow background
  formy_print("Bold Red Text", text_color='red', bg_color='yellow', text_format='bold')

## Print underlined blue text with no background
  formy_print("Underlined Blue Text", text_color='blue', bg_color='none', text_format='underline')

## Print default text with no formatting
  formy_print("Normal Text")

# Contributing

Feel free to fork the repository, make changes, and create pull requests. Contributions are welcome!
License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Thanks to the developers of ANSI escape codes for providing the foundation for terminal text formatting!
