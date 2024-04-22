from django.conf import settings


def settings_context(request):
    return {
        "PROJECT_TITLE": settings.PROJECT_TITLE,
    }
