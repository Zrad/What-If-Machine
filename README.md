# What-If-Machine
Raspberry Pi-Powered What-If machine

This project is for this post where I made a TV that plays Futurama tv episodes based on a button press. It is based on a Raspberry Pi 3 B+, a [CTRONICS 3.5" Screen](https://www.amazon.com/gp/product/B076M399XX/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1), a [DROK Mini Amplifier](https://www.amazon.com/gp/product/B077MKQJW2/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1), two [40 mm speakers](https://www.amazon.com/gp/product/B01LN8ONG4/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1), a [Micro USB breakout board](https://www.amazon.com/gp/product/B07VYZ2NDZ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1), and some various lengths of wire.

The left button is wired to the switch on the display which either toggles it on/off or will adjust brightness. The right button cycles randomly through Futurama episodes. The crank is attached to the audio amp and controls the volume.

There are three services to create, but only the buttons.service will start at boot. The other two are started and stopped depending on the button presses in the buttons.py script.

Link to the 3D printed files: [Thingiverse link](https://www.thingiverse.com/thing:4946494)

Link to more images: [Imgur link](https://imgur.com/gallery/OVnPsT3)

![image](https://user-images.githubusercontent.com/47491287/131703200-dfcf3027-22c8-43ea-9635-09dc7be422cd.png)
