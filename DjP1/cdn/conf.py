import os

LIARA_ACCESS_KEY  = os.environ.get("LIARA_ACCESS_KEY")
LIARA_SECRET_KEY  = os.environ.get("LIARA_SECRET_KEY")
LIARA_ENDPOINT    = os.environ.get("LIARA_ENDPOINT")
LIARA_BUCKET_NAME = os.environ.get("LIARA_BUCKET_NAME")





# Liara Configuration
AWS_ACCESS_KEY_ID       = LIARA_ACCESS_KEY
AWS_SECRET_ACCESS_KEY   = LIARA_SECRET_KEY
AWS_S3_ENDPOINT_URL     = LIARA_ENDPOINT
AWS_STORAGE_BUCKET_NAME = LIARA_BUCKET_NAME
AWS_S3_REGION_NAME      = 'default'

# URL Signing (Canned Policy)
AWS_QUERYSTRING_AUTH = True  # 👈 Enables automatic signing
AWS_QUERYSTRING_EXPIRE = 3600  # 1 hour expiration

# Required for Liara
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_ADDRESSING_STYLE = 'virtual'

# Custom Domain
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.storage.c2.liara.space'


# storage
STORAGES = {
    "default": {
        "BACKEND": "DjP1.cdn.backends.MediaRootS3Boto3Storage",
        "OPTIONS": {
            "querystring_auth": True,  # 👈 Force signing
            "signature_version": "s3v4",
        }
    },
    "staticfiles": {
        "BACKEND": "DjP1.cdn.backends.StaticRootS3Boto3Storage",
        "OPTIONS": {
            "querystring_auth": True,  # 👈 Force signing
            "signature_version": "s3v4",
        },
    }
}

#STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
#MEDIA_URL  = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"






#
#AWS_ACCESS_KEY_ID       = LIARA_ACCESS_KEY
#AWS_SECRET_ACCESS_KEY   = LIARA_SECRET_KEY
#AWS_S3_ENDPOINT_URL     = LIARA_ENDPOINT
#AWS_STORAGE_BUCKET_NAME = LIARA_BUCKET_NAME
#AWS_S3_REGION_NAME      = 'default'
#AWS_S3_OBJECT_PARAMETERS       = {
#    "CacheControl" : "86400"
#}
#
#
#AWS_S3_CUSTOM_DOMAIN = "%s.storage.c2.liara.space" % AWS_STORAGE_BUCKET_NAME
##AWS_LOCATION = f'{LIARA_BUCKET_NAME}.storage.c2.liara.space'
#AWS_QUERYSTRING_AUTH = True  # 👈 Enables URL signature generation
#AWS_QUERYSTRING_EXPIRE = 3600  # URL expiration time in seconds (1 hour default)
#AWS_S3_SIGNATURE_VERSION = 's3v4'  # Required for Liara's S3-compatible API
#S3_URL = "https://%s" % AWS_S3_CUSTOM_DOMAIN
#
##STATICFILES_STORAGE = "DjP1.cdn.backends.StaticRootS3Boto3Storage"
##DEFAULT_FILE_STORAGE = "DjP1.cdn.backends.MediaRootS3Boto3Storage"
#
#STORAGES = {
#  "default": {
#      "BACKEND": "DjP1.cdn.backends.StaticRootS3Boto3Storage",
#  },
#  "staticfiles": {
#      "BACKEND": "DjP1.cdn.backends.StaticRootS3Boto3Storage",
#  },
#}
#
#STATIC_URL = f"https://{S3_URL}/static/"
#MEDIA_URL  = f"https://{S3_URL}/media/"
#