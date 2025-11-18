#!/usr/bin/env python3
import signal
import sys
import time


def signal_handler(signum, frame):
    print(f"Signal {signum} received.")

    print("Sleeping for 3 seconds.")
    time.sleep(15)
    print("Sleep done.")  # It has never gotten here.

    print("Exiting.")
    sys.stdout.flush()
    sys.exit(0)


def main():
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    print("Waiting for signal.")
    for i in range(300):
        if i % 10 == 0:
            print(f"Waiting for signal... {i} seconds")
        time.sleep(1)
    print("Signal not received.")
    sys.exit(1)


if __name__ == "__main__":
    main()
