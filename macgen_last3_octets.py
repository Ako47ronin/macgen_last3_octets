#!/usr/bin/env python3

import argparse

# Banner and ASCII art logo
banner = """

⠀⠀⠀⠀⠀⠀⢠⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⢹⠀⠀⠀⠀⢠⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣼⡀⠀⣀⣤⣶⡴⠒⠒⠒⠒⠒⠠⣤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣃⣗⣿⠇⣿⣧⡃⠀⠀⠀⠀⠀⠀⠀⠹⣾⠱⠤⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡰⠋⢸⢾⣿⢣⣿⣿⠷⣄⡒⢤⣀⣀⠀⢐⢀⠀⠦⠀⠉⢕⢄⠀⠀⠀⠀
⠀⠀⠀⡠⣎⣃⠀⠀⢟⣽⢸⣿⣿⡀⠱⣷⡾⣡⣦⣝⡀⠉⠘⠃⠠⠄⠀⢈⣧⡀⠀⠀
⠀⠀⠰⠁⢸⡟⠲⠀⢘⣜⣿⣿⡟⣉⣣⣼⣷⣻⣯⣙⣿⣿⣶⣶⣦⣴⣶⡿⠋⠱⡀⠀
⠀⠀⡸⠀⡀⠀⠀⠀⠠⡽⢟⣵⣾⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠱⠀
⠀⡇⡃⠀⢁⡀⠀⠀⠠⠷⢟⣿⣵⣶⣶⣇⣿⣿⣿⣟⣛⣛⠻⣯⠀⠀⠀⠀⠀⠀⠀⡇
⠀⢿⡃⠀⠈⠈⠀⠀⠀⠀⠃⢌⣿⣿⣿⣾⣿⣎⣋⣴⣶⣯⣿⣿⡆⠀⠀⠀⠀⠀⢠⢰
⢠⠸⢋⡀⡀⢀⣴⣮⠀⢀⡀⠀⣴⡿⠻⠘⠛⡟⡿⡬⢧⢊⡩⢿⣷⡀⠀⠀⠀⠀⠫⡞
⠘⣇⣇⢟⢶⠟⡉⠀⠀⠀⠁⣰⠊⢀⡀⣄⡰⣱⡷⡗⣭⢄⣐⠙⢿⡂⠠⠿⠇⠀⢀⡇
⠀⢟⡵⠈⣵⠀⠀⠀⠀⠀⠀⣷⢜⠊⣭⡴⢁⣽⡷⡖⣪⠴⢆⣉⣿⡇⠀⠀⠀⠘⡺⠀
⠀⠘⡜⣧⠘⠃⠀⠀⡐⠀⡼⡝⣮⣩⢴⣈⣿⣽⡇⡇⢼⠒⠬⣘⣿⡇⠀⠀⠀⣰⡅⠀
⠀⠀⠘⢌⢷⡔⠦⢀⣈⢠⡓⣭⣰⡴⣽⡽⢿⠍⡿⠏⠇⠒⠡⣽⣟⡅⠀⠀⣼⡟⠀⠀
⠀⠀⠀⠈⠢⣸⣾⣿⠟⣹⣭⣾⠷⣛⢭⣻⣿⣿⣷⣶⣴⣦⣬⣼⣿⣆⠈⡠⠊⠀⠀⠀
⠀⠀⠀⠀⣀⣈⣫⡼⡿⣟⢬⡢⣝⣮⣵⣿⣿⣿⣿⣿⣿⣿⣷⡉⠻⡧⠊⠁⠀⠀⠀⠀
⠀⠀⢠⢖⢧⣛⣛⣛⣾⣾⣷⡿⣟⣋⣽⣿⣿⣿⣿⣿⣯⣿⠼⠓⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⠿⢼⣸⡽⠿⠿⢯⣯⣻⣘⣯⡟⢿⣿⢿⣿⣿⣷⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡭⣿⣿⣿⣿⣿⣿⣯⣾⣟⡋⡓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡌⢀⣀⠘⠳⠙⣽⣿⣿⣿⣧⣋⣙⢾⡷⠦⡄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⠉⠈⠃⠿⠟⠉⢹⠟⠛⠻⡞⠿⠏⠀⠘⠄⠀⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        

Password Generator v1.0
Author: Ako
Email : ako47ron@gmail.com
"""

def generate_mac_last_three_octets(delimiter=""):
    """
    Generates all possible last three octets of a MAC address.

    Args:
        delimiter (str): The delimiter to use between octets. Defaults to no delimiter.

    Returns:
        A list of strings representing the last three octets of a MAC address.
    """
    octets = []
    for i in range(256):
        octets.append(f"{i:02X}")
    return octets

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Generate all possible last three octets of a MAC address.")
parser.add_argument("-d", "--delimiter", type=str, default="", help="The delimiter to use between octets. Defaults to no delimiter.")
parser.add_argument("-o", "--output", type=str, help="The filename to write output to. If not specified, output is printed to screen.")
args = parser.parse_args()

# Run program

print(banner)

octets = generate_mac_last_three_octets(args.delimiter)
output = ""
for i in range(0, len(octets), 3):
    output += args.delimiter.join(octets[i:i+3]) + "\n"

if args.output is not None:
    with open(args.output, "w") as f:
        f.write(output)
else:
    print(output)
