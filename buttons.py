from gpiozero import Button
from signal import pause
import os

Button.was_held = False
Random = True
os.system("sudo systemctl start tvplayer.service")
os.system("clear > /dev/tty1")

def held(btn):
    btn.was_held = True
    os.system("sudo systemctl stop tvplayer.service")
    os.system("sudo systemctl restart hypnotoad.service")

def released(btn):
    if not btn.was_held:
        pressed()
    btn.was_held = False

def pressed():
    random = True
    os.system("sudo systemctl stop hypnotoad.service")
    os.system("sudo systemctl restart tvplayer.service")

btn = Button(12)

btn.when_held = held
btn.when_released = released

pause()
