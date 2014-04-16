# 4-9 Book Ranking Screenscraper
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ') # searches for string
AMZN = 'http://amazon.com/dp/'
ISBNs = {
'0132269937': 'Core Python Programming',
'0132356139': 'Python Web Development with Django',
'0137143419': 'Python Fundamentals',
}

def getRanking(isbn): #Take ISBN,create finalURL and then call urlopen on it
    page = uopen('%s%s'%(AMZN,isbn)) #or str.format() i.e. '{0}{1}'.format(AMZN,isbn)
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]

def _showRanking(isbn): # Outputs ISBN and ranking to user
    print '- %r ranked %s' % (
        ISBNs[isbn], getRanking(isbn))
    
def main():
    print 'At', ctime(), 'on Amazon...'
    for isbn in ISBNs:
        #showRanking(isbn)
        Thread(target=_showRanking,args=(isbn,)).start() #Add multithreading
    print 'All Done at ' ,ctime()
        

    

main()