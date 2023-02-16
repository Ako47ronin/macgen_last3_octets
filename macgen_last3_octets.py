#!/usr/bin/env python3

import argparse
import itertools
import signal
import sys

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
Email : ako47ron at gmail.com
"""

def generate_mac_last_three_octets():
    """
    Generates all possible last three octets of a MAC address.

    Returns:
        A list of strings representing the last three octets of a MAC address.
    """
    octets = []
    for i in range(256):
        for j in range(256):
            for k in range(256):
                octet_str = f"{i:02X}:{j:02X}:{k:02X}"
                octets.append(octet_str)
    return octets

def signal_handler(sig, frame):
    """
    Handles the keyboard interrupt signal.

    Args:
        sig: The signal number.
        frame: The current stack frame.
    """
    print("Keyboard interrupt detected. Exiting...")
    sys.exit(0)

print(banner)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Generate all possible last three octets of a MAC address.")
parser.add_argument("-d", "--delimiter", type=str, default="", help="The delimiter to use between octets. Defaults to no delimiter.")
parser.add_argument("-o", "--output", type=str, help="The filename to write output to. If not specified, output is printed to screen.")
args = parser.parse_args()

# Set up keyboard interrupt signal handler
signal.signal(signal.SIGINT, signal_handler)

# Generate the last three octets
print("[+] Generating octects ..." + "\n")

try:
    octets = generate_mac_last_three_octets()
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting..." + "\n")
    sys.exit(0)

# Format the output with the specified delimiter
output = "\n".join([args.delimiter.join(octet.split(":")) for octet in octets])

# Write output to file or print to screen
if args.output is not None:
    with open(args.output, "w") as f:
        f.write(output)
    print(f"Output written to {args.output}")
else:
    print(output)
