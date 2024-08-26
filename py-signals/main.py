#!/usr/bin/python3

import signal
import time
import sys

done = False


def term_handler(signum, frame):
    print("Termination requested")
    print("Performing cleanup...")
    sys.exit(100)


def int_handler(signum, frame):
    print("Why you try interrupt me😿")


def alarm_handler(signum, frame):
    global done
    done = True
    signal.alarm(0)


# signal.signal(signal.SIGINT, int_handler)
signal.signal(signal.SIGTERM, term_handler)
signal.signal(signal.SIGALRM, alarm_handler)

time_limit = 3
signal.alarm(time_limit)

counter = 1
while not done:
    print(counter**4)
    counter += 1

print("Counter reached")
