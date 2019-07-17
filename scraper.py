import csv
import scraperwiki

# Semicolon separated CSV:
#url = 'http://tjv.pristupinfo.hr/?sort=1&page=1&download'
#url = 'http://schlos.net/codeforcroatia.org/tijela-2019-07-17.csv'

# Comma separated CSV:
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQDRAq7dLGma-4y09syGLI7l8tacTWCu70HE7YBFLUI74dgth99kg_MPEz4ZJWi5wwuCi48bXBgiSMc/pub?gid=1362161529&single=true&output=csv'

data = scraperwiki.scrape(url)
data = data.splitlines()
reader = csv.DictReader(data)

for row in reader:
    print row
    #scraperwiki.sqlite.save(unique_keys, data=row)
    #scraperwiki.sqlite.save(['OIB'], row)
    scraperwiki.sqlite.save(row[1], data=row)

    #record['Name'] = record['Name'].decode("cp1252")
    #print "%s, %s last updated on %s" % (row[2], row[3], row[16])
    #for scraperwiki only:
    #scraperwiki.sqlite.save(['Value'], record)
    #scraperwiki.sqlite.save(unique_keys=['OIB', 'Rb.'], data=record)
