# rpi-gpio-toggle
A python app that used to toggle GPIO pins on a Raspberry Pi using GPIO's LED functions.
Now the app is using PiGPIO instead.
Feel free to go back a few commits and try to make it work with GPIOZero.

# Notes
Your Pi must have the IP adress of `192.168.2.153`, unless you modify it in the code. You can change the IP near the top of the script, at the `Variable Decleration` area.
This app only has two buttons for two states: On and off. Feel free to fork the script to add more, or submit pull requests.
