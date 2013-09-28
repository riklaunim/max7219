MAX7219 Library for pyMCU
==============

ported from Raspberry Pi MAX7219 driver
---------------------------------------


Interfacing LED matrix displays with the MAX7219 driver in Python for pyMCU.
The particular kit I bought can be acquired for a few pounds from 
http://www.banggood.com/MAX7219-Dot-Matrix-Module-DIY-Kit-SCM-Control-Module-For-Arduino-p-72178.html?currency=GBP 

Examples
--------
Run the example code as follows:

    sudo python setup.py install
    sudo python examples/test.py


ToDo
----
- refactor led.py to not require a global own pymcu instance.

License
-------
This code is a fork of https://github.com/rm-hull/max7219 designed for Raspberry Pi

Portions of this code are derived from https://github.com/lthiery/SPI-Py
which includes the following license notice:

> COPYRIGHT (C) 2012 Louis Thiery. All rights reserved. 
Further work by Connor Wolf.

> This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License V2 as published by the 
Free Software Foundation.

> LIABILITY
>This program is distributed for educational purposes only and is no way 
suitable for any particular application, especially commercial. There is
no implied suitability so use at your own risk!
