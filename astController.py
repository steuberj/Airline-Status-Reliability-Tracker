import read_write_data as rwd
import probability_Algorithm as pa

print("AST Controller\n")

user_input = input("\nEnter (d) for Development Mode or (u) User Mode.\n")

if(user_input.lower() == "d"):
    print("In Development Mode")

    ask_q = input("\nInitialize Model Training? (y/n)\n")
    if(ask_q.lower() == "y"):
        print("Initializing...")
        pa.initial_training_function()
        pa.loaded_training_function()
    else:
        print("Rerun and try again.")

    
elif(user_input.lower() == "u"):
    print("In User Mode")
else:
    print("Unknown Mode")