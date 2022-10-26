import kayak
import opodo
import user_inputs

data_inputs = user_inputs.user_inputs()

print(data_inputs)

url_kayak = 'https://www.kayak.com/flights/VIE-MUC/2022-09-12/1adults/children-1L-11?sort=bestflight_a'

data_kayak = kayak.kayak_scrape(data_inputs['url_kayak'], data_inputs['date_kayak_return'])

print(data_kayak)

url_opodo = 'https://www.opodo.com/travel/#results/type=O;from=VIE;to=MUC;dep=2022-09-12;buyPath=FLIGHTS_HOME_SEARCH_FORM;internalSearch=true'

data_opodo = opodo.opodo_scrape(data_inputs['url_opodo'], data_inputs['date_opodo_pickup'], data_inputs['date_opodo_return'], data_inputs['city_arrival'])

print(data_opodo)



