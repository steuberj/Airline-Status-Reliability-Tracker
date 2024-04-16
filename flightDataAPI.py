import aeroapi_python 

def flightdata():
    api_key = 'lpMGPqwMlgA4guMGgD96g4YOc0CznoGG'
    aeroapi = aeroapi_python.AeroAPI(api_key)

    airports = aeroapi.airports
    airport_info = airports.all_flights("MIA")
    print(airport_info)