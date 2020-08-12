import urllib.request
from bs4 import *
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter the url to scrape : ')

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

span_count = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    span_count += 1

print('Count ', span_count)
print('Sum ', sum)
