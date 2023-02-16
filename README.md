## **Mac Address Last 3 Octect Generator**


A simple script to generate all the possible last three octects of a mac address. This is a simple helper script for OUI manipulations and testing. 

Possible Use Cases:

1. OUI Testing

2. Wireless Devices Discovery - Just append the manufacturer OUI
   
   Bluetooth Discovery
   
   Wifi Discovery 
   

# generate_mac_last_three_octets
The generate_mac_last_three_octets() function uses three nested loops to generate all possible combinations of the last three octets, and appends each combination to the octets list.

It generates all possible combinations of the last three octets from "00:00:00" to "FF:FF:FF":

**Reference**

For OUI List, please see: 
https://standards-oui.ieee.org/oui/oui.txt
