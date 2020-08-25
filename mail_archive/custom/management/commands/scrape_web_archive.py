"""
Scrape a mailing list archive over HTTP and import into hyperkitty.

Copyright Michael Lazar 2020.
"""

import gzip
import os
import tempfile
import time

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

        matches = lxml.html.fromstring(resp.content).xpath('//a/@href')
        links = [str(m) for m in matches if str(m).endswith(self.FILE_EXTENSIONS)]

        if not options['full']:
            # Take only the 2 most recent archives, which should ensure that
            # everything is captured since the last scrape.
            links = links[:2]

        mbox_files = []

        for link in links:
            self.stdout.write(f"Found archive {link}, downloading...")
            url = os.path.join(archive_url, link)
            resp = requests.get(url)
            resp.raise_for_status()

            mbox_data = resp.content
            if link.endswith('.gz'):
                self.stdout.write("Decompressing gzip archive")
                mbox_data = gzip.decompress(resp.content)

            with tempfile.NamedTemporaryFile(delete=False) as fp:
                mbox_files.append(fp.name)
                fp.write(mbox_data)

            # Rate limit
            time.sleep(1)

        command_kwargs = {'list_address': options['list_address']}
        if options['full']:
            command_kwargs['since'] = '1980-01-01'

        call_command("hyperkitty_import", *mbox_files, **command_kwargs)
        call_command("update_index_one_list", options['list_address'])

        self.stdout.write("Cleaning up temporary files")
        for filename in mbox_files:
            os.remove(filename)
