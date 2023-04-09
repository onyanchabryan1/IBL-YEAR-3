# This is a Python script that uses the `argparse`, `random`, `sys`, and `pyfiglet` modules to render
# text in ASCII art using different fonts. The script takes a command-line argument `-f` or `--font`
# to specify the font to use, or chooses a random font if no argument is provided. It then prompts the
# user to enter the text to be rendered, and uses the `pyfiglet` module to render the text in the
# chosen font. The resulting ASCII art is printed to the console.
import argparse
import random
import sys
import pyfiglet

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--font', help='specify font name')
args = parser.parse_args()

# Determine font to use
if args.font:
    font = args.font
    if font not in pyfiglet.FigletFont.getFonts():
        sys.exit("Error: Invalid font specified.")
else:
    font = random.choice(pyfiglet.FigletFont.getFonts())

# Get text input from user
text = input("Enter text to be rendered: ")

# Render text in chosen font
figlet = pyfiglet.Figlet(font=font)
output = figlet.renderText(text)

print(output)
