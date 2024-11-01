from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from robots.models import Rule
from robots.models import Url

# Create URL patterns (pattern, allowed)
URLS = [
    ("/admin/", False),
    ("/media/", False),
    ("/static/", False),
    ("/accounts/", False),
    ("/", True),
]


class Command(BaseCommand):
    help = "Generate default robots.txt rules"

    def handle(self, *args, **options):
        # Delete existing rules
        Rule.objects.all().delete()

        # Retrieve the default site
        default_site = Site.objects.get_current()

        # Create or get the default rule
        default_rule, created = Rule.objects.get_or_create(robot="*")
        if created:
            default_rule.sites.add(default_site)

        # Create URL patterns and associate them with the rule
        allowed_urls = []
        disallowed_urls = []

        for pattern, allowed in URLS:
            url, _ = Url.objects.get_or_create(pattern=pattern)
            if allowed:
                allowed_urls.append(url)
            else:
                disallowed_urls.append(url)

        # Use bulk operations to add URLs to the rule
        default_rule.allowed.add(*allowed_urls)
        default_rule.disallowed.add(*disallowed_urls)

        self.stdout.write(self.style.SUCCESS("Default robots.txt rules generated"))
