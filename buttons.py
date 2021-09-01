from gpiozero import Button
from signal import pause
import os

Button.was_held = False
os.system("sudo systemctl start tvplayer.service") #starts the service to play episodes right away

def held(btn): #If the button is held, it will stop the normal TVPlayer service and start the Hypnotoad service
    btn.was_held = True
    os.system("sudo systemctl stop tvplayer.service")
    os.system("sudo systemctl restart hypnotoad.service")

def released(btn):
    if not btn.was_held:
        pressed()
    btn.was_held = False

def pressed(): #If the button was pressed, it will stop the Hypnotoad service and start the TVPlayer service
    os.system("sudo systemctl stop hypnotoad.service")
    os.system("sudo systemctl restart tvplayer.service")

btn = Button(12) #Defines the button on GPIO pin 12

btn.when_held = held
btn.when_released = released

pause()
