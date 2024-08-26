#!/usr/bin/python3

import signal
import time


def signal_handler(signum, frame):
    print("Why you try interrupt me")


signal.signal(signal.SIGINT, signal_handler)

while True:
    print("hey")
    time.sleep(1)
