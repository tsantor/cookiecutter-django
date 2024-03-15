from django.contrib.staticfiles.storage import ManifestFilesMixin
from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from storages.backends.s3boto3 import S3Boto3Storage


class ForgivingManifestStaticFilesStorage(ManifestStaticFilesStorage):
    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            # When the file is missing, let's forgive and ignore that.
            return name


class S3ManifestStaticStorage(ManifestFilesMixin, S3Boto3Storage):
    """S3 storage backend that saves the files locally, too."""
    # location = 'static'
    # default_acl = 'public-read'

    manifest_strict = False

    def hashed_name(self, name, content=None, filename=None):
        try:
            return super().hashed_name(name, content, filename)
        except ValueError:
            # When the file is missing, let's forgive and ignore that.
            return name
