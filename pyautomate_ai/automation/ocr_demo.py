import pyautogui
import pytesseract
import os
import shutil

def find_tesseract():
    # Try to auto-detect Tesseract in PATH or default Windows location
    if shutil.which('tesseract'):
        return 'tesseract'
    win_default = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    if os.path.exists(win_default):
        return win_default
    return None

def main():
    tesseract_cmd = find_tesseract()
    if not tesseract_cmd:
        print('Tesseract not found! Please install it and add to PATH or install to C:\\Program Files\\Tesseract-OCR.')
        return
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    screenshot_path = os.path.join(os.path.dirname(__file__), 'ocr_screenshot.png')
    print('Taking screenshot for OCR...')
    pyautogui.screenshot(screenshot_path)
    print(f'Screenshot saved to {screenshot_path}')

    print('Extracting text from screenshot...')
    text = pytesseract.image_to_string(screenshot_path)
    print('Extracted text:')
    print(text)

if __name__ == '__main__':
    main() 