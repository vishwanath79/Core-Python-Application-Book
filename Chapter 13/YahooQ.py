from urllib2 import urlopen
import csv
from time import ctime
TICKS = ('yhoo', 'dell','nke','adbe','intc')
url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv'
print '\n Prices quoted as of: %s PDT\n'% ctime()
print 'TICKER', 'PRICE', 'DATE', '        Time','  CHANGE', 'OPEN','CLOSE','   MID''   VOLUME'
u = urlopen(url % ','.join(TICKS))
for row in u:
    #print row
    tick,price,time,time2,chg,per,per2,per3,per4 = row.split(',')
    print tick,'%.2f' %float(price),time,time2,chg,per,per2,per3,per4
u.close()