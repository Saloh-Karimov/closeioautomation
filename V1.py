import pytesseract
import numpy as np
import cv2
import time
import pyautogui
import sys
import mss.tools
import pyperclip

# The coordinates for the region to take a screenshot of
x, y, width, height = 1585, 67, 94, 36

# detected text
text1 = "Invite"

# positions to click
pos_a = (360, 250)
pos_b = (1400, 250)
pos_c = (783, 486)
pos_d = (1555, 375)
pos_e = (755, 1008)
pos_h = (287, 26)

# hotkeys
call = ["command", "shift", "d"]
end_call = ["command", "."]
sms = ["command", "shift", "k"]
email = ["command", "shift", "e"]
refresh = ["command", "r"]

while True:
    # move the mouse to the specified coordinates and right-click
    pyautogui.moveTo(515, 250)
    pyautogui.click(button='right')

    # select the "Copy Phone Number" option
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.sleep(0.5)

    # paste the copied phone number and extract the area code
    copied_text = pyperclip.paste()
    area_code = copied_text[2:5]
    ca_area_codes = ['368', '403', '587', '780', '825', '250', '778', '236', '604', '672', '204', '431', '584', '506',
                     '709', '867', '902', '782', '867', '249',
                     '613', '683', '753', '807', '343', '519', '705', '226', '437', '548', '647', '905', '289', '365',
                     '416', '742', '782', '902', '367', '418',
                     '450', '514', '581', '873', '468', '819', '263', '354', '438', '579', '306', '639', '474', '867']

    # if area_code in ca_area_codes, select Canadian phone number, otherwise select US phone number
    if area_code in ca_area_codes:
        print("CA number")
        pyautogui.click(1810, 26)
        time.sleep(0.5)
        pyautogui.click(1666, 166)
        time.sleep(0.5)
        pyautogui.press('up')
        pyautogui.press('enter')

    else:
        print("US number")
        pyautogui.click(1810, 26)
        time.sleep(0.5)
        pyautogui.click(1666, 166)
        time.sleep(0.5)
        pyautogui.press('up')
        pyautogui.press('down')
        pyautogui.press('enter')

    # Click on the lead
    time.sleep(1)
    pyautogui.click(pos_a)
    time.sleep(4)

    # Dial
    pyautogui.hotkey(*call)
    time.sleep(21)

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
        time.sleep(21)

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
        time.sleep(1)

    # Click sms and wait for 2 seconds
    pyautogui.hotkey(*refresh)
    time.sleep(5)
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
    time.sleep(2)

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
