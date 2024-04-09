from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
{%- if cookiecutter.use_whitenoise == 'y' %}
from whitenoise.storage import CompressedManifestStaticFilesStorage
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
    ForgivingManifestStaticFilesStorageMixin, ManifestStaticFilesStorage
):
    """
    A forgiving version of manifest file storage.

    Ensure you use:
    COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
    """

    pass


{%- if cookiecutter.use_whitenoise == 'y' %}
class StaticRootWhiteNoiseStorage(
    ForgivingManifestStaticFilesStorageMixin, CompressedManifestStaticFilesStorage
):
    """
    A forgiving version of manifest file storage.

    Ensure you use:
    COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
    """

    pass
{%- endif %}
