import datetime
from playsound import playsound


print("Set an alarm \n >>")

alarmHour = int(input("Enter Hour"))
alarmMin = int(input("Enter Minute"))
alarmAm = input(" am/pm ")

if alarmAm=="pm":
    alarmAm+=12

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin== datetime.datetime.now().minute:
        print("wAke uP gOizz..")
        playsound("C:\\Users\\deven\\OneDrive\\Desktop\\SYNC Intern\\camerashutter.wav")
        break