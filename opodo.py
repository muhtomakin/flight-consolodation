import utils
import opodoPage
from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys

def opodo_scrape(url, pickup_date, return_date, city_arrival):
    driver = webdriver.Chrome('C:/Users/muhto/Desktop/chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    sleep(randint(8,10))

    print('starting first scrape1.....')

    sleep(randint(5,6))
    opodoPage.agreeCloseButton(driver).click()
    sleep(randint(5,6))
    opodoPage.flightCheapestButton(driver).click()
    sleep(randint(5,6))
    time_arrive = []
    time_departure = []
    times_opodo = []
    stops_opodo = []
    company_opodo = []
    duration_opodo = []
    prices_opodo = []
    sleep(randint(8,10))

    try:
        for i in range(7):
            opodo_prime = opodoPage.flightOpodoPrime(driver, i+1)
            deal = opodoPage.flightCardDeal(driver, i+1)
            if len(opodo_prime) == 2:
                times_arrive = opodoPage.flightArriveOpodoPrimeSkip(driver, i+1)
                times_departure = opodoPage.flightDepartureOpodoPrimeSkip(driver, i+1)
                stops = opodoPage.flightStopsOpodoPrimeSkip(driver, i+1)
                company = opodoPage.flightCompanyOpodoPrimeSkip(driver, i+1)
                duration = opodoPage.flightDurationOpodoPrimeSkip(driver, i+1)
                price = opodoPage.flightPriceOpodoPrimeSkip(driver, i+1)
            elif len(deal) == 2:
                times_arrive = opodoPage.flightArriveDealSkip(driver, i+1)
                times_departure = opodoPage.flightDepartureDealSkip(driver, i+1)
                stops = opodoPage.flightStopsDealSkip(driver, i+1)
                company = opodoPage.flightCompanyDealSkip(driver, i+1)
                duration = opodoPage.flightDurationDealSkip(driver, i+1)
                price = opodoPage.flightPriceDealSkip(driver, i+1)
            elif len(deal) == 2 and len(opodo_prime) == 2:
                company = opodoPage.flightCompanyPrimeAndDealSkip(driver, i+1)
            else:
                times_arrive = opodoPage.flightArrive(driver, i+1)
                times_departure = opodoPage.flightDeparture(driver, i+1)
                stops = opodoPage.flightStops(driver, i+1)
                company = opodoPage.flightCompany(driver, i+1)
                duration = opodoPage.flightDuration(driver, i+1)
                price = opodoPage.flightPrice(driver, i+1)
            sleep(randint(1,2))
            convert_times_arrive = utils.convertTime(times_arrive.text)
            time_arrive.append(convert_times_arrive)
            convert_times_departure = utils.convertTime(times_departure.text)
            time_departure.append(convert_times_departure)
            flight_time = '{} - {}'.format(time_departure[i], time_arrive[i])
            times_opodo.append(flight_time)
            stops_opodo.append(stops.text)
            company_opodo.append(company.text.replace('· ', ''))
            duration_opodo.append(duration.text.replace("'", ""))
            prices_opodo.append(price.text)
            
    except:
        pass
    
    flights = utils.addFlightsInfo(
        times_opodo,
        stops_opodo,
        company_opodo,
        duration_opodo,
        prices_opodo,       
    )
        
    print(flights)

    driver.close()

    driver = webdriver.Chrome('C:/Users/muhto/Desktop/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://www.opodo.com/home/')
    sleep(randint(8,10))
    opodoPage.agreeCloseButton(driver).click()
    sleep(randint(8,10))
    opodoPage.hotelButton(driver).click()
    sleep(randint(8,10))
    opodoPage.hotelPageInputCity(driver).send_keys(city_arrival)
    opodoPage.hotelPageSearchButton(driver).click()
    sleep(randint(8,10))
    opodoPage.hotelSelectDateCalendarOpen(driver).click()
    sleep(randint(2,3))
    opodoPage.hotelSelectDate(driver, pickup_date).click()
    opodoPage.hotelSearchAfterDate(driver).click()
    sleep(randint(8,10))
    opodoPage.hotelSort(driver).click()
    sleep(randint(2,3))
    opodoPage.hotelLowestButton(driver).click()
    sleep(randint(8,10))
    
    try:
        hotelName = opodoPage.hotelName(driver)
        hotelScore = opodoPage.hotelScore(driver)
        hotelReview = opodoPage.hotelReview(driver)
        hotelPrice = opodoPage.hotelPrice(driver)        
    except:
        pass
    
    sections_opodo = {
        'name': hotelName,
        'reviewsScore': hotelScore,
        'reviewsDesc': hotelReview,
        'hotelPrice': hotelPrice,    
    }
    
    hotels = utils.scrape_hotels_opodo(sections_opodo)

    print(hotels)
    opodoPage.carButton(driver).click()
    sleep(randint(12,15))
    opodoPage.carPageDestinationInput(driver).send_keys(city_arrival)
    sleep(randint(2,3))
    opodoPage.carPageDestinationInput(driver).send_keys(Keys.ARROW_DOWN)
    sleep(randint(2,3))
    opodoPage.carPageDestinationInput(driver).send_keys(Keys.ENTER)

    opodoPage.carPickUpDateOpenCalendar(driver).click()
    opodoPage.carSelectDate(driver, pickup_date).click()
    sleep(randint(2,3))
    opodoPage.carReturnDateOpenCalendar(driver).click()
    opodoPage.carSelectDate(driver, return_date).click()
    sleep(randint(2,3))
    opodoPage.carPageSearchButton(driver).click()
    sleep(randint(8,10))
    
    try:
        carBrands = opodoPage.carBrands(driver)
        carPrice = opodoPage.carPrice(driver)        
    except:
        pass
    
    sections_cars_opodo = {
        'carBrands': carBrands,
        'price': carPrice,
    }
    cars = utils.scrape_cars(sections_cars_opodo)
    
    print(cars)
    
    opodo = {
        'Flights': flights,
        'Hotels': hotels,
        'Cars': cars,
    }
    
    return opodo