import aeroapi_python 

def flightdata():
    api_key = 'lpMGPqwMlgA4guMGgD96g4YOc0CznoGG'
    aeroapi = aeroapi_python.AeroAPI(api_key)
    airports = aeroapi.airports
    airport_info = airports.all_flights("MIA")

    print(airport_info.keys())
    key_to_search = 'arrivals'
    print(search_dict(airport_info, key_to_search))

    #Trying to figure out how to get the delay status by looping through the dictionary of info at MIA

'''
    values = [d['operator'] for d in airport_info if 'operator' in d]
    value = values[6] if values else None
    for d in airport_info:
        if 'operator' in d:
            value = d['operator']
            break
    print(value)

    search_key = 'operator'
    result = search_nested_dict(airport_info, search_key)
    print(result)
'''
def search_dict(d, key):
     if key in d:
        return f"The value for the key '{key}' is {d[key]}"
     else:
        return "Key not found."
'''    
def search_nested_dict(nested, target):
    for key, subdict in nested.items():
        if target in subdict:
            return f"Found {target}: {subdict[target]} in {key}"
    return f"{target} not found in any sub-dictionary."
'''