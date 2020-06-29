ak='ISSSVUVTXQWXSCPKR23N'
sk='IYZbHMxJss3vXsoi9pqArIySf205lPcoISmm6ReJ'
server='http://obs.cn-north-4.myhuaweicloud.com'
bucketname="obs-tq-dataset"


vector="/workspace/data/osm-2017-07-03-v3.6.1-china_beijing.mbtiles"
cord=(116.5, 39.9, 116.6, 39.8, 14)
class_key='building'
datasource="Google China"
DataSetName="BuildingDataSet"
import sys
sys.path.append("/workspace/DARTH/Darth")
print(sys.path)
from process import Process


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