from Scraping.kayak import KayakScrape
from selenium import webdriver
from time import sleep
from random import randint
import requests

class GetDatas:
    
    def allCitiesCreateData():
        params = {
            'access_key': '{}'.format(API_KEY)
        }
        
        allCities = requests.get('https://app.goflightlabs.com/cities?access_key={}'.format(params['access_key'])).json()
        if (allCities['success'] == True):
            allCities = allCities['data']
            return allCities

    def data_inputs(cities, date):
        url_kayak = 'https://www.kayak.com/flights/{}/{}?sort=bestflight_a'.format(cities, date)
        return KayakScrape.kayak_scrape(url_kayak, date)






