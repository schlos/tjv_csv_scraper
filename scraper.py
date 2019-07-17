import csv
import scraperwiki

#url = 'http://tjv.pristupinfo.hr/?sort=1&page=1&download'
url = 'http://schlos.net/codeforcroatia.org/tijela-2019-07-17.csv'

data = scraperwiki.scrape(url)
data = data.splitlines()
reader = csv.DictReader(data)

for row in reader:
    print row
    #scraperwiki.sqlite.save(unique_keys, data=row)
    scraperwiki.sqlite.save(['OIB'], row)

    #record['Name'] = record['Name'].decode("cp1252")
    #print "%s, %s last updated on %s" % (row[2], row[3], row[16])
    #for scraperwiki only:
    #scraperwiki.sqlite.save(['Value'], record)
    #scraperwiki.sqlite.save(unique_keys=['OIB', 'Rb.'], data=record)
