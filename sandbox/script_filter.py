
# Created by spencer owen
# https://github.com/spudstud/alfred-bitcoin-workflow

# User can change which number(s) are returned by editing currentValue

import json
import urllib2
from xml.etree.ElementTree import Element, SubElement, Comment,  tostring

# Api v2 url for rates
url="http://data.mtgox.com/api/2/BTCUSD/money/ticker"
jsonURL=urllib2.urlopen(url)
jsonObject=json.load(jsonURL)


# mtgox json datastream returns many statistics
# Setting values for future convience, not actually used in this script
highValue    	= jsonObject['data']['high']['display']
lowValue        = jsonObject['data']['low']['display']
avgValue        = jsonObject['data']['avg']['display']
vwapValue       = jsonObject['data']['vwap']['display']
volValue		= jsonObject['data']['vol']['display']
last_localValue	= jsonObject['data']['last_local']['display']
last_origValue	= jsonObject['data']['last_orig']['display']
last_all 		= jsonObject['data']['last_all']['display']
lastValue       = jsonObject['data']['last']['display']
buyValue		= jsonObject['data']['buy']['display']
sellValue		= jsonObject['data']['sell']['display']
nowValue        = jsonObject['data']['now'] # now does not contain subfields

# Change curentValue to equal which ever datastream value you wish to display when executed
# defautl is lastValue
currentValue = lastValue



# Create a single string with xml data (bad practice)
#print ("<items><item uid='currentPrice' arg='"+currentValue+"' valid='yes'><title>MtGox Current Price</title><subtitle>"+ currentValue +"</subtitle><icon>MtGox.png</icon></item></items>" ).encode('ascii', 'xmlcharrefreplace')

#<items>
	# <item uid='currentPrice' arg='"+currentValue+"' valid='yes'>
	# 	<title>MtGox Current Price</title>
	# 	<subtitle>"+ currentValue +"</subtitle>
	# 	<icon>MtGox.png</icon></item></items>

# Create a xml object that matches the documentaion ^
# http://www.alfredforum.com/topic/5-generating-feedback-in-workflows/

items = Element('items')

item = SubElement(items, 'item')
item.set('uid', 'mtgoxprice')
item.set('arg', str(currentValue)) # arg allows you to pass a string to other displays (notification center)
item.set('valid', 'yes')

title = SubElement(item, 'title')
title.text = "MtGox Current Rate"

subtitle = SubElement(item, 'subtitle')
subtitle.text = str(currentValue)

icon = SubElement(item, 'icon')
icon.text = "MtGox.png"

print tostring(items)
