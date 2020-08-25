"""
Scrape a mailing list archive over HTTP and import into hyperkitty.

Usage:
    python manage.py scrape_web_archive \
        https://lists.orbitalfox.eu/archives/gemini/ \
        --list-address gemini@lists.orbitalfox.eu

Copyright Michael Lazar 2020.
"""
import gzip
import os
import tempfile

from django.core.management.base import BaseCommand
from django.core.management import call_command
import requests
import lxml.html


class Command(BaseCommand):
    help = 'Downloads mail archives from a public website'

    FILE_EXTENSIONS = (".txt", ".txt.gz")

    def add_arguments(self, parser):
        parser.add_argument(
            "archive_url",
            help="the full URL of the pipermail archive page")
        parser.add_argument(
            '--list-address',
            help="the full list address the mailbox will be imported to")
        parser.add_argument(
            "--full", action="store_true",
            help="download all archives, instead of only the most recent")

    def handle(self, archive_url, **options):

        resp = requests.get(archive_url)
        resp.raise_for_status()

        update_index = False

        html = lxml.html.fromstring(resp.content)
        for match in html.xpath('//a/@href'):
            link = str(match)
            if link.endswith(self.FILE_EXTENSIONS):
                self.stdout.write(f"Found archive {link}, downloading...")
                update_index = True

                url = os.path.join(archive_url, link)
                resp = requests.get(url)
                resp.raise_for_status()

                mbox_data = resp.content
                if link.endswith('.gz'):
                    self.stdout.write("Decompressing gzip archive")
                    mbox_data = gzip.decompress(resp.content)

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(mbox_data)
                    fp.flush()

                    list_address = options['list_address']
                    call_command("hyperkitty_import", fp.name, list_address=list_address)

                if not options['full']:
                    break

        if update_index:
            call_command("update_index_one_list", list_address)
