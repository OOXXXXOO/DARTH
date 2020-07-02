ak='XXXXX'
sk='XXXXXXXX'
server='http://obs.cn-north-4.myhuaweicloud.com'
bucketname="XXXXXX"


vector="/workspace/osm-2017-07-03-v3.6.1-china_beijing.mbtiles"
cord=(116.5, 39.9, 116.6, 39.8, 14)
class_key='building'
datasource="Google China"
DataSetName="BuildingDataSet"

from darth.process import Process

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
