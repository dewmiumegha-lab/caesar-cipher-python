# Coursework Assessment 1
# Name:Dewmi Umegha
# Student No:2435430

# A Caesar Cipher Program
import os.path

def welcome():
    print("Welcome to the caesar cipher")
    print ("This programe encrypts text using the caesar ciper")
    return


def enter_message():
    mode = ''
    while True:
        mode=input("Would you like to encrypt (e) or decrypt (d):").strip().lower()
        if mode in ['e','d']:
            break 
        print("Invalid Mode")
    message = input ("What message would you like to encrypt:").upper()
    while True :

        shift=int(input("What is the shift number:"))
        break
        print ("Invalid shift")
    return (mode, message, shift)


def encrypt(message,shift):
    encrypted_message=''
    for char in message:
        if char.isalpha():
            shift_amount=(ord(char)-65+shift)%26
            encrypted_message+=chr(shift_amount+65)
        else:
            encrypted_message+=char
    return encrypted_message

def decrypt(message,shift):
    decrypted_message=''
    for char in message:
        if char.isalpha():
            shift_amount=(ord(char)-65-shift)%26
            decrypted_message+=chr(shift_amount+65)
        else:
            decrypted_message+=char
    return decrypted_message

def process_file(filename, mode,shift):
    list_messages = []
    f=open(filename,'r') 

    for line in f:
        line=line.strip()
        if mode=='e':
            list_messages.append(encrypt(line.upper(),shift))
        elif mode=='d':
            list_messages.append(decrypt(line.upper(),shift))
    return list_messages


def write_messages(lines):
    
    f1=open("result.txt",'w')
    for line in lines:
        f1.write(line+'\n')
def is_file(filename):

    return os.path.isfile (filename)

def message_or_file():
    mode = ''
    filename = None
    message = None
    
    while True:
        mode=input("Would you like to encrypt (e) or decrypt (d):").strip().lower()
        if mode in ['e','d']:
            break
        print ("Invalid Mode")
    while True:
        input_method = input("Would you like to read from a file (f) or the console (c)?").strip().lower()
        if input_method=='f':
            while True:

                filename=input("Enter a filename").strip()
                if is_file (filename):
                    break
                print("Invalid File Name")
            shift=int(input("What is the shift number:"))    
            return (mode, message, filename, shift)
        elif input_method=='c':
            message =input("What message would you like to process:").upper()
            shift=int(input("What is the shift number:"))
            return(mode,message,None,shift)
        else:
            print("Invalid input.plz enter 'f' for file or 'c' for console.")

def main():
    welcome()
    while True:
        mode,message,filename,shift=message_or_file()
        if filename:
            message=process_file(filename,mode,shift)
            write_messages(message)
            print("Messages have been written to the result.txt.")
        else:
            if mode=='e':
                result=encrypt(message,shift)
            else:
                result=decrypt(message,shift)
            print(f"Result:{result}")
        while True:

            another=input("Would you like to process another message?(y/n):").strip().lower()
            if another in ['y','n']:
               break
            print("Invalid input.plz enter 'y' or 'n'.")
        if another =='n':
            print("Thank you for using the caesar ciper program,goodbye!")
            return
if __name__ == '__main__':
    main()
