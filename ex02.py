#odd or even exercise

def oddeven():

    while True:
        in_number=input("Please enter a number:")
        if not in_number.isnumeric():
            print("Please enter only an integer")
            continue
        else:
            break


    if int(in_number)%4==0:
        print("The number you chose was ",in_number," and this is divisible by 4",sep="")
    elif int(in_number)%2==1:
        print("The number you chose was ",in_number," and this is an odd number",sep="")
    else:
        print("The number you chose was ",in_number," and this is an even number",sep="")

if __name__=='__main__':
    oddeven()
