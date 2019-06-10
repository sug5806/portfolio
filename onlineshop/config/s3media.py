from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = ''
    bucket_name = 'm-shop'
    region_name = 'ap-northeast-2'
    custom_domain = '%s.s3.%s.amazonaws.com' % (bucket_name, region_name)
    file_overwrite = False