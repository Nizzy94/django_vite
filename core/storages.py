from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    file_overwrite = False
    location = 'media'  # store files under directory `media/` in bucket `my-app-bucket`
