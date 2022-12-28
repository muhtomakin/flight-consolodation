from selenium.webdriver.common.by import By

#### Kayak Page Elements ####
class KayakPage:
    def pageTitle(driver):
        return driver.find_element(By.XPATH, '//*[@id="Nc8D"]/div/div[1]/div[2]/div[1]/div[2]/a/div')

    def flightResultsList(driver):
        resultContiner = driver.find_elements(By.XPATH, "//div[@class='searchResults']")
        return resultContiner

    def sectionStops(driver):
        return driver.find_elements(By.XPATH,'//div[@class="section stops"]/div[1]')

    def sectionStopsCountry(driver):
        return driver.find_elements(By.XPATH,'//div[@class="section stops"]/div[2]')

    def sectionTimes(driver):
        return driver.find_elements(By.XPATH,'//div[@class="section times"]/div[1]')

    def sectionCompany(driver):
        return driver.find_elements(By.XPATH,'//div[@class="section times"]/div[2]')

    def sectionDuration(driver):
        return driver.find_elements(By.XPATH,'//div[@class="section duration allow-multi-modal-icons"]/div[1]')

    def sectionPrice(driver):
        return driver.find_elements(By.XPATH,'//a[@class="booking-link "]/span[@class="price option-text"]')

    def hotelButton(driver):
        return driver.find_element(By.XPATH, '//a[@aria-label="Search for hotels"]')
    def hotelIncrementDate(driver):
        return driver.find_element(By.XPATH, '//span[@aria-label="Increment date by one day"]')
    def searchButton(driver):
        return driver.find_element(By.XPATH, '//button[@aria-label="Search"]')

    def openCalendar(driver):
        return driver.find_element(By.XPATH, '//div[@class="form-container"]/div/div/div[1]/div[1]/div[2]/div/div/div/div[3]')

    def selectDate(driver, return_date):
        return driver.find_element(By.XPATH, '//div[@aria-label="{}"]'.format(return_date))

    def hotelsDropdownBySort(driver):
        return driver.find_element(By.XPATH, '//div[@id="ResultsListSortDropdownLabel"]')

    def hotelsBySortLowToHigh(driver):
        return driver.find_element(By.XPATH, '//li[@aria-label="Price (low to high)"]')

    def hotelName(driver):
        return driver.find_elements(By.XPATH, '//div[@class="FLpo-hotel-name"]/a')

    def hotelStars(driver):
        return driver.find_elements(By.XPATH, '//div[@class="FLpo-stars"]/div')

    def hotelReviewsScore(driver):
        return driver.find_elements(By.XPATH, '//div[@class="FLpo-reviews"]/div[@class="FLpo-score FLpo-positive"]')

    def hotelReviewsDescription(driver):
        return driver.find_elements(By.XPATH, '//div[@class="FLpo-score-summary"]/div[@class="FLpo-score-description"]')

    def hotelReviewsCount(driver):
        return driver.find_elements(By.XPATH, '//div[@class="FLpo-score-summary"]/div[@class="FLpo-review-count"]')

    def hotelPriceAdd(driver, i):
        return driver.find_element(By.XPATH, '//div[@class="resultsList"]/div[2]/div/div[{}]/div'.format(i))

    def hotelPrice(driver, i):
        return driver.find_element(By.XPATH, '//div[@class="resultsList"]/div[2]/div/div[{}]/div/div/div/div[3]/div'.format(i))

    def moreButton(driver):
        return driver.find_element(By.XPATH, '//a[@class="moreButton"]')

    def carButton(driver):
        return driver.find_element(By.XPATH, '//a[@aria-label="Search for cars"]')

    def carSortCheapest(driver):
        return driver.find_element(By.XPATH, '//div[@data-content="price_a"]')

    def carBrands(driver):
        return driver.find_elements(By.XPATH, '//div[@class="MseY-title js-title"]')

    def carPrice(driver):
        return driver.find_elements(By.XPATH, '//div[@class="c4nz8"]')