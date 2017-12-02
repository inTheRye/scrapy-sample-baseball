# -*- coding: utf-8 -*-
import scrapy

from space_object.spiders import CATEGORY
import math
from sgp4.earth_gravity import wgs84
from sgp4.io import twoline2rv
from space_object.items import TwoLineElementItem


class TwoLineElementSpider(scrapy.Spider):
    name = 'tle'
    allowed_domains = ['www.celestrak.com']
    URL_TEMPLATE = 'https://www.celestrak.com/NORAD/elements/{category}'

    def __init__(self, *args, **kwargs):
        """
        初期処理(CATEGORY毎のURLを設定)
        """
        self.start_urls = [self.URL_TEMPLATE.format(category=c) for c in CATEGORY]

    def parse(self, response):
        """
        TLEと付加情報を解析し、Itemに入れる。
        :param response: 取得した結果(Response)
        :return: TLE+付加情報
        """
        GM = 3.9860044188e+14  # gravitational constant and the mass of Earth
        Re = 6378137.0         # Earth Radius (m)
        tle = response.body.decode("utf-8")

        item = TwoLineElementItem()

        tle_array = tle.split("\n")

        for n in range(len(tle_array)-1)[::3]:

            soname = tle_array[n:n+3][0]
            line1 = tle_array[n:n+3][1]
            line2 = tle_array[n:n+3][2]

            sat = twoline2rv(line1, line2, wgs84)

            sma = (GM/((sat.no/60)**2))**(1/3)
            perigee = sma*(1-sat.ecco)
            apogee = sma*(1+sat.ecco)
            altitude = (perigee+apogee)/2 - Re

            item['soname'] = soname.strip()
            item['satnum'] = sat.satnum
            item['jdsatepoch'] = sat.jdsatepoch
            item['epoch'] = sat.epoch
            item['bstar'] = sat.bstar
            item['inclo'] = (180.0/math.pi)*sat.inclo
            item['nodeo'] = (180.0/math.pi)*sat.nodeo
            item['ecco'] = sat.ecco
            item['argpo'] = sat.argpo
            item['mo'] = (180.0/math.pi)*sat.mo
            item['no'] = (60*24/(2*math.pi))*sat.no
            item['sma'] = sma/1000
            item['perigee'] = perigee/1000
            item['apogee'] = apogee/1000
            item['altitude'] = altitude/1000
            yield item
