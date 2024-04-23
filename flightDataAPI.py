import aeroapi_python 

def flightdata():
    api_key = 'lpMGPqwMlgA4guMGgD96g4YOc0CznoGG'
    aeroapi = aeroapi_python.AeroAPI(api_key)
    airports = aeroapi.airports
    airport_info = airports.scheduled_arrivals("MIA", "DAL")
    #print(airport_info)
    #print(airport_info.keys())
  
    for item in airport_info['scheduled_arrivals']:
        print(search_dict(item, 'ident_iata'))
        print(search_dict(item, 'aircraft_type'))
        print(search_dict(item['destination'], 'code_iata'))
        print(search_dict(item, 'route_distance'))
        print(search_dict(item, 'arrival_delay'))
        print("")

def search_dict(d, key):
     if key in d:
        return f"The value for the key '{key}' is {d[key]}"
     else:
        return "Key not found."
     
flightdata()