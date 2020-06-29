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

import time
from obs.const import LONG, BASESTRING
from obs import util
from obs import progress

__all__ = [
    'BaseModel',
    'GetResult',
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
    'Initiator',
    'ACL',
    'Bucket',
    'CommonPrefix',
    'Condition',
    'Content',
    'DateTime',
    'SseHeader',
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
    'ObjectDeleteMarker',
    'ObjectVersionHead',
    'ObjectVersion',
    'Options',
    'Policy',
    'PutObjectHeader',
    'AppendObjectHeader',
    'AppendObjectContent',
    'RedirectAllRequestTo',
    'Redirect',
    'RoutingRule',
    'Tag',
    'TagInfo',
    'Transition',
    'Part',
    'NoncurrentVersionTransition',
    'Rule',
    'Upload',
    'Versions',
    'Object',
    'WebsiteConfiguration',
    'Logging',
    'ObjectVersions',
    'CompleteMultipartUploadRequest',
    'CompleteMultipartUploadResponse',
    'CopyObjectResponse',
    'CopyPartResponse',
    'DeleteObjectResponse',
    'DeleteObjectsRequest',
    'DeleteObjectsResponse',
    'ErrorResult',
    'DeleteObjectResult',
    'ListMultipartUploadsRequest',
    'ListPartsResponse',
    'GetBucketMetadataResponse',
    'GetBucketQuotaResponse',
    'GetBucketStorageInfoResponse',
    'GetBucketStoragePolicyResponse',
    'GetObjectMetadataResponse',
    'SetObjectMetadataResponse',
    'GetObjectRequest',
    'InitiateMultipartUploadResponse',
    'LifecycleResponse',
    'ListBucketsResponse',
    'ListMultipartUploadsResponse',
    'ListObjectsResponse',
    'LocationResponse',
    'OptionsResponse',
    'PutContentResponse',
    'AppendObjectResponse',
    'UploadPartResponse',
    'ResponseWrapper',
    'ObjectStream',
    'GetBucketEncryptionResponse',
    'UploadFileHeader',
    'GetBucketRequestPaymentResponse',
    'Payer',
    'ExtensionHeader'
]


class BaseModel(dict):
    def __init__(self, **kwargs):
        super(BaseModel, self).__init__(**kwargs)

    def __getattr__(self, key):
        if key == 'allowedAttr':
            return {}
        key = key[:1].lower() + key[1:] if key is not None else ''
        if key in self.allowedAttr:
            return self.get(key)
        return None

    def __setattr__(self, key, value):
        key = key[:1].lower() + key[1:] if key is not None else ''
        if key in self.allowedAttr:
            if util.verify_attr_type(value, self.allowedAttr[key]):
                self[key] = value

    def __delattr__(self, key):
        key = key[:1].lower() + key[1:] if key is not None else ''
        if key in self.allowedAttr and key in self:
            del self[key]


class GetResult(BaseModel):
 
    allowedAttr = {'status': int, 'reason':BASESTRING, 'errorCode': BASESTRING, 'errorMessage': BASESTRING,
                   'body': object, 'requestId': BASESTRING, 'hostId': BASESTRING, 'resource': BASESTRING, 'header':list,
                   'indicator': BASESTRING}
 
    def __init__(self, code=None, message=None, status=None, reason=None, body=None, requestId=None, hostId=None, resource=None, header=None, indicator=None):
        self.status = status
        self.reason = reason
        self.errorCode = code
        self.errorMessage = message
        self.body = body
        self.requestId = requestId
        self.hostId = hostId
        self.resource = resource
        self.header = header
        self.indicator = indicator

class CompletePart(BaseModel):
    allowedAttr = {'partNum': int, 'etag': BASESTRING}

    def __init__(self, partNum=None, etag=None):
        self.partNum = partNum
        self.etag = etag

class AvailableZone(object):
    MULTI_AZ = '3az'

class Permission(object):
    READ = 'READ'
    WRITE = 'WRITE'
    READ_ACP = 'READ_ACP'
    WRITE_ACP = 'WRITE_ACP'
    FULL_CONTROL = 'FULL_CONTROL'

class Group(object):
    ALL_USERS = 'Everyone'
    AUTHENTICATED_USERS = 'AuthenticatedUsers'
    LOG_DELIVERY = 'LogDelivery'

class HeadPermission(object):
    PRIVATE = 'private'
    PUBLIC_READ = 'public-read'
    PUBLIC_READ_WRITE = 'public-read-write'
    PUBLIC_READ_DELIVERED = 'public-read-delivered'
    PUBLIC_READ_WRITE_DELIVERED = 'public-read-write-delivered'
    AUTHENTICATED_READ = 'authenticated-read'
    BUCKET_OWNER_READ = 'bucket-owner-read'
    BUCKET_OWNER_FULL_CONTROL = 'bucket-owner-full-control'
    LOG_DELIVERY_WRITE = 'log-delivery-write'
    
class StorageClass(object):
    STANDARD = 'STANDARD'
    WARM = 'WARM'
    COLD = 'COLD'
    
class RestoreTier(object):
    EXPEDITED = 'Expedited'
    STANDARD = 'STANDARD'
    BULK = 'Bulk'
    
class EventType(object):
    OBJECT_CREATED_ALL = 'ObjectCreated:*'
    OBJECT_CREATED_PUT = 'ObjectCreated:Put'
    OBJECT_CREATED_POST = 'ObjectCreated:Post'
    OBJECT_CREATED_COPY = 'ObjectCreated:Copy'
    OBJECT_CREATED_COMPLETE_MULTIPART_UPLOAD = 'ObjectCreated:CompleteMultipartUpload'
    OBJECT_REMOVED_ALL = 'ObjectRemoved:*'
    OBJECT_REMOVED_DELETE = 'ObjectRemoved:Delete'
    OBJECT_REMOVED_DELETE_MARKER_CREATED = 'ObjectRemoved:DeleteMarkerCreated'

class Grantee(BaseModel):

    allowedAttr = {'grantee_id': BASESTRING, 'grantee_name': BASESTRING, 'group': BASESTRING}

    def __init__(self, grantee_id=None, grantee_name=None, group=None):
        self.grantee_id = grantee_id
        self.grantee_name = grantee_name
        self.group = group

class Grant(BaseModel):

    allowedAttr = {'grantee': Grantee, 'permission': BASESTRING, 'delivered': [bool, BASESTRING]}

    def __init__(self, grantee=None, permission=None, delivered=None):
        self.grantee = grantee
        self.permission = permission
        self.delivered = delivered

class Owner(BaseModel):

    allowedAttr = {'owner_id': BASESTRING, 'owner_name': BASESTRING}

    def __init__(self, owner_id=None, owner_name=None):
        self.owner_id = owner_id
        self.owner_name = owner_name

class Initiator(BaseModel):
    allowedAttr = {'id': BASESTRING, 'name': BASESTRING}
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

class ACL(BaseModel):

    allowedAttr = {'owner': Owner, 'grants': list, 'delivered': [bool, BASESTRING]}

    def __init__(self, owner=None, grants=None, delivered=None):
        self.owner = owner
        self.grants = grants
        self.delivered = delivered

    def add_grant(self, grant):
        if self.grants is None:
            self.grants = []
        if isinstance(grant, Grant):
            self.grants.append(grant)
            
class Bucket(BaseModel):
    allowedAttr = {'name': BASESTRING, 'create_date': BASESTRING, 'location': BASESTRING}
    def __init__(self, name=None, create_date=None, location=None):
        self.name = name
        self.create_date = create_date
        self.location = location
    
class CommonPrefix(BaseModel):
    allowedAttr = {'prefix': BASESTRING}
    def __init__(self, prefix=None):
        self.prefix = prefix
    
class Condition(BaseModel):
    allowedAttr = {'keyPrefixEquals': BASESTRING, 'httpErrorCodeReturnedEquals': int}

    def __init__(self, keyPrefixEquals=None, httpErrorCodeReturnedEquals=None):
        self.keyPrefixEquals = keyPrefixEquals
        self.httpErrorCodeReturnedEquals = httpErrorCodeReturnedEquals
        
class Content(BaseModel):
    allowedAttr = {'key': BASESTRING, 'lastModified': BASESTRING, 'etag': BASESTRING,
                   'size': LONG, 'owner': Owner, 'storageClass': BASESTRING, 'isAppendable':bool}
    
    def __init__(self, key=None, lastModified=None, etag=None, size=None, owner=None, storageClass=None, isAppendable=None):
        self.key = key
        self.lastModified = lastModified
        self.etag = etag
        self.size = size
        self.owner = owner
        self.storageClass = storageClass
        self.isAppendable = isAppendable
        
    def __str__(self):
        return self.key

class DateTime(BaseModel):

    allowedAttr = {'year': int, 'month': int, 'day': int, 'hour': int, 'min':int, 'sec':int}

    def __init__(self, year, month, day, hour=0, min=0, sec=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.min = min
        self.sec = sec

    def ToUTTime(self):
        strTime = '%04d-%02d-%02dT%02d:%02d:%02d.000Z' % (self.year, self.month, self.day, self.hour, self.min, self.sec)
        return strTime

    def ToGMTTime(self):
        strTime = (self.year, self.month, self.day, self.hour, self.min, self.sec, 0, 0, 0)
        gmt_time = time.gmtime(time.mktime(strTime) - time.timezone)
        return time.strftime('%a, %d %b %Y %H:%M:%S GMT', gmt_time)

    def ToUTMidTime(self):
        strTime = '%04d-%02d-%02dT00:00:00.000Z' % (self.year, self.month, self.day)
        return strTime

    @staticmethod
    def UTCToLocal(strUTC):
        if strUTC is None:
            return None

        date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        CST_FORMAT = '%Y/%m/%d %H:%M:%S'
        try:
            gmt_time = time.strptime(strUTC, date_format)
    
            cst_time = time.localtime(time.mktime(gmt_time) - time.timezone)
            dt = time.strftime(CST_FORMAT, cst_time)
    
            return dt
        except:
            return strUTC
    
    @staticmethod
    def UTCToLocalMid(strUTC):
        if strUTC is None:
            return None
    
        date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
        CST_FORMAT = '%Y/%m/%d 00:00:00'
        try:
            gmt_time = time.strptime(util.to_string(strUTC), date_format)
        
            cst_time = time.localtime(time.mktime(gmt_time) - time.timezone)
            dt = time.strftime(CST_FORMAT, cst_time)
            return dt
        except:
            return strUTC

class SseHeader(BaseModel):
    allowedAttr = {'encryption': BASESTRING, 'key': BASESTRING}


class SseCHeader(SseHeader):
    @staticmethod
    def getInstance(key, encryption='AES256'):
        return SseCHeader(encryption=encryption, key=key)

class SseKmsHeader(SseHeader):
    @staticmethod
    def getInstance(key=None, encryption='kms'):
        return SseKmsHeader(encryption=encryption, key=key)
  
class CopyObjectHeader(BaseModel):
    allowedAttr = {'acl': BASESTRING, 'directive': BASESTRING, 'if_match': BASESTRING,
                   'if_none_match': BASESTRING, 'if_modified_since': [BASESTRING, DateTime], 'if_unmodified_since': [BASESTRING, DateTime], 'location': BASESTRING,
                   'destSseHeader': SseHeader, 'sourceSseHeader': SseHeader, 'cacheControl' : BASESTRING, 'contentDisposition': BASESTRING,
                   'contentEncoding' : BASESTRING, 'contentLanguage' : BASESTRING, 'contentType' : BASESTRING, 'expires': BASESTRING, 
                   'storageClass': BASESTRING, 'successActionRedirect': BASESTRING, 'extensionGrants': list}


    def __init__(self, acl=None, directive=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None, location=None, destSseHeader=None, sourceSseHeader=None,
                 cacheControl=None, contentDisposition=None, contentEncoding=None, contentLanguage=None, contentType=None, expires=None, storageClass=None, successActionRedirect=None, extensionGrants=None):
        self.acl = acl
        self.directive = directive
        self.if_match = if_match
        self.if_none_match = if_none_match
        self.if_modified_since = if_modified_since
        self.if_unmodified_since = if_unmodified_since
        self.location = location
        self.destSseHeader = destSseHeader
        self.sourceSseHeader = sourceSseHeader
        self.cacheControl = cacheControl
        self.contentDisposition = contentDisposition
        self.contentEncoding = contentEncoding
        self.contentLanguage = contentLanguage
        self.contentType = contentType
        self.expires = expires
        self.storageClass = storageClass
        self.successActionRedirect = successActionRedirect
        self.extensionGrants = extensionGrants

class SetObjectMetadataHeader(BaseModel):
    allowedAttr = {'removeUnset':bool, 'cacheControl' : BASESTRING, 'contentDisposition': BASESTRING,
                   'contentEncoding' : BASESTRING, 'contentLanguage' : BASESTRING, 'contentType' : BASESTRING, 'expires': BASESTRING, 
                   'storageClass': BASESTRING, 'location': BASESTRING}


    def __init__(self, removeUnset=False, location=None, cacheControl=None, contentDisposition=None, 
                 contentEncoding=None, contentLanguage=None, contentType=None, expires=None, storageClass=None):
        self.removeUnset = removeUnset
        self.location = location
        self.cacheControl = cacheControl
        self.contentDisposition = contentDisposition
        self.contentEncoding = contentEncoding
        self.contentLanguage = contentLanguage
        self.contentType = contentType
        self.expires = expires
        self.storageClass = storageClass

class CorsRule(BaseModel):
    allowedAttr = {'id': BASESTRING, 'allowedMethod': list, 'allowedOrigin': list,
                   'allowedHeader': list, 'maxAgeSecond': [int, BASESTRING], 'exposeHeader': list}

    def __init__(self, id=None, allowedMethod=None, allowedOrigin=None, allowedHeader=None, maxAgeSecond=None, exposeHeader=None):
        self.id = id
        self.allowedMethod = allowedMethod
        self.allowedOrigin = allowedOrigin
        self.allowedHeader = allowedHeader
        self.maxAgeSecond = maxAgeSecond
        self.exposeHeader = exposeHeader
        
class CreateBucketHeader(BaseModel):
    allowedAttr = {'aclControl': BASESTRING, 'storageClass': BASESTRING, 'extensionGrants': list, 'availableZone' : BASESTRING, 'epid' : BASESTRING}

    def __init__(self, aclControl=None, storageClass=None, extensionGrants=None, availableZone=None, epid=None):
        self.aclControl = aclControl
        self.storageClass = storageClass
        self.extensionGrants = extensionGrants
        self.availableZone = availableZone
        self.epid = epid
        
class ExtensionGrant(BaseModel):
    allowedAttr = {'permission': BASESTRING, 'granteeId': BASESTRING}
    
    def __init__(self, granteeId=None, permission=None):
        self.granteeId = granteeId
        self.permission = permission
        
class ErrorDocument(BaseModel):

    allowedAttr = {'key': BASESTRING}

    def __init__(self, key=None):
        self.key = key
        
class IndexDocument(BaseModel):

    allowedAttr = {'suffix': BASESTRING}

    def __init__(self, suffix=None):
        self.suffix = suffix
        
class Expiration(BaseModel):

    allowedAttr = {'date': [BASESTRING, DateTime], 'days': int}

    def __init__(self, date=None, days=None):
        self.date = date
        self.days = days

class NoncurrentVersionExpiration(BaseModel):

    allowedAttr = {'noncurrentDays': int}

    def __init__(self, noncurrentDays=None):
        self.noncurrentDays = noncurrentDays
        
        
class GetObjectHeader(BaseModel):
    allowedAttr = {'range': BASESTRING, 'if_modified_since': [BASESTRING, DateTime],
                   'if_unmodified_since': [BASESTRING, DateTime], 'if_match': BASESTRING, 'if_none_match': BASESTRING,
                   'origin': BASESTRING, 'requestHeaders': BASESTRING, 'sseHeader': SseHeader}


    def __init__(self, range=None, if_modified_since=None, if_unmodified_since=None, if_match=None, if_none_match=None, origin=None,
                 requestHeaders=None, sseHeader=None):
        self.range = range
        self.if_modified_since = if_modified_since
        self.if_unmodified_since = if_unmodified_since
        self.if_match = if_match
        self.if_none_match = if_none_match
        self.origin = origin
        self.requestHeaders = requestHeaders
        self.sseHeader = sseHeader
        
class Lifecycle(BaseModel):
    allowedAttr = {'rule': list}

    def __init__(self, rule=None):
        self.rule = rule

class Replication(BaseModel):
    allowedAttr = {'replicationRules': list, 'agency': BASESTRING}
    def __init__(self, replicationRules=None, agency=None):
        self.replicationRules = replicationRules
        self.agency = agency

class ReplicationRule(BaseModel):
    allowedAttr = {'id': BASESTRING, 'prefix': BASESTRING, 'status' : BASESTRING, 'bucket': BASESTRING, 'storageClass': BASESTRING}
    
    def __init__(self, id=None, prefix=None, status=None, bucket=None, storageClass=None):
        self.id = id
        self.prefix = prefix
        self.status = status
        self.bucket = bucket
        self.storageClass = storageClass
        
class Notification(BaseModel):
    allowedAttr = {'topicConfigurations': list, 'functionGraphConfigurations': list}

    def __init__(self, topicConfigurations=None, functionGraphConfigurations=None):
        self.topicConfigurations = topicConfigurations
        self.functionGraphConfigurations = functionGraphConfigurations

class TopicConfiguration(BaseModel):
    allowedAttr = {'id': BASESTRING, 'topic': BASESTRING, 'events': list, 'filterRules': list}

    def __init__(self, id=None, topic=None, events=None, filterRules=None):
        self.id = id
        self.topic = topic
        self.events = events
        self.filterRules = filterRules

class FunctionGraphConfiguration(BaseModel):
    allowedAttr = {'id': BASESTRING, 'functionGraph': BASESTRING, 'events': list, 'filterRules': list}

    def __init__(self, id=None, functionGraph=None, events=None, filterRules=None):
        self.id = id
        self.functionGraph = functionGraph
        self.events = events
        self.filterRules = filterRules

class FilterRule(BaseModel):
    allowedAttr = {'name': BASESTRING, 'value': BASESTRING}
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
    
class ObjectDeleteMarker(BaseModel):

    allowedAttr = {'key': BASESTRING, 'versionId': BASESTRING, 'isLatest': bool, 'lastModified': BASESTRING, 'owner': Owner}
    def __init__(self, key=None, versionId=None, isLatest=None, lastModified=None, owner=None):
        self.key = key
        self.versionId = versionId
        self.isLatest = isLatest
        self.lastModified = lastModified
        self.owner = owner
    
class ObjectVersionHead(BaseModel):

    allowedAttr = {'name': BASESTRING, 'location':BASESTRING, 'prefix': BASESTRING, 'delimiter': BASESTRING, 'keyMarker':BASESTRING, 
                   'versionIdMarker':BASESTRING, 'nextKeyMarker':BASESTRING, 'nextVersionIdMarker':BASESTRING, 'maxKeys':int, 'isTruncated': bool}
    def __init__(self, name=None, location=None, prefix=None, delimiter=None, keyMarker=None,
                 versionIdMarker=None, nextKeyMarker=None, nextVersionIdMarker=None, maxKeys=None, isTruncated=None):
        self.name = name
        self.location = location
        self.prefix = prefix
        self.delimiter = delimiter
        self.keyMarker = keyMarker
        self.versionIdMarker = versionIdMarker
        self.nextKeyMarker = nextKeyMarker
        self.nextVersionIdMarker = nextVersionIdMarker
        self.maxKeys = maxKeys
        self.isTruncated = isTruncated
    
class ObjectVersion(BaseModel):

    allowedAttr = {'key': BASESTRING, 'versionId': BASESTRING, 'isLatest': bool, 'lastModified': BASESTRING,
                   'etag': BASESTRING, 'size': LONG, 'owner': Owner, 'storageClass': BASESTRING, 'isAppendable': bool}
    
    def __init__(self, key=None, versionId=None, isLatest=None, lastModified=None, etag=None,
                 size=None, owner=None, storageClass=None, isAppendable=None):
        self.key = key
        self.versionId = versionId
        self.isLatest = isLatest
        self.lastModified = lastModified
        self.etag = etag
        self.size = size
        self.owner = owner
        self.storageClass = storageClass
        self.isAppendable = isAppendable
    
class Options(BaseModel):
    allowedAttr = {'origin': BASESTRING, 'accessControlRequestMethods': list, 'accessControlRequestHeaders': list}

    def __init__(self, origin=None, accessControlRequestMethods=None, accessControlRequestHeaders=None):
        self.origin = origin
        self.accessControlRequestMethods = accessControlRequestMethods
        self.accessControlRequestHeaders = accessControlRequestHeaders
        
        
class Policy(BaseModel):

    allowedAttr = {'policyJSON': BASESTRING}
    def __init__(self, policyJSON=None):
        self.policyJSON = policyJSON

class PutObjectHeader(BaseModel):
    allowedAttr = {'md5': BASESTRING, 'acl': BASESTRING, 'location': BASESTRING,
                   'contentType': BASESTRING, 'sseHeader': SseHeader, 'contentLength': [int, LONG, BASESTRING],
                   'storageClass': BASESTRING, 'successActionRedirect': BASESTRING, 'expires': int, 'extensionGrants': list}

    def __init__(self, md5=None, acl=None, location=None, contentType=None, sseHeader=None, contentLength=None,
                 storageClass=None, successActionRedirect=None, expires=None, extensionGrants=None):
        self.md5 = md5
        self.acl = acl
        self.location = location
        self.contentType = contentType
        self.sseHeader = sseHeader
        self.contentLength = contentLength
        self.storageClass = storageClass
        self.successActionRedirect = successActionRedirect
        self.expires = expires
        self.extensionGrants = extensionGrants

AppendObjectHeader = PutObjectHeader

class UploadFileHeader(BaseModel):
    allowedAttr = {'acl': BASESTRING, 'websiteRedirectLocation': BASESTRING,'contentType': BASESTRING, 'sseHeader': SseHeader,
                   'storageClass': BASESTRING, 'successActionRedirect': BASESTRING, 'expires': int, 'extensionGrants': list}

    def __init__(self, acl=None, websiteRedirectLocation=None, contentType=None, sseHeader=None,
                 storageClass=None, successActionRedirect=None, expires=None, extensionGrants=None):
        self.acl = acl
        self.websiteRedirectLocation = websiteRedirectLocation
        self.contentType = contentType
        self.sseHeader = sseHeader
        self.storageClass = storageClass
        self.successActionRedirect = successActionRedirect
        self.expires = expires
        self.extensionGrants = extensionGrants

class AppendObjectContent(BaseModel):
    allowedAttr = {'content': [object], 'position': [LONG, int, BASESTRING], 'offset':[LONG, int, BASESTRING], 'isFile': bool}
    def __init__(self, content=None, position=None, offset=None, isFile=False):
        self.content = content
        self.position = position
        self.offset = offset
        self.isFile = isFile
    

class RedirectAllRequestTo(BaseModel):

    allowedAttr = {'hostName': BASESTRING, 'protocol': BASESTRING}

    def __init__(self, hostName=None, protocol=None):
        self.hostName = hostName
        self.protocol = protocol
        
class Redirect(BaseModel):
    allowedAttr = {'protocol': BASESTRING, 'hostName':BASESTRING, 'replaceKeyPrefixWith':BASESTRING,
                   'replaceKeyWith':BASESTRING, 'httpRedirectCode':int}

    def __init__(self, protocol=None, hostName=None, replaceKeyPrefixWith=None, replaceKeyWith=None, httpRedirectCode=None):
        self.protocol = protocol
        self.hostName = hostName
        self.replaceKeyPrefixWith = replaceKeyPrefixWith
        self.replaceKeyWith = replaceKeyWith
        self.httpRedirectCode = httpRedirectCode

    
class RoutingRule(BaseModel):
    allowedAttr = {'condition': Condition, 'redirect': Redirect}

    def __init__(self, condition=None, redirect=None):
        self.condition = condition
        self.redirect = redirect
        
class Tag(BaseModel):
    allowedAttr = {'key': BASESTRING, 'value': BASESTRING}

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

class TagInfo(BaseModel):

    allowedAttr = {'tagSet': list}

    def __init__(self, tagSet=None):
        self.tagSet = tagSet

    def addTag(self, key, value):
        if self.tagSet is None:
            self.tagSet = []
        self.tagSet.append(Tag(key=key, value=value))
        return self
    
class Transition(BaseModel):

    allowedAttr = {'date': [BASESTRING, DateTime], 'days': int, 'storageClass': BASESTRING}

    def __init__(self, storageClass=None, date=None, days=None):
        self.storageClass = storageClass
        self.date = date
        self.days = days

class Part(BaseModel):

    allowedAttr = {'partNumber': int, 'lastModified': BASESTRING, 'etag': BASESTRING, 'size':LONG}
    def __init__(self, partNumber=None, lastModified=None, etag=None, size=None):
        self.partNumber = partNumber
        self.lastModified = lastModified
        self.etag = etag
        self.size = size

class NoncurrentVersionTransition(BaseModel):

    allowedAttr = {'noncurrentDays': int, 'storageClass': BASESTRING}

    def __init__(self, storageClass=None, noncurrentDays=None):
        self.noncurrentDays = noncurrentDays
        self.storageClass = storageClass
        
class Rule(BaseModel):

    allowedAttr = {'id': BASESTRING, 'prefix': BASESTRING, 'status': BASESTRING, 'expiration': Expiration, 'noncurrentVersionExpiration': NoncurrentVersionExpiration,
                   'transition': [Transition, list], 'noncurrentVersionTransition': [NoncurrentVersionTransition, list]}

    def __init__(self, id=None, prefix=None, status=None, expiration=None, noncurrentVersionExpiration=None, transition=None, noncurrentVersionTransition=None):
        self.id = id
        self.prefix = prefix
        self.status = status
        self.expiration = expiration
        self.noncurrentVersionExpiration = noncurrentVersionExpiration
        self.transition = transition
        self.noncurrentVersionTransition = noncurrentVersionTransition
        
class Upload(BaseModel):
    allowedAttr = {'key': BASESTRING, 'uploadId':BASESTRING, 'initiator': Initiator,
                   'owner': Owner, 'storageClass': BASESTRING, 'initiated': BASESTRING}

    def __init__(self, key=None, uploadId=None, initiator=None, owner=None, storageClass=None, initiated=None):
        self.key = key
        self.uploadId = uploadId
        self.initiator = initiator
        self.owner = owner
        self.storageClass = storageClass
        self.initiated = initiated
    
class Versions(BaseModel):

    allowedAttr = {'prefix': BASESTRING, 'key_marker': BASESTRING, 'max_keys': [int, BASESTRING],
                   'delimiter': BASESTRING, 'version_id_marker': BASESTRING}

    def __init__(self, prefix=None, key_marker=None, max_keys=None, delimiter=None, version_id_marker=None):
        self.prefix = prefix
        self.key_marker = key_marker
        self.max_keys = max_keys
        self.delimiter = delimiter
        self.version_id_marker = version_id_marker
   
class Object(BaseModel):
    allowedAttr = {'key' : BASESTRING, 'versionId' : BASESTRING}

    def __init__(self, key=None, versionId=None):
        self.key = key
        self.versionId = versionId
     
class WebsiteConfiguration(BaseModel):

    allowedAttr = {'redirectAllRequestTo': RedirectAllRequestTo, 'indexDocument': IndexDocument, 'errorDocument': ErrorDocument, 'routingRules': list}
    def __init__(self, redirectAllRequestTo=None,
                 indexDocument=None,
                 errorDocument=None,
                 routingRules=None):
        self.redirectAllRequestTo = redirectAllRequestTo
        self.indexDocument = indexDocument
        self.errorDocument = errorDocument
        self.routingRules = routingRules
        
class Logging(BaseModel):
    allowedAttr = {'targetBucket': BASESTRING, 'targetPrefix': BASESTRING, 'targetGrants': list, 'agency': BASESTRING}

    def __init__(self, targetBucket=None, targetPrefix=None, targetGrants=None, agency=None):
        self.targetBucket = targetBucket
        self.targetPrefix = targetPrefix
        self.targetGrants = targetGrants
        self.agency = agency
    
    def add_grant(self, grant):
        if self.targetGrants is None:
            self.targetGrants = []
        if isinstance(grant, Grant):
            self.targetGrants.append(grant) 
        
class ObjectVersions(BaseModel):

    allowedAttr = {'head': ObjectVersionHead, 'versions': list, 'markers': list, 'commonPrefixs': list}
    def __init__(self, head=None, versions=None, markers=None, commonPrefixs=None):
        self.head = head
        self.versions = versions
        self.markers = markers
        self.commonPrefixs = commonPrefixs
    
class CompleteMultipartUploadRequest(BaseModel):
    allowedAttr = {'parts': list}

    def __init__(self, parts=None):
        self.parts = parts

    def add_part(self, part):
        if self.parts is None:
            self.parts = []
        if isinstance(part, CompletePart):
            self.parts.append(part)

class CompleteMultipartUploadResponse(BaseModel):

    allowedAttr = {'location': BASESTRING, 'bucket': BASESTRING,
                   'key': BASESTRING, 'etag': BASESTRING, 'versionId' : BASESTRING, 'sseKms': BASESTRING, 
                   'sseKmsKey':BASESTRING, 'sseC':BASESTRING, 'sseCKeyMd5':BASESTRING, 'objectUrl':BASESTRING}
    def __init__(self, location=None, bucket=None, key=None, etag=None,
                 versionId=None, sseKms=None, sseKmsKey=None, sseC=None, 
                 sseCKeyMd5=None, objectUrl=None):
        self.location = location
        self.bucket = bucket
        self.key = key
        self.etag = etag
        self.versionId = versionId
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5
        self.objectUrl = objectUrl

class CopyObjectResponse(BaseModel):
    allowedAttr = {'lastModified': BASESTRING, 'etag': BASESTRING, 'copySourceVersionId': BASESTRING, 'versionId': BASESTRING,
                   'sseKms': BASESTRING, 'sseKmsKey': BASESTRING, 'sseC':BASESTRING, 'sseCKeyMd5': BASESTRING}
    def __init__(self, lastModified=None, etag=None, copySourceVersionId=None, versionId=None, sseKms=None, sseKmsKey=None, sseC=None, sseCKeyMd5=None):
        self.lastModified = lastModified
        self.etag = etag
        self.copySourceVersionId = copySourceVersionId
        self.versionId = versionId
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5
    
class CopyPartResponse(BaseModel):
    allowedAttr = {'lastModified': BASESTRING, 'etag': BASESTRING, 'modifiedDate': BASESTRING, 
                   'sseKms': BASESTRING, 'sseKmsKey':BASESTRING, 'sseC':BASESTRING, 'sseCKeyMd5':BASESTRING}
    def __init__(self, lastModified=None, etag=None, modifiedDate=None, sseKms=None, sseKmsKey=None, sseC=None, sseCKeyMd5=None):
        self.lastModified = lastModified
        self.etag = etag
        self.modifiedDate = modifiedDate
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5
    
class DeleteObjectResponse(BaseModel):
    allowedAttr = {'deleteMarker': bool, 'versionId': BASESTRING}
    def __init__(self, deleteMarker=None, versionId=None):
        self.deleteMarker = deleteMarker
        self.versionId = versionId
    
class DeleteObjectsRequest(BaseModel):

    allowedAttr = {'quiet': bool, 'objects': list}

    def __init__(self, quiet=None, objects=None):
        self.quiet = quiet
        self.objects = objects


    def add_object(self, object):
        if self.objects is None:
            self.objects = []
        if isinstance(object, Object):
            self.objects.append(object)

class DeleteObjectsResponse(BaseModel):
    allowedAttr = {'deleted': list, 'error': list}
    def __init__(self, deleted=None, error=None):
        self.deleted = deleted
        self.error = error

class ErrorResult(BaseModel):
    allowedAttr = {'key': BASESTRING, 'versionId' : BASESTRING, 'code': BASESTRING, 'message': BASESTRING}
    def __init__(self, key=None, versionId=None, code=None, message=None):
        self.key = key
        self.versionId = versionId
        self.code = code
        self.message = message

class DeleteObjectResult(BaseModel):
    allowedAttr = {'key': BASESTRING, 'versionId' : BASESTRING, 'deleteMarker': bool, 'deleteMarkerVersionId': BASESTRING}
    def __init__(self, key=None, versionId=None, deleteMarker=None, deleteMarkerVersionId=None):
        self.key = key
        self.versionId = versionId
        self.deleteMarker = deleteMarker
        self.deleteMarkerVersionId = deleteMarkerVersionId
            
class ListMultipartUploadsRequest(BaseModel):
    allowedAttr = {'delimiter': BASESTRING, 'prefix': BASESTRING, 'max_uploads': [int, BASESTRING], 'key_marker': BASESTRING, 'upload_id_marker': BASESTRING}

    def __init__(self, delimiter=None, prefix=None, max_uploads=None, key_marker=None, upload_id_marker=None):
        self.delimiter = delimiter
        self.prefix = prefix
        self.max_uploads = max_uploads
        self.key_marker = key_marker
        self.upload_id_marker = upload_id_marker


class ListPartsResponse(BaseModel):

    allowedAttr = {'bucketName': BASESTRING, 'objectKey': BASESTRING, 'uploadId': BASESTRING, 'initiator': Initiator,
                   'owner': Owner, 'storageClass': BASESTRING, 'partNumberMarker': int, 'nextPartNumberMarker': int, 'maxParts': int,
                   'isTruncated': bool, 'parts': list}
    def __init__(self, bucketName=None, objectKey=None, uploadId=None, initiator=None, owner=None, 
                 storageClass=None, partNumberMarker=None, nextPartNumberMarker=None, maxParts=None, isTruncated=None, parts=None):
        self.bucketName = bucketName
        self.objectKey = objectKey
        self.uploadId = uploadId
        self.initiator = initiator
        self.owner = owner
        self.storageClass = storageClass
        self.partNumberMarker = partNumberMarker
        self.nextPartNumberMarker = nextPartNumberMarker
        self.maxParts = maxParts
        self.isTruncated = isTruncated
        self.parts = parts
    

class GetBucketMetadataResponse(BaseModel):

    allowedAttr = {'storageClass': BASESTRING, 'accessContorlAllowOrigin': BASESTRING, 'accessContorlAllowHeaders':BASESTRING, 
                   'accessContorlAllowMethods':BASESTRING,
                   'accessContorlExposeHeaders':BASESTRING, 
                   'accessContorlMaxAge':int, 'location': BASESTRING, 'obsVersion' : BASESTRING, 'availableZone':BASESTRING, 'epid':BASESTRING}
    def __init__(self, storageClass=None, accessContorlAllowOrigin=None, accessContorlAllowHeaders=None, 
                 accessContorlAllowMethods=None, accessContorlExposeHeaders=None, accessContorlMaxAge=None, 
                 location=None, obsVersion=None, availableZone=None, epid=None):
        self.storageClass = storageClass
        self.accessContorlAllowOrigin = accessContorlAllowOrigin
        self.accessContorlAllowHeaders = accessContorlAllowHeaders
        self.accessContorlAllowMethods = accessContorlAllowMethods
        self.accessContorlExposeHeaders = accessContorlExposeHeaders
        self.accessContorlMaxAge = accessContorlMaxAge
        self.location = location
        self.obsVersion = obsVersion
        self.availableZone = availableZone
        self.epid = epid
    
class GetBucketQuotaResponse(BaseModel):
    allowedAttr = {'quota': LONG}
    def __init__(self, quota=None):
        self.quota = quota
    

class GetBucketStorageInfoResponse(BaseModel):
    allowedAttr = {'size': LONG, 'objectNumber': int}
    def __init__(self, size=None, objectNumber=None):
        self.size = size
        self.objectNumber = objectNumber

class GetBucketEncryptionResponse(BaseModel):
    allowedAttr = {'encryption': BASESTRING, 'key': BASESTRING}
    def __init__(self, encryption=None, key=None):
        self.encryption = encryption
        self.key = key    
    
class GetBucketStoragePolicyResponse(BaseModel):
    allowedAttr = {'storageClass': BASESTRING}
    def __init__(self, storageClass=None):
        self.storageClass = storageClass
    
class GetObjectMetadataResponse(BaseModel):

    allowedAttr = {'storageClass': BASESTRING, 'accessContorlAllowOrigin': BASESTRING, 
                   'accessContorlAllowHeaders':BASESTRING, 'accessContorlAllowMethods':BASESTRING,
                   'accessContorlExposeHeaders': BASESTRING, 'accessContorlMaxAge': int, 
                   'contentLength': LONG, 'contentType': BASESTRING, 'websiteRedirectLocation': BASESTRING,
                   'lastModified': BASESTRING, 'etag': BASESTRING, 'versionId': BASESTRING, 
                   'restore': BASESTRING, 'expiration': BASESTRING, 'sseKms': BASESTRING, 
                   'sseKmsKey': BASESTRING, 'sseC':BASESTRING, 'sseCKeyMd5': BASESTRING, 'isAppendable': bool, 'nextPosition': LONG}
    def __init__(self, storageClass=None, accessContorlAllowOrigin=None, accessContorlAllowHeaders=None, 
                 accessContorlAllowMethods=None, accessContorlExposeHeaders=None, accessContorlMaxAge=None, contentLength=None,
                 contentType=None, websiteRedirectLocation=None, lastModified=None, etag=None, versionId=None,
                 restore=None, expiration=None, sseKms=None, sseKmsKey=None, sseC=None, sseCKeyMd5=None, isAppendable=None, nextPosition=None):
        self.storageClass = storageClass
        self.accessContorlAllowOrigin = accessContorlAllowOrigin
        self.accessContorlAllowHeaders = accessContorlAllowHeaders
        self.accessContorlAllowMethods = accessContorlAllowMethods
        self.accessContorlExposeHeaders = accessContorlExposeHeaders
        self.accessContorlMaxAge = accessContorlMaxAge
        self.contentLength = contentLength
        self.contentType = contentType
        
        self.websiteRedirectLocation = websiteRedirectLocation
        self.lastModified = lastModified
        self.etag = etag
        self.versionId = versionId
        self.restore = restore
        self.expiration = expiration
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5
        self.isAppendable = isAppendable
        self.nextPosition = nextPosition

SetObjectMetadataResponse = GetObjectMetadataResponse
 
    
class GetObjectRequest(BaseModel):
    allowedAttr = {'content_type': BASESTRING, 'content_language': BASESTRING,
                   'expires': BASESTRING, 'cache_control': BASESTRING, 'content_disposition': BASESTRING,
                   'content_encoding': BASESTRING, 'versionId': BASESTRING, 'imageProcess' : BASESTRING}

    def __init__(self, content_type=None, content_language=None, expires=None, cache_control=None, content_disposition=None, 
                 content_encoding=None, versionId=None, imageProcess=None):
        self.content_type = content_type
        self.content_language = content_language
        self.expires = expires
        self.cache_control = cache_control
        self.content_disposition = content_disposition
        self.content_encoding = content_encoding
        self.versionId = versionId
        self.imageProcess = imageProcess
        
    
class InitiateMultipartUploadResponse(BaseModel):
    allowedAttr = {'bucketName': BASESTRING, 'objectKey': BASESTRING, 'uploadId': BASESTRING,
                   'sseKms': BASESTRING, 'sseKmsKey': BASESTRING, 'sseC': BASESTRING, 'sseCKeyMd5': BASESTRING}
    def __init__(self, bucketName=None, objectKey=None, uploadId=None):
        self.bucketName = bucketName
        self.objectKey = objectKey
        self.uploadId = uploadId
    
    
class LifecycleResponse(BaseModel):

    allowedAttr = {'lifecycleConfig': Lifecycle}
    def __init__(self, lifecycleConfig=None):
        self.lifecycleConfig = lifecycleConfig
        
        
class ListBucketsResponse(BaseModel):

    allowedAttr = {'buckets': list, 'owner': Owner}
    def __init__(self, buckets=None, owner=None):
        self.buckets = buckets
        self.owner = owner
    
class ListMultipartUploadsResponse(BaseModel):

    allowedAttr = {'bucket': BASESTRING, 'keyMarker': BASESTRING, 'uploadIdMarker':BASESTRING,
                   'nextKeyMarker':BASESTRING, 'nextUploadIdMarker':BASESTRING, 'maxUploads': int,
                   'isTruncated':bool, 'prefix':BASESTRING, 'delimiter':BASESTRING, 'upload': list, 'commonPrefixs': list}
    def __init__(self, bucket=None, keyMarker=None, uploadIdMarker=None, nextKeyMarker=None, nextUploadIdMarker=None, 
                 maxUploads=None, isTruncated=None, prefix=None, delimiter=None, upload=None, commonPrefixs=None):
        self.bucket = bucket
        self.keyMarker = keyMarker
        self.uploadIdMarker = uploadIdMarker
        self.nextKeyMarker = nextKeyMarker
        self.nextUploadIdMarker = nextUploadIdMarker
        self.maxUploads = maxUploads
        self.isTruncated = isTruncated
        self.prefix = prefix

        self.delimiter = delimiter
        self.upload = upload
        self.commonPrefixs = commonPrefixs

class ListObjectsResponse(BaseModel):

    allowedAttr = {'name': BASESTRING, 'location' : BASESTRING, 'prefix': BASESTRING, 'marker': BASESTRING, 'delimiter':BASESTRING,
                   'max_keys': int, 'is_truncated': bool, 'next_marker': BASESTRING, 'contents': list, 'commonPrefixs': list}

    def __init__(self, name=None, location=None, prefix=None, marker=None, delimiter=None, 
                 max_keys=None, is_truncated=None, next_marker=None, contents=None, commonPrefixs=None):
        self.name = name
        self.location = location
        self.prefix = prefix
        self.marker = marker
        self.delimiter = delimiter
        self.max_keys = max_keys
        self.is_truncated = is_truncated
        self.next_marker = next_marker
        self.contents = contents
        self.commonPrefixs = commonPrefixs
    
class LocationResponse(BaseModel):

    allowedAttr = {'location': BASESTRING}

    def __init__(self, location=None):
        self.location = location
        
class OptionsResponse(BaseModel):

    allowedAttr = {'accessContorlAllowOrigin': BASESTRING, 'accessContorlAllowHeaders':BASESTRING, 'accessContorlAllowMethods':BASESTRING,
                   'accessContorlExposeHeaders':BASESTRING, 'accessContorlMaxAge':int}
    def __init__(self, accessContorlAllowOrigin=None, accessContorlAllowHeaders=None, accessContorlAllowMethods=None, 
                 accessContorlExposeHeaders=None, accessContorlMaxAge=None):
        self.accessContorlAllowOrigin = accessContorlAllowOrigin
        self.accessContorlAllowHeaders = accessContorlAllowHeaders
        self.accessContorlAllowMethods = accessContorlAllowMethods
        self.accessContorlExposeHeaders = accessContorlExposeHeaders
        self.accessContorlMaxAge = accessContorlMaxAge


class PutContentResponse(BaseModel):

    allowedAttr = {'storageClass': BASESTRING, 'etag': BASESTRING, 'versionId': BASESTRING, 
                   'sseKms': BASESTRING, 'sseKmsKey': BASESTRING, 'sseC': BASESTRING, 'sseCKeyMd5': BASESTRING, 'objectUrl' : BASESTRING}
    def __init__(self, storageClass=None, etag=None, versionId=None, sseKms=None, sseKmsKey=None, 
                 sseC=None, sseCKeyMd5=None, objectUrl=None):
        self.storageClass = storageClass
        self.etag = etag
        self.versionId = versionId
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5
        self.objectUrl = objectUrl
        
class AppendObjectResponse(BaseModel):

    allowedAttr = {'storageClass': BASESTRING, 'etag': BASESTRING, 'nextPosition': LONG,
                   'sseKms': BASESTRING, 'sseKmsKey': BASESTRING, 'sseC': BASESTRING, 'sseCKeyMd5': BASESTRING, 'objectUrl':BASESTRING}
    def __init__(self, storageClass=None, etag=None, nextPosition=None, sseKms=None, sseKmsKey=None, 
                 sseC=None, sseCKeyMd5=None, objectUrl=None):
        self.storageClass = storageClass
        self.etag = etag
        self.nextPosition = nextPosition
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5
        self.objectUrl = objectUrl
        
         
class UploadPartResponse(BaseModel):

    allowedAttr = {'etag': BASESTRING, 'sseKms': BASESTRING, 'sseKmsKey': BASESTRING, 'sseC':BASESTRING, 'sseCKeyMd5': BASESTRING}
    def __init__(self, etag=None, sseKms=None, sseKmsKey=None, sseC=None, sseCKeyMd5=None):
        self.etag = etag
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5

class GetBucketRequestPaymentResponse(BaseModel):
    allowedAttr = {'payer': BASESTRING}
    def __init__(self, payer=None):
        self.payer = payer

class Payer(object):
    BUCKET_OWNER_PAYER = "BucketOwner"
    REQUESTER_PAYER = "Requester"
    REQUESTER = "requester"

class ResponseWrapper(object):
    def __init__(self, conn, result, connHolder, contentLength=None, notifier=None):
        self.conn = conn
        self.result = result
        self.connHolder = connHolder
        self.contentLength = contentLength
        self.readedCount = 0
        self.notifier = notifier
        if self.notifier is None:
            self.notifier = progress.NONE_NOTIFIER
 
    def __getattr__(self, name):
        if name == 'read' and self.result:
            def _read(*args, **kwargs):
                chunk = self.result.read(*args, **kwargs)
                if not chunk:
                    if self.contentLength is not None and self.contentLength != self.readedCount:
                        raise Exception('premature end of Content-Length delimiter message body (expected:' +  util.to_string(self.contentLength) + '; received:' + util.to_string(self.readedCount) + ')')
                else:
                    newReadCount = len(chunk)
                    if newReadCount > 0:
                        self.notifier.send(newReadCount)
                    self.readedCount += newReadCount
                return chunk
            return _read
        
        return getattr(self.result, name) if self.result else None
 
    def close(self):
        self.notifier.end()
        if self.conn:
            util.do_close(self.result, self.conn, self.connHolder)
 
class ObjectStream(BaseModel):
 
    allowedAttr = {'response': ResponseWrapper, 'buffer': object, 'size': LONG, 'url': BASESTRING, 'deleteMarker': bool, 
                   'storageClass': BASESTRING, 'accessContorlAllowOrigin': BASESTRING, 
                   'accessContorlAllowHeaders': BASESTRING, 'accessContorlAllowMethods': BASESTRING,
                   'accessContorlExposeHeaders':BASESTRING, 'accessContorlMaxAge':int, 
                   'contentLength': LONG, 'cacheControl': BASESTRING, 'contentDisposition': BASESTRING,
                   'contentEncoding': BASESTRING, 'contentLanguage': BASESTRING, 
                   'contentType': BASESTRING, 'expires': BASESTRING, 'websiteRedirectLocation': BASESTRING,
                   'lastModified': BASESTRING, 'etag': BASESTRING, 'versionId':BASESTRING, 
                   'restore': BASESTRING, 'expiration': BASESTRING, 'sseKms': BASESTRING, 
                   'sseKmsKey': BASESTRING, 'sseC':BASESTRING, 'sseCKeyMd5': BASESTRING}

    def __init__(self, response=None, buffer=None, size=None, url=None, deleteMarker=None, storageClass=None,
                 accessContorlAllowOrigin=None, accessContorlAllowHeaders=None, accessContorlAllowMethods=None,
                 accessContorlExposeHeaders=None, accessContorlMaxAge=None, contentLength=None, cacheControl=None,
                 contentDisposition=None, contentEncoding=None, contentLanguage=None, contentType=None, expires=None,
                 websiteRedirectLocation=None, lastModified=None, etag=None, versionId=None, restore=None, 
                 expiration=None, sseKms=None, sseKmsKey=None, sseC=None, sseCKeyMd5=None):
        self.response = response
        self.buffer = buffer
        self.size = size
        self.url = url
        self.deleteMarker = deleteMarker
        self.storageClass = storageClass
        self.accessContorlAllowOrigin = accessContorlAllowOrigin
        self.accessContorlAllowHeaders = accessContorlAllowHeaders
        self.accessContorlAllowMethods = accessContorlAllowMethods
        self.accessContorlExposeHeaders = accessContorlExposeHeaders
        self.accessContorlMaxAge = accessContorlMaxAge
        self.contentLength = contentLength
        self.cacheControl = cacheControl
        self.contentDisposition = contentDisposition
        self.contentEncoding = contentEncoding
        self.contentLanguage = contentLanguage
        self.contentType = contentType
        self.expires = expires
        self.websiteRedirectLocation = websiteRedirectLocation
        self.lastModified = lastModified
        self.etag = etag
        self.versionId = versionId
        self.restore = restore
        self.expiration = expiration
        self.sseKms = sseKms
        self.sseKmsKey = sseKmsKey
        self.sseC = sseC
        self.sseCKeyMd5 = sseCKeyMd5
        
class ExtensionHeader(BaseModel):
    allowedAttr = {'requesterPayer': BASESTRING}

    def __init__(self, requesterPayer=None):
        self.requesterPayer = requesterPayer