import time
import pyautogui

def close_tabs(num_tabs_to_close):
    # Sleep for a few seconds to allow you to switch to your web browser
    print("Switch to your web browser within the next 5 seconds...")
    time.sleep(5)

    # Perform the closing of tabs
    for _ in range(num_tabs_to_close):
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(0.5)  # Add a small delay between closing tabs

if __name__ == "__main__":
    num_tabs_to_close = 10  # Adjust the number of tabs to close as needed
    close_tabs(num_tabs_to_close)
