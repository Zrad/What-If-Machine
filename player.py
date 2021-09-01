import os

os.system("clear > /dev/tty1") #clear any text on the Pi's screen so it is blank between episodes
os.system("while true; do omxplayer --orientation 180 -o local $(ls /home/pi/futurama/videos/* | shuf | head -n1); done") #indefinitely play Futurama episodes on Omxplayer, flipped 180 degrees and outputting on headphone jack)
