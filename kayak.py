import utils
import kayakPage
from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys

def kayak_scrape(url, return_date):
    driver = webdriver.Chrome('C:/Users/muhto/Desktop/chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    sleep(randint(8,10))
    try:
        xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
        driver.find_elements_by_xpath(xp_popup_close)[5].click()
    except Exception as e:
        pass
    driver.implicitly_wait(10)
    print('starting first scrape1.....')

    try:
        times = kayakPage.sectionTimes(driver)
        stops = kayakPage.sectionStops(driver)
        company = kayakPage.sectionCompany(driver)
        durations = kayakPage.sectionDuration(driver)
        prices = kayakPage.sectionPrice(driver)
        sections_flights = {
            'times': times,
            'stops': stops,
            'company': company,
            'durations': durations,
            'prices': prices,
        }
        flights = utils.scrape_flights(sections_flights)
        
    except:
        pass

    print(flights)

    print('starting first scrape2.....')
    kayakPage.hotelButton(driver).click()
    sleep(randint(8,10))
    kayakPage.hotelsDropdownBySort(driver).click()
    sleep(randint(2,5))
    kayakPage.hotelsBySortLowToHigh(driver).click()
    sleep(randint(8,10))
    for i in range(4):
        kayakPage.moreButton(driver).click()
        sleep(randint(5,7))
    hotelPrices = []
    className_suggest = kayakPage.hotelPriceAdd(driver, 1).get_attribute("class")
    className_normal = kayakPage.hotelPriceAdd(driver, 3).get_attribute("class")
    try:
        for i in range(23):
            indexClassName = kayakPage.hotelPriceAdd(driver, i+1).get_attribute("class")
            if className_suggest == indexClassName or className_normal == indexClassName:
                price = kayakPage.hotelPrice(driver, i+1)
                hotelPrices.append(price.text.split('\n')[0])

        name = kayakPage.hotelName(driver)
        reviewsScore = kayakPage.hotelReviewsScore(driver)
        reviewsDesc = kayakPage.hotelReviewsDescription(driver)
        sections_hotels = {
            'name': name,
            'reviewsScore': reviewsScore,
            'reviewsDesc': reviewsDesc,
            'hotelPrice': hotelPrices,    
        }
        hotels = utils.scrape_hotels_kayak(sections_hotels)
        
    except:
        pass

    print(hotels)
        
    print('starting first scrape3.....')
    sleep(randint(8,10))
    kayakPage.carButton(driver).click()
    sleep(randint(5,7))
    kayakPage.carSortCheapest(driver).click()
    sleep(randint(5,7))
    
    try:
        carBrands = kayakPage.carBrands(driver)
        price = kayakPage.carPrice(driver)
        sections_cars = {
            'carBrands': carBrands,
            'price': price,
        }
        cars = utils.scrape_cars(sections_cars)
    
    except:
        pass
    
    print(cars)

    kayak = {
        'Flights': flights,
        'Hotels': hotels,
        'Cars': cars,
    }
    
    return kayak
