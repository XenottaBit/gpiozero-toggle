# Imports
# ------------------------------------

import tkinter as tk
from gpiozero import LED as PIN, OutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
# ====================================
# Variable Decleration
# ------------------------------------
device = OutputDevice() #GPIO Pin Output Device
# ====================================
# Window Creation
# ------------------------------------
#Create Window Instance


win = tk.Tk()
#Add Window Title
win.title("GPIO Pin Toggle")
#Add Title and Position it
lbl = tk.Label(win, text="GPIO Pin Toggling", font=("Helvetica", 15))
lbl.grid(column=0, row=0)

#Create Textbox to Specify Pin Number
txt = tk.Entry(win, width=3)
txt.grid(column=0, row=1)
txt.insert(0, "Pin")

#Set Status
statusvar = tk.StringVar()
statusvar.set("Pin Status Shown Here")
#Display Pin Status
statuslbl = tk.Label(win, textvar = statusvar, font=("Helvetica", 7))
statuslbl.grid(column=0, row=4)

# ====================================
# Button Events
# ------------------------------------
# Pin Factory Configuration
factory = PiGPIOFactory(host='192.168.2.153')

# On event
def pinenable():
    PinID = int(txt.get())
    device = OutputDevice(PinID)
    device.on()
    statusvar.set("Pim " + txt.get() + " Has Been Raised")

# Off event
def pindisable():
    PinID = int(txt.get())
    device = OutputDevice(PinID)
    device.on()
    statusvar.set("Pim " + txt.get() + " Has Been Lowered")

# ====================================

#Set up on button
btn = tk.Button(win, text="Raise pin", command=pinenable, width=25, height=3)
btn.grid(column=0, row=2)
#Set up off button
btn = tk.Button(win, text="Lower pin", command=pindisable, width=25, height=3)
btn.grid(column=0, row=3)



#Start GUI/ Create Main Loop
win.mainloop()


