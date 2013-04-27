#!/bin/bash
. ../lib/jsawk
curl http://data.mtgox.com/api/2/BTCUSD/money/ticker | jsawk -a 'return this.name'
