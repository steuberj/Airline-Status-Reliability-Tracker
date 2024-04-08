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
        rwd.modifyCSV
        print("Complete.")
    else:
        pass

    ask_q = input("\nInitialize Model Training? (y/n)\n")
    if(ask_q.lower() == "y"):
        print("Initializing...")
        pa.initial_training_function()
        pa.loaded_training_function()
    else:
        pass

    ask_q = input("\nCheck weather? (y/n)\n")
    if(ask_q.lower() == "y"):
        print("Running...")
        wapi.weatherCheck(input("Enter a city: "))
        print("Complete.")
    else:
        pass

elif(user_input.lower() == "u"):
    print("In User Mode")

    #Starts GUI and will access files as needed

else:
    print("Unknown Mode")