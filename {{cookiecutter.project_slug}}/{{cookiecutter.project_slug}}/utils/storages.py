from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
{%- if cookiecutter.use_whitenoise == 'y' %}
from whitenoise.storage import CompressedManifestStaticFilesStorage
{%- endif %}
{%- if cookiecutter.cloud_provider == 'AWS' %}
from storages.backends.s3 import S3Storage
{%- endif %}

class ForgivingManifestStaticFilesStorageMixin:
    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            # When the file is missing, let's forgive and ignore that.
            return name


class ForgivingManifestStaticFilesStorage(
    ForgivingManifestStaticFilesStorageMixin,
    ManifestStaticFilesStorage,
):
    """
    A forgiving version of manifest file storage.

    Ensure you use:
    COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
    """
{%- if cookiecutter.use_whitenoise == 'y' %}


class StaticRootWhiteNoiseStorage(
    ForgivingManifestStaticFilesStorageMixin,
    CompressedManifestStaticFilesStorage,
):
    """
    A forgiving version of manifest file storage.

    Ensure you use:
    COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
    """
{%- endif %}
{%- if cookiecutter.cloud_provider == 'AWS' %}


class S3ManifestStaticFilesStorage(
    ForgivingManifestStaticFilesStorageMixin, S3Storage, ManifestStaticFilesStorage
):
    pass
{%- endif %}
