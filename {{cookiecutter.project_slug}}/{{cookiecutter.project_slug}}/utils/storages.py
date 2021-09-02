{% if cookiecutter.cloud_provider == 'AWS' -%}
from storages.backends.s3boto3 import S3Boto3Storage, S3ManifestStaticStorage

class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = "media"
    file_overwrite = False

class ManifestS3Storage(S3ManifestStaticStorage):
    location = "static"
    default_acl = "public-read"
    manifest_strict = False


{%- elif cookiecutter.cloud_provider == 'GCP' -%}
from storages.backends.gcloud import GoogleCloudStorage


class StaticRootGoogleCloudStorage(GoogleCloudStorage):
    location = "static"
    default_acl = "publicRead"


class MediaRootGoogleCloudStorage(GoogleCloudStorage):
    location = "media"
    file_overwrite = False
{%- endif %}


{%- elif cookiecutter.use_whitenoise -%}
from whitenoise.storage import CompressedManifestStaticFilesStorage

class CustomCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            result = super().hashed_name(name, content, filename)
        except ValueError:
            # When the file is missing, let's forgive and ignore that.
            result = name
        return result
{%- endif %}
