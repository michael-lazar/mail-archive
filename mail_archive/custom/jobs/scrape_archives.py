from django_extensions.management.jobs import BaseJob
from django.core.management import call_command


LISTS = [
    (
        "license-discuss@lists.opensource.org",
        "http://lists.opensource.org/pipermail/license-discuss_lists.opensource.org/",
    ),
    (
        "license-review@lists.opensource.org",
        "https://lists.opensource.org/pipermail/license-review_lists.opensource.org/",
    ),
    (
        "gemini@lists.orbitalfox.eu",
        "https://lists.orbitalfox.eu/archives/gemini/",
    )
]


class Job(BaseJob):
    help = "Scrape the public mail archives"
    when = "daily"

    def execute(self):
        for list_address, archive_url in LISTS:
            call_command("scrape_web_archive", archive_url, list_address=list_address)
