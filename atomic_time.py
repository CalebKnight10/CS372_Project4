# Caleb Knight
# CS 372
# Compare sys clock to atomic clock

import socket
import sys
import datetime

def nist_time():
	s = socket.socket()
	s.connect(("time.nist.gov", 37))
	
	message = s.recv(4096)
	s.close()
	
	hex_nist = int.from_bytes(message, "big")
	
	# print(mes)
	#print(f"{hex_nist:04x}")
	
	dec_nist = int('e6ef0607', 16)
	print("NIST time: ", dec_nist)
	# e6ef04f8
	# e6ef0607

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(datetime.datetime.now().strftime("%s"))
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta
    print("System time: ", seconds_since_1900_epoch)
    return seconds_since_1900_epoch
nist_time()
system_seconds_since_1900()