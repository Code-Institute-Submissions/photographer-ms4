from storages.backends.s3boto3 import S3Boto3Storage

""" Custom storage info for media files """


class MediaStorage(S3Boto3Storage):
    bucket_name = "photographer-static"
    location = "media"
    file_overwrite = False
