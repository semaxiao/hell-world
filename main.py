# -*- coding:utf-8 -*-
import requests
import json

def getprice():
	url = "https://tiger-wkgk.matchbyte.net/wkapi/v1.0/flightsearch"


	data = {
		'adults': '2',
		'children': '0',
		'infants': '0',
		'originStation': 'TPE',
		'originStation': 'NGO',
		'destinationStation': 'NGO',
		'destinationStation': 'TPE',
		'departureDate': '2018-05-05',
		'departureDate': '2018-05-12',
		'includeoverbooking': 'false',
		'daysBeforeAndAfter': '4',
		'locale': 'zh-TW'
	} 

	res = requests.get(url, params=data)
	print (type(res.text))
	data = json.loads(res.text)
	
	for target in data['journeyDateMarkets'][0]['lowFares']['lowestFares']:
		print (target)
		
		
if __name__ == '__main__':
	getprice()		