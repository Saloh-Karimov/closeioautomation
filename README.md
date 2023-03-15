# closeioautomation

This is the update to my first Python script, that uses pytesserac, numpy, opencv-python, PyAutoGUI, mss and pyperclip to automate the outbound calling process in close.io CRM.

Here's a list of what I got the script to do:

1. Copy phone number of lead
2. If phone number is Canadian, select Canadian phone number to dial, otherwise select US phone number
3. Select the latest lead who opted in in a smart view
4. Dial and wait for 21 seconds while it dials and rings
5. Take a screenshot of a certain region
6. Convert it to grayscale and then to text using pytesseract. This is because pytesseract works better with greyscale images.
7. An option to "Invite" others onto the call is displayed if a lead picks up the call. So if it does'nt detect text1 (Invite) from that screenshot using pytesseract, end the call. If detected, end the script.
8. Dial again and wait for 18 seconds while it dials and rings
9. Take a screenshot of the same region
10. Convert it to grayscale and then to text using pytesseract.
11. If text1 is not detected, end the call. If detected, end the script.
12. SMS the lead by choosing the right template
13. Email the lead by choosing the right template
14. Go back to the beginning and repeat
