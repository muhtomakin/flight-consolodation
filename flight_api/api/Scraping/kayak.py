from Scraping.kayakPage import KayakPage
from Scraping.utils import Utils
from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys

class KayakScrape():
    def kayak_scrape(url, return_date):
        driver = webdriver.Chrome('{}'.format(chromiumdriverexe_path))
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
            times = KayakPage.sectionTimes(driver)
            stops = KayakPage.sectionStops(driver)
            company = KayakPage.sectionCompany(driver)
            durations = KayakPage.sectionDuration(driver)
            prices = KayakPage.sectionPrice(driver)
            sections_flights = {
                'times': times,
                'stops': stops,
                'company': company,
                'durations': durations,
                'prices': prices,
            }
            flights = Utils.scrape_flights(sections_flights)
            
        except Exception as e:
            print(e)

        print(flights)

        print('starting first scrape2.....')
        sleep(randint(8,10))
        KayakPage.hotelIncrementDate(driver).click()
        sleep(randint(8,10))
        KayakPage.hotelButton(driver).click()
        sleep(randint(8,10))
        KayakPage.hotelsDropdownBySort(driver).click()
        sleep(randint(2,5))
        KayakPage.hotelsBySortLowToHigh(driver).click()
        sleep(randint(8,10))
        for i in range(4):
            KayakPage.moreButton(driver).click()
            sleep(randint(5,7))
        hotelPrices = []
        className_suggest = KayakPage.hotelPriceAdd(driver, 1).get_attribute("class")
        className_normal = KayakPage.hotelPriceAdd(driver, 3).get_attribute("class")
        try:
            for i in range(23):
                indexClassName = KayakPage.hotelPriceAdd(driver, i+1).get_attribute("class")
                if className_suggest == indexClassName or className_normal == indexClassName:
                    price = KayakPage.hotelPrice(driver, i+1)
                    hotelPrices.append(price.text.split('\n')[0])

            name = KayakPage.hotelName(driver)
            reviewsScore = KayakPage.hotelReviewsScore(driver)
            reviewsDesc = KayakPage.hotelReviewsDescription(driver)
            sections_hotels = {
                'name': name,
                'reviewsScore': reviewsScore,
                'reviewsDesc': reviewsDesc,
                'hotelPrice': hotelPrices,    
            }
            hotels = Utils.scrape_hotels_kayak(sections_hotels)
            
        except:
            pass

        print(hotels)
            
        print('starting first scrape3.....')
        sleep(randint(8,10))
        KayakPage.carButton(driver).click()
        sleep(randint(5,7))
        KayakPage.carSortCheapest(driver).click()
        sleep(randint(5,7))
        
        try:
            carBrands = KayakPage.carBrands(driver)
            price = KayakPage.carPrice(driver)
            sections_cars = {
                'carBrands': carBrands,
                'price': price,
            }
            cars = Utils.scrape_cars(sections_cars)
        
        except:
            pass
        
        print(cars)

        kayak = {
            'Flights': flights,
            'Hotels': hotels,
            'Cars': cars,
        }
        
        return kayak
