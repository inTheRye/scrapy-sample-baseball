# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TwoLineElementItem(Item):
    soname = Field()      # common space object name
    satnum = Field()      # satellite catalog number
    jdsatepoch = Field()  # epoch in Julian date
    epoch = Field()       # epoch in UTC
    bstar = Field()       # B Star
    inclo = Field()       # inclination
    nodeo = Field()       # right ascension of ascending node
    ecco = Field()        # eccentricity
    argpo = Field()       # argument of perigee
    mo = Field()          # mean anomaly
    no = Field()          # mean motion
    sma = Field()         # Semi-major axis
    apogee = Field()      # apogee
    perigee = Field()     # perigee
    altitude = Field()    # altitude
