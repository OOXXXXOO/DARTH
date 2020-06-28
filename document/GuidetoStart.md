![](hansen_tree_cover.png)
# Guide to Start

This demo work for generate dataset quickly.
```python
from process import Process

vector="/workspace/osm-2017-07-03-v3.6.1-china_beijing.mbtiles"
cord=(116.5, 39.9, 116.6, 39.8, 14)
class_key='building'
datasource="Google China"
DataSetName="BuildingDataSet"

```

`process` is a full function dataset generate flow & it will download map production datasource like:

   * Google
   * Google China,
   * Google Maps,
   * Google Satellite,
   * Google Terrain,
   * Google Terrain Hybrid,
   * Google Satellite Hybrid
   * Stamen Terrain
   * Stamen Toner
   * Stamen Toner Light
   * Stamen Watercolor
   * Wikimedia Map
   * Wikimedia Hike Bike Map
   * Esri Boundaries Places
   * Esri Gray (dark)
   * Esri Gray (light)
   * Esri National Geographic
   * Esri Ocean,
   * Esri Satellite,
   * Esri Standard,
   * Esri Terrain,
   * Esri Transportation,
   * Esri Topo World,
   * OpenStreetMap Standard,
   * OpenStreetMap H.O.T.,
   * OpenStreetMap Monochrome,
   * OpenTopoMap,
   * Strava All,
   * Strava Run,
   * Open Weather Map Temperature,
   * Open Weather Map Clouds,
   * Open Weather Map Wind Speed,
   * CartoDb Dark Matter,
   * CartoDb Positron,
   * Bing VirtualEarth
   
for get target information as deeplearning training , we need rasterize vector object that from vector datasource like:

   * MBTiles 
   * Shapefile
   * Pbf
   * Geojson
   
whole work flow include 4 step of data process like:
   
    Step I:
    Init Downlaoder,Bucket,Vector

    Step II:
    Init default vector layer
    Init area , imagery level of mission

    Step III:
    Download
    Merge(Optional)
    Rasterize

    Step IV:
    Upload to Bucket

    Last Step:
    If don't save temp dataset ,clean the cache

input args:

* `vector`       : local path of vector object
* `cord`         : WGS Standard Cord (min-lon,min-lat,max-lon,maxlat,zoom_level)
* `class_key`    : The class you need generate
* `Datasource`   : Map production datasource name
* `Merge`        : Merge the tiles file to whole file or not
* `Keep_local`   : The last step will delete local cache ,this option could choose to save it.
* `upload`       : Use Network Strong Server or not (Just support [Huawei OBS server](https://developer.huaweicloud.com/sdk?OBS) now)
* `thread`       : download thread count


```python
Process(
    vector,
    cord,
    class_key
)
```

    # ---------------------------------------------------------------------------- #
    #                                     DARTH                                    #
    # ---------------------------------------------------------------------------- #
    # ===== Bucket para preview {}
    
    
    
    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Step I ---------------------------------- #
    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #
    #                            MAP Production Toolkit                            #
    # ---------------------------------------------------------------------------- #
    # ---------------------- MAP Serverv Init Successful by ---------------------- #
    # ---------------------- Google China ---------------------------------------- #
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
    
    
    
    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Step II --------------------------------- #
    # ---------------------------------------------------------------------------- #
    # -----Set Default Layer | building | :  <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7ff1df648e70> >
    # -----WGS BoundingBox: (116.4930128805835, 39.9085118736554, 116.60310895291508, 39.790620416540385)
    # -----Mercator BoudingBox: (12967942.873035664, 4852656.366560855, 12980198.711744247, 4835562.295251646)
    # -----Total tiles number：5 X 7


      0%|          | 0/35 [00:00<?, ?it/s]

    # -----Url Queue size: 35
    # -----Set filter Rect: (12967942.873035664, 4852656.366560855, 12980198.711744247, 4835562.295251646)
    
    
    
    # ---------------------------------------------------------------------------- #
    # --------------------------------- Step III --------------------------------- #
    # ---------------------------------------------------------------------------- #
    # ===== imagery dir : DataSet/images/
    # ===== targets dir : DataSet/targets/
    # ===== Start Downloading.....


     94%|█████████▍| 33/35 [00:03<00:00,  9.25it/s]
    100%|██████████| 35/35 [00:00<00:00, 80350.65it/s]
    100%|██████████| 35/35 [00:03<00:00, 11.13it/s]
      3%|▎         | 1/35 [00:00<00:03,  9.10it/s]

    # ===== Decode Downloading...
    # ------------------------------- Download Done ------------------------------ #
    
    # ===== Save description done DataSet/Google China-Sun Jun 28 09:51:04 2020-(116.5, 39.9, 116.6, 39.8)-14.json
    # ===== Start Generate.....


    100%|██████████| 35/35 [00:03<00:00, 10.15it/s]

    # ---------------------------------------------------------------------------- #
    #                             DataSet process done                             #
    # ---------------------------------------------------------------------------- #


    


****
Normally , the local storage dataset is low reusability method , so this workflow support for Internet Data Storge like :
- [x] [Huawei OBS server](https://developer.huaweicloud.com/sdk?OBS)

In additional ,the tool will support for:
- [ ] AMAZON S3
- [ ] MiscroSoft Azure

For use OBS server you must register or buy Bucket & Install OBS python package:
****

```bash
cd obs-src/
python setup.py instal



#out:
Processing dependencies for esdk-obs-python==3.20.1
Finished processing dependencies for esdk-obs-python==3.20.1
```

Then we could open upload option:


```python
ak='XXXXXXXXXXXXXX' # your access_key_id
sk='XXXXXXXXXXXXXX' # your secret_access_key
server='http://obs.cn-north-4.myhuaweicloud.com'# your server
bucketname="XXXXXXX"# your bucket name
```


```python
Process(
    vector,
    cord,
    class_key,
    Upload=True,
    ak=ak,
    sk=sk,
    server=server,
    bn=bucketname
)
```

    # ---------------------------------------------------------------------------- #
    #                                     DARTH                                    #
    # ---------------------------------------------------------------------------- #
    # ===== Bucket para preview {'ak': 'ISSSVUVTXQWXSCPKR23N', 'sk': 'IYZbHMxJss3vXsoi9pqArIySf205lPcoISmm6ReJ', 'server': 'http://obs.cn-north-4.myhuaweicloud.com', 'bn': 'obs-tq-dataset'}
    
    
    
    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Step I ---------------------------------- #
    # ---------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #
    #                            MAP Production Toolkit                            #
    # ---------------------------------------------------------------------------- #
    # ---------------------- MAP Serverv Init Successful by ---------------------- #
    # ---------------------- Google China ---------------------------------------- #
    # ---------------------------------------------------------------------------- #
    #                                Bucket ToolKit                                #
    # ---------------------------------------------------------------------------- #
    # ----access key (AK) :  ISSSVUVTXQWXSCPKR23N
    # ----secret key (SK):  IYZbHMxJss3vXsoi9pqArIySf205lPcoISmm6ReJ
    # ----server :  http://obs.cn-north-4.myhuaweicloud.com
    # ----bucket name :  obs-tq-dataset
    # ----root :  /
    # ---------------------------------------------------------------------------- #
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
    
    
    
    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Step II --------------------------------- #
    # ---------------------------------------------------------------------------- #
    # -----Set Default Layer | building | :  <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7ff1dd55ccc0> >
    # -----WGS BoundingBox: (116.4930128805835, 39.9085118736554, 116.60310895291508, 39.790620416540385)
    # -----Mercator BoudingBox: (12967942.873035664, 4852656.366560855, 12980198.711744247, 4835562.295251646)
    # -----Total tiles number：5 X 7
    # -----Url Queue size: 35
    # -----Set filter Rect: (12967942.873035664, 4852656.366560855, 12980198.711744247, 4835562.295251646)
    
    
    
    # ---------------------------------------------------------------------------- #
    # --------------------------------- Step III --------------------------------- #
    # ---------------------------------------------------------------------------- #
    # ===== imagery dir : DataSet/images/
    # ===== targets dir : DataSet/targets/
    Getting bucket metadata
    
    storageClass: STANDARD
    accessContorlAllowOrigin: None
    accessContorlMaxAge: None
    accessContorlExposeHeaders: None
    accessContorlAllowMethods: None
    accessContorlAllowHeaders: None
    Deleting bucket CORS
    
    status204
    # ===== Bucket imagery root  : DataSets/DataSet/images/
    # ===== Bucket Targets root  : DataSets/DataSet/targets/
    # ===== Bucket Description root : DataSets/DataSet/
    # ===== Base Folder DataSets
    # ===== list (DataSets): 


      0%|          | 0/35 [00:00<?, ?it/s]

    # ===== object count :  1000
       |--- : DataSets/ etag["d41d8cd98f00b204e9800998ecf8427e"]
       |--- : DataSets/Building_Beijing_14/.meta etag["f802f58e7d89c2cad4f9d42d54a805e7"]
       |--- : DataSets/Building_Beijing_14/Google China-Wed Jun 10 17:44:24 2020-(116.3, 39.9, 116.6, 39.7)-14.json etag["f5d4d06dde3c263cc7c08dd203e9ea86"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6208-14.tif etag["62724a9ee3e6a089e4a8974e0aa2b115"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6209-14.tif etag["1712a0eee45ef4aa0460b55918cbbd6b"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6210-14.tif etag["4c3023113719fa50192bd379de31d843"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6211-14.tif etag["59cb243b1932909164dafdeeb87eb29d"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6212-14.tif etag["0e239caf1796f5b71245c50de3d2b535"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6213-14.tif etag["df9e7aeb65eb9c559e52f7b7565a0c96"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6214-14.tif etag["c4620def4d0157802b77acf59e0a4061"]
    # ===== Start Downloading.....


    100%|██████████| 35/35 [00:01<00:00, 22.26it/s]
    100%|██████████| 35/35 [00:00<00:00, 66818.68it/s]
    100%|██████████| 35/35 [00:01<00:00, 20.14it/s]
      3%|▎         | 1/35 [00:00<00:03,  9.87it/s]

    # ===== Decode Downloading...
    # ------------------------------- Download Done ------------------------------ #
    
    # ===== Save description done DataSet/Google China-Sun Jun 28 10:07:51 2020-(116.5, 39.9, 116.6, 39.8)-14.json
    # ===== Start Generate.....


    100%|██████████| 35/35 [00:03<00:00, 10.22it/s]
     11%|█▏        | 4/35 [00:00<00:00, 39.99it/s]

    
    
    
    # ---------------------------------------------------------------------------- #
    # ---------------------------------- Step IV --------------------------------- #
    # ---------------------------------------------------------------------------- #
    # ===== Upload dataset meta DataSets/DataSet/.meta
    # ===== Upload dataset description DataSets/DataSet/Google China-Sun Jun 28 10:07:51 2020-(116.5, 39.9, 116.6, 39.8)-14.json
    # ===== upload imagry to bucket.....


    100%|██████████| 35/35 [00:01<00:00, 33.26it/s]
     11%|█▏        | 4/35 [00:00<00:00, 39.17it/s]

    # ===== upload target to bucket.....


    100%|██████████| 35/35 [00:00<00:00, 41.14it/s]


    # ===== uploaded bucket:
    # ===== list (DataSets): 
    # ===== object count :  1000
       |--- : DataSets/ etag["d41d8cd98f00b204e9800998ecf8427e"]
       |--- : DataSets/Building_Beijing_14/.meta etag["f802f58e7d89c2cad4f9d42d54a805e7"]
       |--- : DataSets/Building_Beijing_14/Google China-Wed Jun 10 17:44:24 2020-(116.3, 39.9, 116.6, 39.7)-14.json etag["f5d4d06dde3c263cc7c08dd203e9ea86"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6208-14.tif etag["62724a9ee3e6a089e4a8974e0aa2b115"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6209-14.tif etag["1712a0eee45ef4aa0460b55918cbbd6b"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6210-14.tif etag["4c3023113719fa50192bd379de31d843"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6211-14.tif etag["59cb243b1932909164dafdeeb87eb29d"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6212-14.tif etag["0e239caf1796f5b71245c50de3d2b535"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6213-14.tif etag["df9e7aeb65eb9c559e52f7b7565a0c96"]
       |--- : DataSets/Building_Beijing_14/images/Google China-13484-6214-14.tif etag["c4620def4d0157802b77acf59e0a4061"]
    # ---------------------------------------------------------------------------- #
    #                             DataSet process done                             #
    # ---------------------------------------------------------------------------- #


In this part , all the data already upload your OBS storage server .
In addition, you not only could choose keep local dataset or not, but also read dataset by index json file:
```json

{
    "time": "Sun Jun 28 17:30:36 2020",
    "left": 116.5,
    "top": 39.9,
    "right": 116.6,
    "bottom": 39.8,
    "zoom": 14,
    "server": "Google China",
    "data": [
        {
            "server": "Google China",
            "info": [
                13494,
                6208,
                14
            ],
            "url": "http://mt2.google.cn/vt/lyrs=s&hl=zh-CN&gl=CN&src=app&x=13494&y=6208&z=14",
            "path": "DataSet/images/Google China-13494-6208-14.tif"
        },
        {
            "server": "Google China",
            "info": [
                13496,
                6208,
                14
            ],
            "url": "http://mt2.google.cn/vt/lyrs=s&hl=zh-CN&gl=CN&src=app&x=13496&y=6208&z=14",
            "path": "DataSet/images/Google China-13496-6208-14.tif"
        },

.......

```


```python

```
