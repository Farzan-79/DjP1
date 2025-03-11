import os

LIARA_ACCESS_KEY  = os.environ.get("LIARA_ACCESS_KEY")
LIARA_SECRET_KEY  = os.environ.get("LIARA_SECRET_KEY")
LIARA_ENDPOINT    = os.environ.get("LIARA_ENDPOINT")
LIARA_BUCKET_NAME = os.environ.get("LIARA_BUCKET_NAME")


AWS_ACCESS_KEY_ID       = LIARA_ACCESS_KEY
AWS_SECRET_ACCESS_KEY   = LIARA_SECRET_KEY
AWS_S3_ENDPOINT_URL     = LIARA_ENDPOINT
AWS_STORAGE_BUCKET_NAME = LIARA_BUCKET_NAME
AWS_S3_REGION_NAME      = 'us-east-1'
AWS_S3_PARAMETERS       = {
    "CacheControl" : "86400"
}
AWS_S3_CUSTOM_DOMAIN = f"{LIARA_BUCKET_NAME}.storage.c2.liara.space"
AWS_LOCATION = f'{LIARA_BUCKET_NAME}.storage.c2.liara.space'

STATICFILES_STORAGE = "DjP1.cdn.backends.StaticRootS3Boto3Storage"
DEFAULT_FILE_STORAGE = "DjP1.cdn.backends.MediaRootS3Boto3Storage"

STORAGES = {
  "default": {
      "BACKEND": "storages.backends.s3.S3Storage",
  },
  "staticfiles": {
      "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
  },
}

#STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
#MEDIA_URL  = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
