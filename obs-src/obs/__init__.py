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


from obs.ilog import LogConf
from obs.client import ObsClient
from obs.model import *


__all__ = [
    'LogConf',
    'ObsClient',
    'CompletePart',
    'Permission',
    'StorageClass', 
    'EventType',
    'RestoreTier',
    'Group',
    'Grantee',
    'Grant',
    'ExtensionGrant',
    'Owner',
    'ACL',
    'Condition',
    'DateTime',
    'SseCHeader',
    'SseKmsHeader',
    'CopyObjectHeader',
    'SetObjectMetadataHeader',
    'CorsRule',
    'CreateBucketHeader',
    'ErrorDocument',
    'IndexDocument',
    'Expiration',
    'NoncurrentVersionExpiration',
    'GetObjectHeader',
    'HeadPermission',
    'Lifecycle',
    'Notification',
    'TopicConfiguration',
    'FunctionGraphConfiguration',
    'FilterRule',
    'Replication',
    'ReplicationRule',
    'Options',
    'PutObjectHeader',
    'AppendObjectHeader',
    'AppendObjectContent',
    'RedirectAllRequestTo',
    'Redirect',
    'RoutingRule',
    'Tag',
    'TagInfo',
    'Transition',
    'NoncurrentVersionTransition',
    'Rule',
    'Versions',
    'Object',
    'WebsiteConfiguration',
    'Logging',
    'CompleteMultipartUploadRequest',
    'DeleteObjectsRequest',
    'ListMultipartUploadsRequest',
    'GetObjectRequest',
    'UploadFileHeader',
    'Payer',
    'ExtensionHeader'
]

