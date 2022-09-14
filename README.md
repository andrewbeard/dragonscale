# Dragonscale
Super-simple die rolling firmware for the BBC micro:bit single board computer.

Once upon a time there was an odd little product called the [Dragonbone](https://rpggeek.com/rpgitem/71769/dragonbone-electronic-dice), an electronic die roller built in the 80s. A number of people expressed a sense of nostalgia about the Dragonbone, and wished someone would start making them again.

I'm not going to do that.

What I can do is offer some quick and dirty software to make a BBC micro:bit fill the same roll as the Dragonbone without the 1983 LED interface. Instead we have a brand-spanking new 2022 LED interface! It's also a lot smaller, and not really bone shaped any more. With some creative license I'm going to call it scale shaped, though.

## Installation
If you're familiar with the BBC micro:bit you can take the main.py file and build it into an apopropriate hex file for flashing on the micro:bit. Otherwise you're probably better off looking at the releases section and grabbing the latest pre-build hex file. Plugging you micro:bit into a computer brings up a drive that you can just copy the hex file to, in stalling the die rolling firmware.

## Using the Dragonscale
![](https://cdn.sanity.io/images/ajwvhvgo/production/4cfb4a0c22aa25164ba6f5f9cb4ae2d53cbf35ba-2577x1068.png)

So the micro:bit has a really simple interface with a matrix of LEDs flanked on either side by a button. Hitting the left button ("A") cycles through the available die sizes and displays the current die size scrolling across the LEDs. Be aware that the Dragonscale supports the entire [Dungeon Crawl Classics](https://goodman-games.com/dungeon-crawl-classics-rpg/) dice chain, so there may be a couple in there you're not used to if you normally think of the standard set of 7 polyhedrals. The right button ("B") rolls the currently selected die size and scrolls the result across the LEDs. That's pretty much it. You can also shake the device to trigger a roll; it will display a "?" on the LEDs just so you know you've triggered a roll but will not start scrolling the result until you stop. During testing there were a couple times I really got in to shakin g the board and by the time I stopped half my die result was already off the screen.