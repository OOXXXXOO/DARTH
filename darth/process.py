import multiprocessing
from tqdm import tqdm
import os
import gdal



from downloader import downloader
from obsclient import bucket
from vector import Vector


def Process(
    VectorDataSource,
    WgsCord,
    Class_key,
    DataSourcesType='Google China',
    DataSetName="DataSet",
    Remote_dataset_root="DataSets/",
    Thread_count=2,
    Nodata=0,
    Merge=False,
    Keep_local=True,
    Over_write=True,
    Upload=False,
    **args
    ):
    """
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
    args:

        for obs server:
            ak : access_key_id,    
            sk : secret_access_key,    
            server : server
            bn :  bucketname


    """

    print("# ---------------------------------------------------------------------------- #")
    print("#                                     DARTH                                    #")
    print("# ---------------------------------------------------------------------------- #")

    print("# ===== Bucket para preview %s"%args)


    
    print("\n\n\n# ---------------------------------------------------------------------------- #")
    print("# ---------------------------------- Step I ---------------------------------- #")
    print("# ---------------------------------------------------------------------------- #")



    Download=downloader(DataSourcesType,thread_count=Thread_count)
    if Upload:
        Bucket=bucket(
            access_key_id=args["ak"],
            secret_access_key=args["sk"],
            server=args["server"],
            bucketName=args["bn"]
            )
        if not Over_write:
            Bucket.check(remote_metaname)
    Vec=Vector(VectorDataSource)
    remote_metaname=Remote_dataset_root+DataSetName+"/.meta"





    print("\n\n\n# ---------------------------------------------------------------------------- #")
    print("# ---------------------------------- Step II --------------------------------- #")
    print("# ---------------------------------------------------------------------------- #")

    Vec.getDefaultLayerbyName(Class_key)
    Download.add_cord(*WgsCord)
    Vec.crop_default_layer_by_rect(Download.mercator_cord)

    print("\n\n\n# ---------------------------------------------------------------------------- #")
    print("# --------------------------------- Step III --------------------------------- #")
    print("# ---------------------------------------------------------------------------- #")

    image_dir=os.path.join(DataSetName,'images/')
    targets_dir=os.path.join(DataSetName,'targets/')
    print("# ===== imagery dir :",image_dir)
    print("# ===== targets dir :",targets_dir)
    if not os.path.exists("./"+DataSetName):
        os.makedirs(image_dir)
        os.makedirs(targets_dir)
    

    local_metaname=DataSetName+"/.meta"
    with open(local_metaname,"w") as meta:
        if Upload:
            meta.write(
                "Bucket Meta:\n"+str(Bucket.getBucketMetadata())
            )
        meta.write(
            "Vector object Meta:\n"+str(Vec.meta)
        )
    meta.close()

        
    if Upload:
        bucket_imagery_root=os.path.join(Remote_dataset_root,image_dir)
        bucket_targets_root=os.path.join(Remote_dataset_root,targets_dir)
        bucket_description_root=os.path.join(Remote_dataset_root,DataSetName+"/")
            
        print("# ===== Bucket imagery root  :",bucket_imagery_root)
        print("# ===== Bucket Targets root  :",bucket_targets_root)
        print("# ===== Bucket Description root :",bucket_description_root)
        
        Bucket.cd("DataSets")
        Bucket.ls()
    
    print("# ===== Start Downloading.....")
    Download.download(output_path=image_dir)
    tiles=[i["path"] for i in Download.result]
    Vec.generate(tiles,output_path=targets_dir)
    


    if Upload:
        print("\n\n\n# ---------------------------------------------------------------------------- #")
        print("# ---------------------------------- Step IV --------------------------------- #")
        print("# ---------------------------------------------------------------------------- #")
        print("# ===== Upload dataset meta",remote_metaname)

        Bucket.upload(
            remote_path=remote_metaname,
            local_path=local_metaname
        )
            
        ## Saveing index json file
        remote_json_path=os.path.join(bucket_description_root,Download.json_path.split('/')[-1])
        print("# ===== Upload dataset description",remote_json_path)
        if not Over_write:
            Bucket.check(remote_json_path)
        
        Bucket.upload(
                remote_path=remote_json_path,
                local_path=Download.json_path
            )


        print("# ===== upload imagry to bucket.....")
        
        for tile in tqdm(tiles):
            file_name=tile.split('/')[-1]
            remote_tiles=os.path.join(bucket_imagery_root,file_name)
            if not Over_write:
                Bucket.check(remote_tiles)
            
            Bucket.upload(
                remote_path=remote_tiles,
                local_path=tile
            )

        print("# ===== upload target to bucket.....")

        for target in tqdm(Vec.labellist):
            file_name=target.split('/')[-1]
            remote_target=os.path.join(bucket_targets_root,file_name)
            if not Over_write:
                Bucket.check(remote_target)
        
            Bucket.upload(
                remote_path=remote_target,
                local_path=target
            )
        print("# ===== uploaded bucket:")
        Bucket.ls()

    if not Keep_local:
        print("# ------------------------------- Clear-cache ------------------------------- #")
        cmd="rm -rf "+DataSetName
        os.system(cmd)
        print("# -------------------------------- Clear-Done ------------------------------- #")

    print("# ---------------------------------------------------------------------------- #")
    print("#                             DataSet process done                             #")
    print("# ---------------------------------------------------------------------------- #")

def main():
    vecfile="/workspace/data/osm-2017-07-03-v3.6.1-china_beijing.mbtiles"
    macfile='/Users/tanwenxuan/workspace/Data/osm-2017-07-03-v3.6.1-china_beijing.mbtiles'
    tqfile="/workspace/osm-2017-07-03-v3.6.1-china_beijing.mbtiles"

    process(tqfile,Keep_local=False,Over_write=True)





if __name__ == '__main__':
    main()
    