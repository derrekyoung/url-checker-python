# url-checker
Python scripts to check URLs

This script will iterate over the list of URLs and return the HTTP status code of connecting to that URL. 
Unreachable/down URLs will report as "DOWN".

Connecting to a URL over HTTPS that has a self-signed cert will incorrectly return that the URL is down. I might address that in the future, but it's lower on my list.

## Usage
Modify the list of URLs at the top of the script to hit the ones you care about.

`python generic-url-checker.py`

## To Do
* Add support for testing against self-signed certs
