#exercise 01
import datetime

def questions():

    while True:
        name=input("Please enter your name: ")
        name_trimmed=name.replace(" ","")
        if not name_trimmed.isalpha():
            print("Please enter only letters for your name")
            #better try again... Return to the start of the loop
            continue
        else:
            #age was successfully parsed!
            #we're ready to exit the loop.
            break

    while True:
        try:
            age=int(input("Please enter your age: "))
        except ValueError:
            print("Please enter only integers for your age")
            continue
        else:
            break

    now=datetime.datetime.now()
    nowyear=now.year
    year_100=nowyear-age+100

    while True:
        count=int(input("Please enter a number between 1 and 10: "))
        if int(count)>10 or int(count)<1:
            print("Please enter only an integer")
            continue
        else:
            break

    for i in range(count):
        if year_100<=now.year:
            print("Hello ",name,". You turned 100 in ",year_100,". Congratulations!", sep="")
        else:
            print("Hello ",name,". You will turn 100 in the year ",year_100,".",sep="")
#
if __name__=='__main__':
    questions()
