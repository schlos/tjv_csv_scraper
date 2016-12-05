import scraperwiki
import csv

url = 'http://tjv.pristupinfo.hr/?sort=1&page=1&download'

data = scraperwiki.scrape(url)
data = data.splitlines()
reader = csv.DictReader(data)

for row in reader:
    scraperwiki.sqlite.save(unique_keys=[""], data=row)

    #record['Name'] = record['Name'].decode("cp1252")
    #print "%s, %s last updated on %s" % (row[2], row[3], row[16])
    #for scraperwiki only:
    #scraperwiki.sqlite.save(['Value'], record)
    #scraperwiki.sqlite.save(unique_keys=['OIB', 'Rb.'], data=record)
