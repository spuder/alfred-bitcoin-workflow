
#Created by spencer owen
#https://github.com/spudstud/alfred-bitcoin-workflow
import json
import urllib2
from xml.etree.ElementTree import Element, SubElement, Comment,  tostring


url="http://data.mtgox.com/api/2/BTCUSD/money/ticker"

jsonURL=urllib2.urlopen(url)

jsonObject=json.load(jsonURL)

currentValue    = jsonObject['data']['high']['display']
lowValue        = jsonObject['data']['low']['display']
avgValue        = jsonObject['data']['avg']['display']
lastValue       = jsonObject['data']['last']['display']
nowValue        = jsonObject['data']['now']



# use standard xml libraries instead of creating a single xml string
#print ("<items><item uid='currentPrice' arg='"+currentValue+"' valid='yes'><title>MtGox Current Price</title><subtitle>"+ currentValue +"</subtitle><icon>MtGox.png</icon></item></items>" ).encode('ascii', 'xmlcharrefreplace')
#<items>
	# <item uid='currentPrice' arg='"+currentValue+"' valid='yes'>
	# 	<title>MtGox Current Price</title>
	# 	<subtitle>"+ currentValue +"</subtitle>
	# 	<icon>MtGox.png</icon></item></items>

items = Element('items')
item = SubElement(items, 'item')
item.set('uid', 'mtgoxprice')
item.set('arg', str(currentValue))
item.set('valid', 'yes')

title = SubElement(item, 'title')
title.text = "MtGox Current Rate"

subtitle = SubElement(item, 'subtitle')
subtitle.text = str(currentValue)

icon = SubElement(item, 'icon')
icon.text = "MtGox.png"

print tostring(items)