#!/usr/bin/python
# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

import os
import traceback
from obs import const, util, progress, bulktasks
from obs.model import GetObjectRequest
from obs.model import GetObjectHeader
from obs.ilog import ERROR

def _download_files(obsClient, bucketName, prefix, downloadFolder=None, taskNum=const.DEFAULT_TASK_NUM, taskQueueSize=const.DEFAULT_TASK_QUEUE_SIZE, 
                      headers=GetObjectHeader(), imageProcess=None, interval=const.DEFAULT_BYTE_INTTERVAL, taskCallback=None, progressCallback=None,
                      threshold=const.DEFAULT_MAXIMUM_SIZE, partSize=5*1024*1024, subTaskNum=1, enableCheckpoint=False, checkpointFile=None, extensionHeaders=None):
    try:
        executor = None
        notifier = None
        if downloadFolder is None or not os.path.isdir(downloadFolder):
            raise Exception('%s is not a Folder' % downloadFolder)
        
        if taskCallback is not None and not callable(taskCallback):
            raise Exception('Invalid taskCallback')
        
        (taskNum, taskQueueSize, interval, threshold) = bulktasks._checkBulkTasksPara(taskNum, taskQueueSize, interval, threshold)
        
        taskCallback = taskCallback if taskCallback is not None else util.lazyCallback
        executor = bulktasks.ThreadPool(taskNum, taskQueueSize)
        state = bulktasks.ExecuteProgress()
        totalTasks = const.LONG(0)
        totalAmount = const.LONG(0)
        notifier = progress.ProgressNotifier(progressCallback, totalAmount, interval) if progressCallback is not None else progress.NONE_NOTIFIER
        notifier.start()
        
        query = GetObjectRequest(imageProcess=imageProcess)
        
        prefix = prefix if prefix is not None else '' 
        prefixDir = prefix[:prefix.rfind('/')+1] 
        
        for content in _list_objects(obsClient, bucketName, prefix=prefix, extensionHeaders=extensionHeaders):
            objectKey = content.key
            totalTasks += 1
            totalAmount += content.size
            objectPath = objectKey.replace(prefixDir, '', 1)
            if objectPath.startswith('/') or objectPath.find('//') != -1 or objectPath.find('\\') != -1:
                state._failed_increment()
                taskCallback(objectKey, Exception('illegal path: %s' % objectKey))
                obsClient.log_client.log(ERROR, 'illegal path: %s' % objectKey)
                continue
            
            downloadPath = os.path.join(downloadFolder, objectPath)
            downloadPath = util.safe_encode(downloadPath)
            if const.IS_WINDOWS:
                downloadPath = util.safe_trans_to_gb2312(downloadPath)
            
            dirName = os.path.dirname(downloadPath)                
            if not os.path.exists(dirName):
                try:
                    os.makedirs(dirName, 0o755)
                except Exception as e:
                    state._failed_increment()
                    taskCallback(objectKey, e)
                    obsClient.log_client.log(ERROR, traceback.format_exc())
                    continue
                
            if objectKey.endswith(('/')):
                state._successful_increment()
            elif content.size < threshold: 
                executor.execute(_task_wrap, obsClient, obsClient._getObjectWithNotifier, key=objectKey, taskCallback=taskCallback, state=state, bucketName=bucketName, 
                                 objectKey=objectKey, getObjectRequest=query, headers=headers, downloadPath=downloadPath, notifier=notifier, extensionHeaders=extensionHeaders)
            else:
                executor.execute(_task_wrap, obsClient, obsClient._downloadFileWithNotifier, key=objectKey, taskCallback=taskCallback, state=state, bucketName=bucketName, 
                                 objectKey=objectKey, downloadFile=downloadPath, partSize=partSize, taskNum=subTaskNum, enableCheckpoint=enableCheckpoint, 
                                 checkpointFile=checkpointFile, header=headers, imageProcess=imageProcess, notifier=notifier, extensionHeaders=extensionHeaders)
                
        state.total_tasks = totalTasks
        notifier.totalAmount = totalAmount
    finally:
        if executor is not None:
            executor.shutdown()
        if notifier is not None:
            notifier.end()
    
    return state
    
def _task_wrap(obsClient, func, key, taskCallback=None, state=None, **kwargs):
    try:
        res = func(**kwargs)
        if res.status < 300:
            state._successful_increment()
        else:
            state._failed_increment()
        taskCallback(key, res)
    except Exception as e:
        state._failed_increment()
        taskCallback(key, e)
        obsClient.log_client.log(ERROR, traceback.format_exc())
        
def _list_objects(obsClient, bucketName, prefix=None, marker=None, max_keys=None, delimiter=None, extensionHeaders=None):
    while True:
        resp = obsClient.listObjects(bucketName, max_keys=max_keys, marker=marker, prefix=prefix, delimiter=delimiter, extensionHeaders=extensionHeaders)
        if resp.status < 300:
            for content in resp.body.contents:
                yield content
            if not resp.body.is_truncated:
                break
            marker = resp.body.next_marker
        else:
            obsClient.log_client.log(ERROR, 'listObjects Error: errorCode:%s, errorMessage:%s' % (resp.errorCode, resp.errorMessage))
            break