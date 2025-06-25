from selenium import webdriver
import time
import os

def main():
    driver = webdriver.Chrome()
    try:
        driver.get('https://example.com')
        time.sleep(2)
        screenshot_path = os.path.join(os.path.dirname(__file__), 'example_screenshot.png')
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot saved to {screenshot_path}')
    finally:
        driver.quit()

if __name__ == '__main__':
    main() 