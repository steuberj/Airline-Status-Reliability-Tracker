import read_write_data as rwd
import probability_Algorithm as pa
import weatherAPI as wapi
import flightDataAPI as fapi

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
        print("Initializing...")
        pa.initial_training_function('New_Airline_Delay_Cause_DLJAX', 'DLJAX_model')
        print("1")
        pa.initial_training_function('New_Airline_Delay_Cause_DLMCO', 'DLMCO_model')
        print("2")
        pa.initial_training_function('New_Airline_Delay_Cause_DLMIA', 'DLMIA_model')
        print("3")
        pa.initial_training_function('New_Airline_Delay_Cause_AAJAX', 'AAJAX_model')
        print("4")
        pa.initial_training_function('New_Airline_Delay_Cause_AAMCO', 'AAMCO_model')
        print("5")
        pa.initial_training_function('New_Airline_Delay_Cause_AAMIA', 'AAMIA_model')
        print("6")
        pa.initial_training_function('New_Airline_Delay_Cause_SWJAX', 'SWJAX_model')
        print("7")
        pa.initial_training_function('New_Airline_Delay_Cause_SWMCO', 'SWMCO_model')
        print("8")
        pa.initial_training_function('New_Airline_Delay_Cause_SWMIA', 'SWMIA_model')
        print("9")
        #pa.loaded_training_function()
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
        fapi.flightdata()
        print("Complete.")
    else:
        pass

elif(user_input.lower() == "u"):
    print("In User Mode")

    #Starts GUI and will access files as needed

else:
    print("Unknown Mode")