#!/usr/bin/python3

import signal
import time
import sys


def term_handler(signum, frame):
    print("Termination requested")
    print("Performing cleanup...")
    sys.exit(100)


def int_handler(signum, frame):
    print("Why you try interrupt me😿")


signal.signal(signal.SIGINT, int_handler)
signal.signal(signal.SIGTERM, term_handler)

while True:
    print("hey")
    time.sleep(1)
