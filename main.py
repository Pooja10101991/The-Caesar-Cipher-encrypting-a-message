# The Caesar Cipher
msg=input("enter the message:") #enter the message to be encrypted
shift = 0

while shift == 0:
    try:
        shift = int(input("Enter cipher's shift (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Bad shift value!")

enc="" #empty string for loading encrypted msg

for ch in msg:
    num = ord(ch) + shift
    if ch.isdigit()or ch.isspace(): #keep the digits and space as it is.
        enc+=ch
    else:
        if ch.isupper(): #for upper case letters
            if 65<=num<=90:
                enc += chr(num)
            else:
                num1 = num % 90
                enc+=chr(ord('@')+num1)
        else:
            if 97<=num<=122:  #for lower case letters
                enc+=chr(num)
            else:
                num1 = num % 122
                enc+=chr(ord('`')+num1)
print(enc) #print the encrypted message
