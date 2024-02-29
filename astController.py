import read_write_data

print("AST Controller/n")

user_input = input("\nEnter (d) for Development Mode or (u) User Mode.\n")

if(user_input.lower() == "d"):
    print("In Development Mode")
elif(user_input.lower() == "u"):
    print("In User Mode")
else:
    print("Unknown Mode")