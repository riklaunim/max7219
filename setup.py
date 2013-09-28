#!/usr/bin/env python

from distutils.core import setup,Extension
setup(
    name = "max7219",
    version = "0.0.1",
    author = "Piotr Malinski",
    author_email = "riklaunim@gmail.com",
    description = ("A small library to drive a MAX7219 LED serializer using SPI"),
    license = "GPLv2",
    keywords = "pyMCU led max7219",
    url = "https://github.com/riklaunim/max7219",
    packages=['max7219'],
)
