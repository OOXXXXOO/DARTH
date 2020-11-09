import os 
import sys
sys.path.append("/Users/winshare/workspace/DARTH/")

from darth.downloader import downloader
Google=downloader("Google China")
Google.add_cord(116.3, 39.9, 116.6, 39.7, 13)# WGS Lonlat Form
Google.download()
tiles=[i["path"] for i in Google.result]
from darth.vector import Vector
Building=Vector("osm-2017-07-03-v3.6.1-china_beijing.mbtiles")
Building.getDefaultLayerbyName("building")
Building.crop_default_layer_by_rect(Google.mercator_cord)#FILTER to speed up
label=Building.generate(tiles)