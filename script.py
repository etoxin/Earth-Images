import urllib.request
import requests
from requests.exceptions import HTTPError

urls = []

for x in range(1000, 20000, 1):
    urls.append(
        ['https://www.gstatic.com/prettyearth/assets/full/' + str(x) + '.jpg', 'images/earthview_' + str(x) + '.jpg'])

for url in urls:
    try:
        print('Checking: ' + url[0])
        r = requests.get(url[0], allow_redirects=True)
        open(url[1], 'wb').write(r.content)
        r.raise_for_status()
    except HTTPError:
        print('Could not download image')
    else:
        print(r.url, 'downloaded image successfully')
