```python

```


```python
import sys 
sys.path.append("/workspace/Darth/darth/")
sys.path.append("/workspace/Darth/")
```


```python
from darth.downloader import downloader
```


```python
Google=downloader("Google China",thread_count=8)
```

    # ---------------------------------------------------------------------------- #
    #                            MAP Production Toolkit                            #
    # ---------------------------------------------------------------------------- #
    # ---------------------- MAP Serverv Init Successful by ---------------------- #
    # ---------------------- Google China ---------------------------------------- #



```python
Google.add_cord(116.3, 39.9, 116.6, 39.7, 13)
Google.download()
```

    # -----WGS BoundingBox: (116.27325422704708, 39.90850398784923, 116.62506415757257, 39.67233079805734)
    # -----Mercator BoudingBox: (12943479.451629978, 4852655.222148937, 12982642.753946641, 4818439.909406773)
    # -----Total tiles number：8 X 7


      0%|          | 0/56 [00:00<?, ?it/s]

    # -----Url Queue size: 56


     88%|████████▊ | 49/56 [00:00<00:00, 30.20it/s]
    100%|██████████| 56/56 [00:00<00:00, 93877.31it/s]
    100%|██████████| 56/56 [00:00<00:00, 57.96it/s]

    # ===== Decode Downloading...
    # ------------------------------- Download Done ------------------------------ #
    
    # ===== Save description done Google China-Sun Jun 28 10:51:01 2020-(116.3, 39.9, 116.6, 39.7)-13.json


    



```python
tiles=[i["path"] for i in Google.result]
```


```python
from darth.vector import Vector
vecfile="/workspace/osm-2017-07-03-v3.6.1-china_beijing.mbtiles"
Building=Vector(vecfile)#3.7GB SQLite-MBTiles . The China Main Class Vector Object.

```

    # ---------------------------------------------------------------------------- #
    #                                Vector Toolkit                                #
    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #
    #                            TIFF process Toolkit                              #
    # ---------------------------------------------------------------------------- #
    # -----Class TIF init without filename
    # -----Valid vector format : mbtiles
    
    # ----------------------------- Meta Information ----------------------------- #
    # -----ZOOM_LEVEL : 14                                                         #
    # -----attribution : <a href="http://www.openmaptiles.org/" target="_blank">&co#
    # -----center : 116.4025,39.92,14                                              #
    # -----description : Extract from https://openmaptiles.org                     #
    # -----maxzoom : 14                                                            #
    # -----minzoom : 0                                                             #
    # -----name : OpenMapTiles                                                     #
    # -----pixel_scale : 256                                                       #
    # -----mtime : 1499626373833                                                   #
    # -----format : pbf                                                            #
    # -----id : openmaptiles                                                       #
    # -----version : 3.6.1                                                         #
    # -----maskLevel : 5                                                           #
    # -----bounds : 115.686,39.414,117.119,40.426                                  #
    # -----planettime : 1499040000000                                              #
    # -----basename : china_beijing.mbtiles                                        #
    # ----------------------------- Meta Information ----------------------------- #
    
    # -----Description :  /workspace/osm-2017-07-03-v3.6.1-china_beijing.mbtiles
    # -----LayerCount: 15
    # -----Layer : 0  LayerName :  water 
    # -----Layer : 1  LayerName :  waterway 
    # -----Layer : 2  LayerName :  landcover 
    # -----Layer : 3  LayerName :  landuse 
    # -----Layer : 4  LayerName :  mountain_peak 
    # -----Layer : 5  LayerName :  park 
    # -----Layer : 6  LayerName :  boundary 
    # -----Layer : 7  LayerName :  aeroway 
    # -----Layer : 8  LayerName :  transportation 
    # -----Layer : 9  LayerName :  building 
    # -----Layer : 10  LayerName :  water_name 
    # -----Layer : 11  LayerName :  transportation_name 
    # -----Layer : 12  LayerName :  place 
    # -----Layer : 13  LayerName :  housenumber 
    # -----Layer : 14  LayerName :  poi 
    # -----Extent: (12878106.611910647, 13037627.442217408, 4781148.214470335, 4928041.927030869)
    # -----Alread Load: /workspace/osm-2017-07-03-v3.6.1-china_beijing.mbtiles
    # -------------------------------- DEFINE DONE ------------------------------- #



```python
Building.getDefaultLayerbyName("building")
```

    # -----Set Default Layer | building | :  <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7f2def7f37b0> >





    <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7f2def7f37b0> >




```python
Building.crop_default_layer_by_rect(Google.mercator_cord)#FILTER to speed up
label=Building.generate(tiles)
```

      0%|          | 0/56 [00:00<?, ?it/s]

    # -----Set filter Rect: (12943479.451629978, 4852655.222148937, 12982642.753946641, 4818439.909406773)
    # ===== Start Generate.....


    100%|██████████| 56/56 [00:27<00:00,  2.03it/s]



```python
import tifffile as tif 
import matplotlib.pyplot as plt
image=tif.imread(tiles[1])
label=tif.imread(label[1])
plt.imshow(image),plt.show()
plt.imshow(label),plt.show()
```


![png](output_9_0.png)



![png](output_9_1.png)





    (<matplotlib.image.AxesImage at 0x7f2dece74080>, None)




```python

```
