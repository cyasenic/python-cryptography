import threading
import sys
import time


#assigning list and an empty string to variables for storage of ascii values and data.
global ascii_list
global ascii_de_obs_list
global de_obsfucated_string

ascii_list = []
ascii_de_obs_list = []
de_obsfucated_string = ""


#own printing version of print value. just extra learning python
def printText(string):
    for letter in string:
         
         sys.stdout.write(letter)
         sys.stdout.flush()
         time.sleep(.01)


#From here the process of obsfucation of data starts
def read_append_orginal_data_to_list():
    try:
        with open(file="/home/cyasen/Desktop/python-cryptography/originalFile.txt", mode="rb") as original_file:
            data = original_file.read()
            
            for letter in data.decode():
                ascii_list.append(ord(letter))
                
        printText("[+] Reading data from file and appending ascii values to list... (sucess)\n")
                
    except Exception as read_append_original_data_list_error:
        print(read_append_original_data_list_error)


def write_obsfucated_list_data_to_file():
    try:
        with open("/home/cyasen/Desktop/python-cryptography/original_obsfucated.txt", "wb") as ascii_file:
            for ascii in ascii_list:
                ascii_file.write(str(ascii).encode()+b"\n")
                
        printText("[+] Writing obsfucated data to file... (sucess)\n")
                
    except Exception as write_obsfucated_list_data_to_file_error:
        print(write_obsfucated_list_data_to_file_error)


#from here the de_obsfucation of the data starts taking place
def read_obsfucated_file_append_data_to_list():
    try:
        with open("/home/cyasen/Desktop/python-cryptography/original_obsfucated.txt", "rb") as ascii_written_file:
            ascii_data = ascii_written_file.readlines()
            
            for line in ascii_data:
                ascii_de_obs_list.append(line.decode().strip("\n"))
                
        printText("[+] Reading obsfucated data from file and add ascii values to list... (sucess)\n")
    
    except Exception as read_obsfucated_file_append_data_to_list_error:
        printText(read_obsfucated_file_append_data_to_list_error)
        

def append_de_obsfucated_data_to_empty_string():
    try:
        global de_obsfucated_string
        for ascii in ascii_de_obs_list:    
            de_obsfucated_string += chr(int(ascii))
            
        printText("[+] Adding de_obsfucated data to empty string ready for writing... (sucess)\n")
    
    except Exception as append_de_obsfucated_data_top_empty_string_error:
        printText(append_de_obsfucated_data_top_empty_string_error)


def write_de_obsfucated_data_back_to_file():
    try:
        with open("/home/cyasen/Desktop/python-cryptography/original_de_obsfucated.txt", mode="wb") as de_obsfucated_file:
            de_obsfucated_file.write(de_obsfucated_string.encode())
            
        printText("[+] Writing the de_obsfucated data back to file in progress... (sucess)\n")
            
    except Exception as write_de_obsfucated_data_back_to_file:
        print(write_de_obsfucated_data_back_to_file)


def main():
    try:
        #creating threads to each function 
        threading.Thread(target=read_append_orginal_data_to_list()).start()
        threading.Thread(target=write_obsfucated_list_data_to_file()).start()
        threading.Thread(target=read_obsfucated_file_append_data_to_list()).start()
        threading.Thread(target=append_de_obsfucated_data_to_empty_string()).start()
        threading.Thread(target=write_de_obsfucated_data_back_to_file()).start()
        
        printText("[+] Obsufucation of file done with 100% success..Quiting now\n")
    
    except Exception as main_error:
        print(main_error)
main()
