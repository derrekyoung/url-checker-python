#! /usr/bin/python

###############################################################################
#
# Version 0.1
#
###############################################################################

import time
import requests

# Use the hostname, not the host:port or the full protocol:host:port.
# If you only have 1 Controller then change this to specify one 1. Same for the rest of the components.
CONTROLLER_HOSTNAMES = [
    'controller'
    ,'controller-primary'
    ,'controller-secondary'
]
EUM_SERVER_HOSTNAMES=[
    'eum-server'
]
EVENTS_SERVICE_HOSTNAMES=[
    'events-service0'
    ,'events-service1'
    ,'events-service2'
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
    urls = getUrls(CONTROLLER_HOSTNAMES, EUM_SERVER_HOSTNAMES, EVENTS_SERVICE_HOSTNAMES)
    for url in urls:
        status = ""
        try:
            status = checkUrl(url)
        except requests.exceptions.ConnectionError:
            status = "DOWN"

        printStatus(url, status)

def getUrls(controllers, eums, events):
    urls =[]
    replace="REPLACE_ME"

    controller_urls = [
        'http://'+replace+':8090/controller/login.html'
        #,'https://'+replace+':8181/controller/'
        #,'https://'+replace+':8181/controller/login.html'
        ,'http://'+replace+':9080/_ping'
        ,'http://'+replace+':9081/healthcheck?pretty=true'
    ]
    eum_urls = [
        'http://'+replace+':7001/eumcollector/ping'
        ,'http://'+replace+':7001/eumcollector/get-version'
        ,'http://'+replace+':7001/eumaggregator/ping'
        ,'http://'+replace+':7001/eumaggregator/licenseusage'
        ,'http://'+replace+':7001/eumaggregator/get-version'
        ,'http://'+replace+':7001/eumaggregator/beacon'
    ]
    es_urls = [
        'http://'+replace+':9080/_ping'
        ,'http://'+replace+':9081/healthcheck?pretty=true'
        ,'http://'+replace+':9200/appdynamics_accounts/_search?pretty=true'
    ]

    # Replace the controller hostnames in the controller URLs
    for host in controllers:
        for url in controller_urls:
            urls.append( url.replace(replace, host) )

    # Replace the EUM hostnames in the EUM URLs
    for host in eums:
        for url in eum_urls:
            urls.append( url.replace(replace, host) )

    # Replace the Events Service hostnames in the Events Service URLs
    for host in events:
        for url in es_urls:
            urls.append( url.replace(replace, host) )

    #print urls
    return urls

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
