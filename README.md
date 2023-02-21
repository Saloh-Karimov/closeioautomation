# Close.io Automation

This is my first Python script, that uses pyautogui, pytesserect, mss.tools, numpy and open CV to automate the outbound calling process in close.io CRM. 

Here's a list of what I got the script to do:

1. Select the latest lead who opted in in a smart view
2. Dial and wait for 19 seconds while it dials and rings
3. Take a screenshot of a certain region
4. Convert it to grayscale and then to text using pytesseract. This is because pytesseract works better with greyscale images.
5. An option to "Invite" others onto the call is displayed if a lead picks up the call. So if it does'nt detect text1 (Invite) from that screenshot using pytesseract, end the call. If detected, end the script.
6. Dial again and wait for 18 seconds while it dials and rings 
7. Take a screenshot of the same region
8. Convert it to grayscale and then to text using pytesseract.
9. If text1 is not detected, end the call. If detected, end the script.
10. SMS the lead by choosing the right template
11. Email the lead by choosing the right template
12. Go back to the beginning and repeat
