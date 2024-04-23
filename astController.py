import read_write_data as rwd
import probability_Algorithm as pa
import WeatherAPI as wapi
import flightDataAPI as fapi
import guiController as gui

verification = False

print("\nAST Controller")

user_input = input("\nEnter (d) for Development Mode or (u) User Mode.\n")

if(user_input.lower() == "d"):
    while(verification == False):
        password_verify = input("\nEnter Password: ")
        if(password_verify.lower() == "admin1234"):
            verification = True
            print("In Development Mode.")
            break
        else:
            print("Incorrect Password.")
            continue
    
    ask_q = input("\nRun data preprocessing? (y/n)\n")
    if(ask_q.lower() == "y"):
        print("Running...")
        rwd.modifyCSV('Airline_Delay_Cause_DLJAX','New_Airline_Delay_Cause_DLJAX')
        rwd.modifyCSV('Airline_Delay_Cause_DLMCO','New_Airline_Delay_Cause_DLMCO')
        rwd.modifyCSV('Airline_Delay_Cause_DLMIA','New_Airline_Delay_Cause_DLMIA')
        rwd.modifyCSV('Airline_Delay_Cause_AAJAX','New_Airline_Delay_Cause_AAJAX')
        rwd.modifyCSV('Airline_Delay_Cause_AAMCO','New_Airline_Delay_Cause_AAMCO')
        rwd.modifyCSV('Airline_Delay_Cause_AAMIA','New_Airline_Delay_Cause_AAMIA')
        rwd.modifyCSV('Airline_Delay_Cause_SWJAX','New_Airline_Delay_Cause_SWJAX')
        rwd.modifyCSV('Airline_Delay_Cause_SWMCO','New_Airline_Delay_Cause_SWMCO')
        rwd.modifyCSV('Airline_Delay_Cause_SWMIA','New_Airline_Delay_Cause_SWMIA')
        print("Complete.")
    else:
        pass

    ask_q = input("\nInitialize Model Training? (y/n)\n")
    if(ask_q.lower() == "y"):
        print("Running...")
        pa.training_function('New_Airline_Delay_Cause_DLJAX', 'DLJAX_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_DLJAX', 'DLJAX_arrmodel', 'arr_flights')
        '''
        pa.training_function('New_Airline_Delay_Cause_DLMCO', 'DLMCO_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_DLMCO', 'DLMCO_arrmodel', 'arr_flights')
        pa.training_function('New_Airline_Delay_Cause_DLMIA', 'DLMIA_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_DLMIA', 'DLMIA_arrmodel', 'arr_flights')
        pa.training_function('New_Airline_Delay_Cause_AAJAX', 'AAJAX_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_AAJAX', 'AAJAX_arrmodel', 'arr_flights')
        pa.training_function('New_Airline_Delay_Cause_AAMCO', 'AAMCO_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_AAMCO', 'AAMCO_arrmodel', 'arr_flights')
        pa.training_function('New_Airline_Delay_Cause_AAMIA', 'AAMIA_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_AAMIA', 'AAMIA_arrmodel', 'arr_flights')
        pa.training_function('New_Airline_Delay_Cause_SWJAX', 'SWJAX_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_SWJAX', 'SWJAX_armodel', 'arr_flights')
        pa.training_function('New_Airline_Delay_Cause_SWMCO', 'SWMCO_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_SWMCO', 'SWMCO_arrmodel', 'arr_flights')
        pa.training_function('New_Airline_Delay_Cause_SWMIA', 'SWMIA_delmodel', 'arr_del15')
        pa.training_function('New_Airline_Delay_Cause_SWMIA', 'SWMIA_arrmodel', 'arr_flights')
        '''
        print(pa.controlFunction('DLJAX_delmodel', 'DLJAX_arrmodel'))
        print("Complete.")
    else:
        pass

    ask_q = input("\nCheck weather? (y/n)\n")
    if(ask_q.lower() == "y"):
        print("Running...")
        wapi.weatherCheck(input("Enter a city: "))
        print("Complete.")
    else:
        pass

    ask_q = input("\nCheck Flight Data? (y/n)\n")
    if(ask_q.lower() == "y"):
        print("Running...")
        askq_1 = input("Enter Airport Code: ")
        askq_2 = input("Enter Airline Code: ")
        print(fapi.flightdata(askq_1, askq_2))
        print("Complete.")
    else:
        pass

elif(user_input.lower() == "u"):
    print("In User Mode")
    print("Running")
    
    pa.training_function('New_Airline_Delay_Cause_DLJAX', 'DLJAX_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_DLJAX', 'DLJAX_arrmodel', 'arr_flights')
    '''
    pa.training_function('New_Airline_Delay_Cause_DLMCO', 'DLMCO_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_DLMCO', 'DLMCO_arrmodel', 'arr_flights')
    pa.training_function('New_Airline_Delay_Cause_DLMIA', 'DLMIA_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_DLMIA', 'DLMIA_arrmodel', 'arr_flights')
    pa.training_function('New_Airline_Delay_Cause_AAJAX', 'AAJAX_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_AAJAX', 'AAJAX_arrmodel', 'arr_flights')
    pa.training_function('New_Airline_Delay_Cause_AAMCO', 'AAMCO_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_AAMCO', 'AAMCO_arrmodel', 'arr_flights')
    pa.training_function('New_Airline_Delay_Cause_AAMIA', 'AAMIA_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_AAMIA', 'AAMIA_arrmodel', 'arr_flights')
    pa.training_function('New_Airline_Delay_Cause_SWJAX', 'SWJAX_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_SWJAX', 'SWJAX_armodel', 'arr_flights')
    pa.training_function('New_Airline_Delay_Cause_SWMCO', 'SWMCO_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_SWMCO', 'SWMCO_arrmodel', 'arr_flights')
    pa.training_function('New_Airline_Delay_Cause_SWMIA', 'SWMIA_delmodel', 'arr_del15')
    pa.training_function('New_Airline_Delay_Cause_SWMIA', 'SWMIA_arrmodel', 'arr_flights')
    '''
    print("Complete")
    gui.startGui()
else:
    print("Unknown Mode")