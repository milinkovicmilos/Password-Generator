# Password-Generator
Application for generating random passwords with Graphical User Interface made with Tkinter.

# Requirements
1. Python (tested on 3.11.0)
2. PyAutoGUI (for getting mouse position on screen)

# Usage
Application is started by running pwgenerator.py.
First user needs to select characters that are gonna be used in password.
After that user should provide desired length of password.
After that Password can be created in two ways:
  1. By using time based pseudo-randomness
  2. By inputing mouse position thats going to be used as seed every 50ms

Generated password will appear in box below two buttons.
User can copy the generated password to clipboard by clicking the button below it.
User can also choose to hide the generated password. In this case every character will be represented as '*' (asterisk).
