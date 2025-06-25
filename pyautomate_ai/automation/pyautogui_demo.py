import pyautogui
import time
import os

def main():
    print('Moving mouse to (100, 100)')
    pyautogui.moveTo(100, 100, duration=1)
    time.sleep(1)
    screenshot_path = os.path.join(os.path.dirname(__file__), 'desktop_screenshot.png')
    pyautogui.screenshot(screenshot_path)
    print(f'Screenshot saved to {screenshot_path}')

if __name__ == '__main__':
    main() 