from selenium.webdriver.common.by import By

def opodo_logo(driver):
    return driver.find_element(By.XPATH, '//*[@id="logo"]')

def agreeCloseButton(driver):
    return driver.find_element(By.XPATH, '//button[@aria-label="Agree and close: Agree to our data processing and close"]')

def flightCheapestButton(driver):
    return driver.find_element(By.XPATH, '//*[@id="sorting-tab-cheapest"]/div')

def flightListContainer(driver):
    return driver.find_elements(By.XPATH, '//div[@id="results_list_container"]/div/div/div[1]/div')

def flightOpodoPrime(driver, i):
    return driver.find_elements(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div'.format(i))

def flightPrice(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div/div/div/div/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div/span'.format(i))

def flightPriceOpodoPrimeSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div[2]/div/div/div/div/div/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div/span'.format(i))

def flightPriceDealSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div[2]/div/div/div/div[3]/div/div[3]/div/div/div[1]/div/div[2]/div/span'.format(i))                                      
                                                                          
def flightStops(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/span[2]'.format(i))

def flightStopsDealSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/span[2]'.format(i))

def flightStopsOpodoPrimeSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/span[2]'.format(i))

def flightCompany(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div'.format(i))

def flightCompanyOpodoPrimeSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div'.format(i))

def flightCompanyDealSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div'.format(i))

def flightCompanyPrimeAndDealSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div[2]/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div'.format(i))

def flightDuration(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/span[1]'.format(i))

def flightDurationOpodoPrimeSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/span[1]'.format(i))

def flightDurationDealSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/span[1]'.format(i))
                                          
def flightDeparture(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div'.format(i))
                                          
def flightArrive(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1]'.format(i))
                          
def flightCardDeal(driver, i):
    return driver.find_elements(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div'.format(i))
                
def flightArriveDealSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1]'.format(i))

def flightDepartureDealSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div'.format(i))

def flightArriveOpodoPrimeSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1]'.format(i))

def flightDepartureOpodoPrimeSkip(driver, i):
    return driver.find_element(By.XPATH, '//*[@id="results_list_container"]/div/div/div[1]/div[{}]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div'.format(i))
  
def hotelButton(driver):
    return driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/div/div[2]/a')
  
def hotelPageInputCity(driver):
    return driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/form/div/div[1]/div/div[1]/label/input')

def hotelPageSearchButton(driver):
    return driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div/div/div/div/form/div/div[4]/div[2]/button')

def hotelSelectDateCalendarOpen(driver):
    return driver.find_element(By.XPATH, '//button[@data-testid="date-display-field-start"]')

def hotelSelectDate(driver, date):
    return driver.find_element(By.XPATH, '//span[@aria-label="{}"]'.format(date))

def hotelSearchAfterDate(driver):
    return driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/div[2]/div[1]/div[1]/div/div/form/div/div[6]/div/button')

def hotelSort(driver):
    return driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]')

def hotelLowestButton(driver):
    return driver.find_element(By.XPATH, '//div[@data-testid="sorters-dropdown"]/div/div/div/ul/li[3]/button')

def hotelName(driver):
    return driver.find_elements(By.XPATH, '//div[@data-testid="title"]')

def hotelScore(driver):
    return driver.find_elements(By.XPATH, '//div[@data-testid="review-score"]/div[1]')

def hotelReview(driver):
    return driver.find_elements(By.XPATH, '//div[@data-testid="review-score"]/div[2]/div[1]')

def hotelPrice(driver):
    return driver.find_elements(By.XPATH, '//div[@data-testid="price-and-discounted-price"]/span')

def carButton(driver):
    return driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/header/div/div/div/div/div[1]/div/ul/li[5]/a')

def carPageSearchButton(driver):
    return driver.find_element(By.XPATH, '/html/body/article[1]/div/div/div/section/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[12]/ct-search-button/div/button')

def carPageDestinationInput(driver):
    return driver.find_element(By.XPATH, '/html/body/article[1]/div/div/div/section/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[4]/div/div/div/input')

def carPickUpDateOpenCalendar(driver):
    return driver.find_element(By.XPATH, '//*[@id="pickupDate"]')

def carReturnDateOpenCalendar(driver):
    return driver.find_element(By.XPATH, '//*[@id="returnDate"]')

def carSelectDate(driver, date):
    return driver.find_element(By.XPATH, '//td[@aria-label="{}"]'.format(date))

def carBrands(driver):
    return driver.find_elements(By.XPATH, '//div[@data-auto-id="ct-vehicle-block-title"]/h3')

def carPrice(driver):
    return driver.find_elements(By.XPATH, '//ct-vehicle-block-price-total-amount/div/div')


# //*[@id="results_list_container"]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1] ## deal
# //*[@id="results_list_container"]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1] ## prime
# //*[@id="results_list_container"]/div/div/div[1]/div[5]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1]    ## normal
# //*[@id="results_list_container"]/div/div/div[1]/div[9]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1]
# //*[@id="results_list_container"]/div/div/div[1]/div[8]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div/div[1]
