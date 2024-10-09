#Streching is onother way of making hashed password more secure but it might also be very poor
#This is done by use of libraries and one of the most used libraries is bycrypt 
#The cons is that the salt can easily be spotted and removed and later on get the hash.

import argparse
import bcrypt

#function to get the needed data for encryption
def hash_streching(data):
    try:
        salt = bcrypt.gensalt() #generates salt automatically for you
        return salt, bcrypt.hashpw(data.encode("utf-8"), salt)
    
    except Exception as hashing_error:
        return hashing_error
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="streching hashed passwords using bcrypt")
    parser.add_argument("--data", dest="data", action="store", required=True, type=str)
    
    arguments = parser.parse_args()
    print(hash_streching(data=arguments.data))
 
    
#After printing the output then you realise that the hash can be easily detected and removed from the hashed password
#This method is more prawn to bruteforcing attacks and an attacker can engineer a script to remove the salt
#Which means he will get the hash that he needs for the bruteforce.