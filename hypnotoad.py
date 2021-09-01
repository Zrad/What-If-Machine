import os

os.system("clear > /dev/tty1") #clear any text on the Pi's screen so it is blank between episodes
os.system("omxplayer --orientation 180 -o local /home/pi/futurama/videos/FuturamaS00e04.m4v") #Play the Hypnotoad episode, flip screen 180 degrees and output to headphone jack
