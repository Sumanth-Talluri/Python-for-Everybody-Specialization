import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter url : ')

total_number = 0
sum = 0

print(f'Retrieving {url}')
xml = ur.urlopen(url).read()
print(f'Retrieved {len(xml)} characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print(f'Count: {total_number}')
print(f'Sum: {sum}')
