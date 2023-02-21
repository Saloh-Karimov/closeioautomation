import pytesseract
# from mss import mss
import numpy as np
import cv2
import time
import pyautogui
import sys
import mss.tools

# The coordinates for the region to take a screenshot of
x, y, width, height = 1585, 67, 94, 36

# detected text
text1 = "Invite"

# positions to click
pos_a = (360, 250)
pos_b = (1547, 315)
pos_c = (777, 555)
pos_d = (1555, 375)
pos_e = (755, 1008)
pos_h = (287, 26)

# hotkeys
call = ["command", "shift", "d"]
end_call = ["command", "."]
sms = ["command", "shift", "k"]
email = ["command", "shift", "e"]

while True:
    # Click on pos_a
    time.sleep(2)
    pyautogui.click(pos_a)
    time.sleep(4)

    # Click call
    pyautogui.hotkey(*call)
    time.sleep(19)

    # Take screenshot of roi1
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = np.array(sct.grab(monitor))

    # Convert the screenshot to grayscale and then to text using pytesseract
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    # If text1 is found, end script
    if text1 in text:
        sys.exit()

    else:
        pyautogui.hotkey(*end_call)
        time.sleep(2)
        pyautogui.hotkey(*call)
        time.sleep(18)

    # Take screenshot of roi1 and check for text1
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = np.array(sct.grab(monitor))

    # Convert the screenshot to grayscale and then to text using pytesseract
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    # If text1 is found, end script
    if text1 in text:
        sys.exit()

    else:
        pyautogui.hotkey(*end_call)
        time.sleep(5)

    # Click sms and wait for 2 seconds
    pyautogui.hotkey(*sms)
    time.sleep(2)

    # Click pos_b
    pyautogui.click(pos_b)
    time.sleep(2)

    # Type "Sa", press enter, and wait 2 seconds
    pyautogui.typewrite("Sa")
    pyautogui.press("enter")
    time.sleep(2)

    # Click on pos_c and wait for 2 seconds
    pyautogui.click(pos_c)
    time.sleep(2)

    # Click email and wait for 2 seconds
    pyautogui.hotkey(*email)
    time.sleep(3)

    # Click on pos_d
    pyautogui.click(pos_d)

    # Type "Sal", press enter, and wait 2 seconds
    pyautogui.typewrite("Sal")
    pyautogui.press("enter")
    time.sleep(2)

    # Click on pos_e and wait for 2 seconds
    pyautogui.click(pos_e)
    time.sleep(2)

    # Click on pos_f and wait for 4 seconds
    pyautogui.click(pos_h)
    time.sleep(4)
