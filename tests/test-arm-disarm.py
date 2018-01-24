#!/usr/bin/env python

"""test-send.py: Test script to send RC commands to a MultiWii Board."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2016 Altax.net"

__license__ = "GPL"
__version__ = "2"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

from pymultiwii import MultiWii
import time

if __name__ == "__main__":

    #board = MultiWii("/dev/tty.usbserial-AM016WP4")
    board = MultiWii("COM4") #更改成藍芽連接的COM
    try:
        board.arm()
        print ("Board is armed now!")
        print ("In 3 seconds it will disarm...")
        time.sleep(3)
        board.disarm()
        print ("Disarmed.")
        time.sleep(3)

    except Exception as error:
        print ("Error on Main: "+str(error))
