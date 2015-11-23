#! /usr/bin/python

###############################################################################
#
# Version 0.1
#
###############################################################################

import time
import requests

URLS = [
    'http://www.appdynamics.com'
    ,'http://www.google.com'
    ,'http://google.com'
    ,'http://www.twitter.com'
    ,'http://www.google.com/asdfasdfasdf'
    ,'http://www.cnn.com'
    ,'http://www.NotARealDomainJustMadeItUpFoobar.co'
]



###############################################################################
# Don't edit below this line
###############################################################################
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

def main():
    while True:
        print "\nTesting URLs.", time.ctime()
        checkUrls()
        print "Press CTRL+C to exit"
        time.sleep(10) #Sleep 10 seconds

def checkUrls():
    for url in URLS:
        status = "N/A"
        try:
            status = checkUrl(url)
        except requests.exceptions.ConnectionError:
            status = "DOWN"

        printStatus(url, status)

def checkUrl(url):
    r = requests.get(url, timeout=5)
    #print r.status_code
    return str(r.status_code)

def printStatus(url, status):
    color = GREEN

    if status != "200":
        color=RED

    print color+status+ENDC+' '+ url

#
# Main app
#
if __name__ == '__main__':
    main()
