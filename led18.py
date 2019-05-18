#!/usr/bin/python3

# DWP Moonen
# connect a LED to gpio18
# led18.py <setup|on|off|status|close>

from time import sleep
import sys

LED = "18"
LED_PATH = "/sys/class/gpio/gpio18/"
SYSFS_DIR = "/sys/class/gpio/"
    
def writeLED(filename, value, path):
    fo = open(path + filename, "w")
    if fo.closed:
        print("file closed")
    else:
        print("file open")
    fo.write(value)
    sleep(0.5)
    fo.close()
    if fo.closed:
        print("file closed")
    else:
        print("file open")
    return

if len(sys.argv) !=2:
    print("cmd <arg>")

elif sys.argv[1] == "on":
    writeLED(filename="value", value="1", path=LED_PATH)

elif sys.argv[1] == "off":
    writeLED(filename="value", value="0", path=LED_PATH)

elif sys.argv[1] == "setup":
    writeLED(filename="export", value=LED, path=SYSFS_DIR)
    sleep(1)
    writeLED(filename="direction", value="out", path=LED_PATH)

elif sys.argv[1] == "status":
    fo = open(LED_PATH + "value", "r")
    if fo.closed:
        print("file closed")
    else:
        print("file open")
    print(fo.read(), end='')
    fo.close()
    if fo.closed:
        print("file closed")
    else:
        print("file open")

elif sys.argv[1] == "close":
    writeLED(filename="unexport", value=LED, path=SYSFS_DIR)
    print("Closing", end='', flush=True)
    print(" .", end='', flush=True)
    sleep(1)
    print(" .", end='', flush=True)
    sleep(1)
    print(" .", end='', flush=True)
    sleep(1)
    print("\n")

else:
    print("Invalid <argv[1]>")
    exit(1)
    
exit(0)


