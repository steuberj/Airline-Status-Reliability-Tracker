import aeroapi_python 

def flightdata():
    flightinfo = []

    api_key = 'lpMGPqwMlgA4guMGgD96g4YOc0CznoGG'
    aeroapi = aeroapi_python.AeroAPI(api_key)
    airports = aeroapi.airports
    airport_info = airports.scheduled_arrivals("MIA", "DAL")
    #print(airport_info
    #print(airport_info.keys())
    flightinfo = []
    for item in airport_info['scheduled_arrivals']:
      flightinfo.append(search_dict(item, 'ident_iata'))
      flightinfo.append(search_dict(item, 'aircraft_type'))
      flightinfo.append(search_dict(item['destination'], 'code_iata'))
      flightinfo.append(search_dict(item, 'route_distance'))
      flightinfo.append(search_dict(item, 'arrival_delay'))
      #print("")

    return flightinfo

def search_dict(d, key):
     if key in d:
        return f"{d[key]}"
     else:
        return "Key not found."
     
print(flightdata())