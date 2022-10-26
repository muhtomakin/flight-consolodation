from errors import CityNotValid, DateIsNotInRange, DateIsNotValid, TripTypeInvalid, TravelersCountChildrenInvalidPerAdults
import datetime
import time
import utils
import requests

def user_inputs():
    params = {
        'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiYzAyYjY4ZWY1NjFhN2ZmNTQ2YTE5NzhkNjJiNjVlNzRmODAwM2M5NWQ4Y2JjOGM4MWVkZDFlYzdkMmFkMWIwNDg5OThiMTA0NDBlMWU0M2MiLCJpYXQiOjE2NjA0NjIzMTEsIm5iZiI6MTY2MDQ2MjMxMSwiZXhwIjoxNjkxOTk4MzExLCJzdWIiOiIxMDU5NCIsInNjb3BlcyI6W119.sk81tV17qpUZqDuJaU1V1S69tcme8ScDakNQjrp8ifoGgy8x4UUrLvE0irQ6Zm5oH4spNqIamUU98UQeNHhpyQ'
    }
    # cities = requests.get('https://app.goflightlabs.com/cities?access_key=YOUR_ACCESS_KEY', params)

    today = datetime.date.today()

    #### Trip Type ####
    # while True:
    #     try:
    #         # print('One-way: 1 /n/n /n/n Multi-city: 2')
    #         # trip_type = int(input("Please enter your trip type (1 - 2) : "))
    #         # if trip_type < 1 or trip_type > 2:
    #         #     raise TripTypeInvalid
    #         adults = int(input('Please enter adults (12+) traveler count:'))
    #         children = int(input('Please enter children (2-11) traveler count:'))
    #         infants = int(input('Please enter infants traveler count:'))
    #         travelers = {
    #             'adults': adults,
    #             'children': children,
    #             'infants': infants,
    #         } 
        
    #         if children + infants > adults*2 :
    #            raise TravelersCountChildrenInvalidPerAdults        
    #         else:
    #             break     
            
    #     except ValueError:
    #         print("Invalid Enter!!!")
    #     except TripTypeInvalid:
    #         print('Please enter between 1-3!!!')
    #     except TravelersCountChildrenInvalidPerAdults:
    #         print('Maximum of 2 children per adult!!!')

    while True:
        try:
            city_departure = input('Please enter departure location:')
            city_departure_code = requests.get('https://app.goflightlabs.com/cities?access_key=YOUR_ACCESS_KEY&search={}'.format(city_departure), params).json()
            if type(city_departure_code) == dict:
                raise CityNotValid
            if type(city_departure_code) == list:
                city_departure_code = city_departure_code[0]['iata_code']

            city_arrival = input('Please enter arrival location:')
            city_arrival_code = requests.get('https://app.goflightlabs.com/cities?access_key=YOUR_ACCESS_KEY&search={}'.format(city_arrival), params).json()
            if type(city_arrival_code) == dict:
                raise CityNotValid
            if type(city_arrival_code) == list:
                city_arrival_code = city_arrival_code[0]['iata_code']
            cities = '{}-{}'.format(city_departure_code, city_arrival_code)
            
            year = int(input('Please enter Year:'))
            month = input('Please enter Month:')
            if month.lower() in utils.months:
                i = utils.months.index(month)  
                month = i+1 
            day = int(input('Please enter your Date:')) 
            
            date = '{}/{}/{}'.format(month, day, year)
            if datetime.date(year, int(month), day) < today:
                raise DateIsNotValid
            if time.strptime(date, '%m/%d/%Y'):
                if int(month) < 10:
                    month = '0{}'.format(month)
                date = '{}-{}-{}'.format(year, month, day) 
                break
            picked_date = datetime.date(year, int(month), day).toordinal()
            current_date = datetime.date.today().toordinal()
            if picked_date - current_date > 40:
                raise DateIsNotInRange
                
        except ValueError:
            print('Invalid Date!!!')
        except CityNotValid:
            print('Please enter valid city!!!')
        except DateIsNotValid:
            print('Please do not enter previous date!!!')
        except DateIsNotInRange:
            print('Please enter at most 40 days later!!!')
            
    date_opodo_pickup = '{} {} {}'.format(day, utils.months[int(month)-1], year)
    date_opodo_return = '{} {} {}'.format(day+1, utils.months[int(month)-1], year)
    date_kayak_return = '{} {} {}'.format(day+1, utils.months[int(month)-1], year)
    url_kayak = 'https://www.kayak.com/flights/'
    url_opodo = 'https://www.opodo.com/travel/#results/type=O;'

    #if trip_type == 1:
    #if travelers['adults'] == 1 and travelers['children'] == 0 and travelers['infants'] == 0:
    url_kayak += '{}/{}?sort=bestflight_a'.format(cities, date)
    url_opodo += 'from={};to={};dep={};buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true'.format(city_departure_code, city_arrival_code, date)
    #elif travelers['adults'] > 1 and travelers['children'] == 0 and travelers['infants'] == 0:
    #     url_kayak += '{}/{}/{}adults?sort=bestflight_a'.format(cities, date, travelers['adults'])
    #     url_opodo += 'from={};to={};dep={};adults={};buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true'.format(city_departure_code, city_arrival_code, date, travelers['adults'])
    # else:
    #     children_count = '-11'*travelers['children']
    #     infants_count = '-1L'*travelers['infants']
    #     children_url = infants_count + children_count
    #     url_kayak += '{}/{}/{}adults/children{}?sort=bestflight_a'.format(cities, date, travelers['adults'], children_url)
    #     url_opodo += 'from={};to={};dep={};adults={};children={};infants={};buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true'.format(city_departure_code, city_arrival_code, date, travelers['adults'], travelers['children'], travelers['infants'])
        

    print(url_kayak)
    print(url_opodo)
    
    data = {
        'url_kayak': url_kayak,
        'url_opodo': url_opodo,
        'city_arrival': city_arrival,
        'date_opodo_pickup': date_opodo_pickup,
        'date_opodo_return': date_opodo_return,
        'date_kayak_return': date_kayak_return,
    }
    
    return data
    
    # https://www.opodo.com/travel/#results/type=O;from=VIE;to=MUC;dep=2022-09-12;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true
    # https://www.opodo.com/travel/#results/type=O;from=VIE;to=MUC;dep=2022-09-12;adults=2;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true
    # https://www.opodo.com/travel/#results/type=O;from=VIE;to=MUC;dep=2022-09-12;adults=2;children=1;infants=1;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true
    # https://www.opodo.com/travel/#results/type=O;from=VIE;to=MUC;dep=2022-09-12;children=1;infants=1;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true
    # https://www.opodo.com/travel/#results/type=O;from=VIE;to=MUC;dep=2022-09-12;adults=2;children=1;infants=1;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true