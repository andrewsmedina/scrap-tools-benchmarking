import requests

from io import BytesIO

import rows

extract_links = rows.plugins.html.extract_links
extract_text = rows.plugins.html.extract_text


journal_url = "http://www.rondonopolis.mt.gov.br/diario-oficial/"
response = requests.get(journal_url)

packages = rows.import_from_html(BytesIO(response.content), index=10, preserve_html=True)

import pdb; pdb.set_trace()