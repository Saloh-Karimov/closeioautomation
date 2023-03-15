This is the update to my first Python script, that uses pytesserac, numpy, opencv-python, PyAutoGUI, mss and pyperclip to automate the outbound calling process in close.io CRM.

Here's a list of what I got the script to do:

Copy phone number of lead
If phone number is Canadian, select Canadian phone number to dial, otherwise select US phone number
Select the latest lead who opted in in a smart view
Dial and wait for 21 seconds while it dials and rings
Take a screenshot of a certain region
Convert it to grayscale and then to text using pytesseract. This is because pytesseract works better with greyscale images.
An option to "Invite" others onto the call is displayed if a lead picks up the call. So if it does'nt detect text1 (Invite) from that screenshot using pytesseract, end the call. If detected, end the script.
Dial again and wait for 18 seconds while it dials and rings
Take a screenshot of the same region
Convert it to grayscale and then to text using pytesseract.
If text1 is not detected, end the call. If detected, end the script.
SMS the lead by choosing the right template
Email the lead by choosing the right template
Go back to the beginning and repeat
