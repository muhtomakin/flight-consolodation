from copy import copy

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

initial_info_flights = {
    'Time': '',
    'Stops': '',
    'TravelCompany': '',
    'Duration': '',
    'Price': '',
}

initial_info_hotels = {
    'HotelName': '',
    'Score': '',
    'Reviews': '',
    'Price': '',
}

initial_info_cars = {
    'CarBrand': '',
    'Price': '',
}

class Utils:

    def convertTime(time):
        hour = int(time[0:2])
        if hour < 12:
            converted_time = '{}:{} am'.format(hour, time[3:])
        else:
            hour = hour - 12
            converted_time = '{}:{} pm'.format(hour, time[3:])
        return converted_time

    def get_prices(element):
        return element['Price']

    def addFlightsInfo(times, stops, company, durations, prices):
        info = copy(initial_info_flights)
        data = []
        
        r = range(len(prices))
        
        for i in r:
            info['Time'] = times[i]
            info['Stops'] = stops[i]
            info['TravelCompany'] = company[i]
            info['Duration'] = durations[i]
            info['Price'] = prices[i]
            data.append(info)
            info = copy(initial_info_flights)
        
        return data

    def scrape_flights(sections):
        times = []
        stops = []
        stopCountry = []
        company = []
        durations = []
        prices = []
        
        for section in sections:
            if section == 'prices':
                for item in sections[section]:
                    if item.text != '':
                        prices.append(int(item.text.replace('$', '')))
            if section == 'times':
                for item in sections[section]:
                    times.append(item.text)
            if section == 'stops':
                for item in sections[section]:
                    stops.append(item.text)
            if section == 'stopCountry':
                for item in sections[section]:
                    stopCountry.append(item.text)
            if section == 'company':
                for item in sections[section]:
                    company.append(item.text)
            if section == 'durations':
                for item in sections[section]:
                    durations.append(item.text)
                    

        data = Utils.addFlightsInfo(times, stops, company, durations, prices)
        
        return data

    def scrape_hotels_kayak(sections):
        info = copy(initial_info_hotels)
        data = []
        name = []
        reviewsScore = []
        reviewsDesc = []
        
        for section in sections:
            if section == 'name':
                for item in sections[section]:
                    name.append(item.text)
            if section == 'reviewsScore':
                for item in sections[section]:
                    reviewsScore.append(item.text)
            if section == 'reviewsDesc':
                for item in sections[section]:
                    reviewsDesc.append(item.text)

        r = range(len(sections['hotelPrice']))
        
        for i in r:
            info['HotelName'] = name[i]
            info['Score'] = reviewsScore[i]
            info['Reviews'] = reviewsDesc[i]
            info['Price'] = sections['hotelPrice'][i]
            data.append(info)
            info = copy(initial_info_hotels)
            
        return data
           
    def scrape_cars(sections):
        info = copy(initial_info_cars)
        data = []
        brands = []
        price = []
        
        for section in sections:
            if section == 'carBrands':
                for item in sections[section]:
                    brands.append(item.text)
            if section == 'price':
                for item in sections[section]:
                    price.append((item.text))
            
        r = range(len(sections['price']))
        
        for i in r:
            info['CarBrand'] = brands[i]
            info['Price'] = price[i]
            data.append(info)
            info = copy(initial_info_cars)
            
        return data