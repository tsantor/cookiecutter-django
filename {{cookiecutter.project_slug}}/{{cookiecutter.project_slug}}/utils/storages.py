from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
{%- if cookiecutter.use_whitenoise == 'y' %}
from whitenoise.storage import CompressedManifestStaticFilesStorage
{%- endif %}
{%- if cookiecutter.cloud_provider == 'AWS' %}
from storages.backends.s3boto3 import S3ManifestStaticStorage
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
    pass
{%- if cookiecutter.use_whitenoise == 'y' %}


class StaticRootWhiteNoiseStorage(
    ForgivingManifestStaticFilesStorageMixin,
    CompressedManifestStaticFilesStorage,
):
    pass
{%- endif %}
{%- if cookiecutter.cloud_provider == 'AWS' %}


class ForgivingS3ManifestStaticStorage(
    ForgivingManifestStaticFilesStorageMixin,
    S3ManifestStaticStorage,
):
    pass

{%- endif %}
