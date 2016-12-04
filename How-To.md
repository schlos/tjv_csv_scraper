For detailed description read [the post](http://scraping.pro/how-to-scrape-csv-data-files/)

# How to scrape CSV data files

This short post in to guide you in how to scrape CSV data files. You may ask, why do we need this scrape if those data are already in files? The answer is that you might need to spend quite a lot of time in downloading the files into one place and sorting or merging them.

Python’s CSV library is well able to do a lot of the work for you. Another handy tool is the ScraperWiki toolset and library. So, even if you don’t have much ability in programing, you can adopt a scraper, adjust it for your situation and get data scraped and saved into SQLite database in ScraperWiki for further download. Also you could generate a view from your data scraped.

First of all I got a CSV scrape guide from ScraperWiki: [here](https://classic.scraperwiki.com/scrapers/csv_files_scraper/).

## Basic steps

Scrape the target web file into variable ‘data‘ by the url of the file:

```
import csv
import scraperwiki
url = 'https://docs.google.com/spreadsheet/pub?key=0AmNIZgbwy5TmdENjMmZ2cm5VQXJJMWlQVENIek5Ta2c&amp;output=csv'
data = scraperwiki.scrape(url)
```

However, in pure Python we need to use ‘urllib2′ library instead of ‘scraperwiki’:

```
import urllib2
import csv
url = 'https://docs.google.com/spreadsheet/pub?key=0AmNIZgbwy5TmdENjMmZ2cm5VQXJJMWlQVENIek5Ta2c&amp;output=csv'
data = urllib2.urlopen(url)
```

Split lines from CSV library using ‘splitlines’ method (only in ScraperWiki):

```
data = data.splitlines()
```

and put them into a CSV object called ‘reader‘:

```
reader = csv.DictReader(data)
```

After that we loop over the lines in the ‘reader‘ object to print and/or save them into database:

```
for record in reader:
   print record
   #for scraperwiki only:
   scraperwiki.sqlite.save(['Value'], record)
```

Another [scraper guide](https://classic.scraperwiki.com/docs/python/python_csv_guide/), and [another](https://github.com/scraperwiki/code-scraper-in-browser-tool/wiki/CSV-reading-guide-(Python)).
