import scraperwiki
import csv

url = 'http://tjv.pristupinfo.hr/?sort=1&page=1&download'

data = scraperwiki.scrape(url)
data = data.splitlines()
reader = csv.DictReader(data)

for record in reader:
    #record['Name'] = record['Name'].decode("cp1252")
    print record 
    #for scraperwiki only:
    scraperwiki.sqlite.save(['Value'], record) 
