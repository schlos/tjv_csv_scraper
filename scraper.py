import scraperwiki
import csv

url = 'http://tjv.pristupinfo.hr/?sort=1&page=1&download'

data = scraperwiki.scrape(url)
data = data.splitlines()
#reader = csv.DictReader(data)

csv_reader = csv.DictReader(data, delimiter=';')

for record in csv_reader:
    print record 
    #for scraperwiki only:
    scraperwiki.sqlite.save(['OIB'], record) 
