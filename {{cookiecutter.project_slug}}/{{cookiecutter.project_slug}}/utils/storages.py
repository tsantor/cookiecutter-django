{% if cookiecutter.cloud_provider == 'AWS' -%}
from storages.backends.s3boto3 import S3ManifestStaticStorage
from storages.backends.s3 import S3Storage


class StaticS3Storage(S3Storage):
    location = "static"
    default_acl = "public-read"


class MediaS3Storage(S3Storage):
    location = "media"
    file_overwrite = False

class ManifestS3Storage(S3ManifestStaticStorage):
    location = "static"
    default_acl = "public-read"
    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            result = super().hashed_name(name, content, filename)
        except ValueError:
            # When the file is missing, let's forgive and ignore that.
            result = name
        return result


{%- elif cookiecutter.cloud_provider == 'GCP' -%}
from storages.backends.gcloud import GoogleCloudStorage


class StaticGoogleCloudStorage(GoogleCloudStorage):
    location = "static"
    default_acl = "publicRead"


class MediaGoogleCloudStorage(GoogleCloudStorage):
    location = "media"
    file_overwrite = False
{%- elif cookiecutter.cloud_provider == 'Azure' -%}
from storages.backends.azure_storage import AzureStorage


class StaticAzureStorage(AzureStorage):
    location = "static"


class MediaAzureStorage(AzureStorage):
    location = "media"
    file_overwrite = False
{%- endif %}


{% if cookiecutter.use_whitenoise -%}
from whitenoise.storage import CompressedManifestStaticFilesStorage

class StaticRootWhiteNoiseStorage(CompressedManifestStaticFilesStorage):
    """
    A forgiving version of manifest file storage.

    Ensure you use:
    COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
    """

    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            result = super().hashed_name(name, content, filename)
        except ValueError:
            # When the file is missing, let's forgive and ignore that.
            result = name
        return result
{% endif %}
