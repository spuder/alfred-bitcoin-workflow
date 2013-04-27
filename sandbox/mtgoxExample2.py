#Created by specer owen
#https://github.com/spudstud/alfred-bitcoin-workflow
import json
import urllib2

url="http://data.mtgox.com/api/2/BTCUSD/money/ticker"


jsonURL=urllib2.urlopen(url)

jsonObject=json.load(jsonURL)

currentValue 	= jsonObject['data']['high']['display']
lowValue	= jsonObject['data']['low']['display']
avgValue 	= jsonObject['data']['avg']['display']
lastValue 	= jsonObject['data']['last']['display']
nowValue 	= jsonObject['data']['now']

#Sometimes your json is not a string,you will need to use json.load, not json.loads:

print jsonObject
print currentValue
print lowValue
print avgValue
print lastValue
print nowValue
