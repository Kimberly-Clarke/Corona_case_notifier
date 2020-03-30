from plyer import notification
import requests
from bs4 import BeautifulSoup as bs
import os
import time

def notifyMe(title,message):
	notification.notify(
		title = title,
		message = message,
		app_icon = os.getcwd()+"\covid.ico",   #gets the current working directory
		timeout = 15                           #time to which the notification appear
		)
global total_case,total_death,total_rec
def getdata():
        r = requests.get("https://virusncov.com/")     #site to fetch data
        data = r.content
        soup = bs(data,'lxml')
        getdata.total_case = "Total Corona cases: %s " %(soup.h2.text.split(" ")[-1])+"\n"
        getdata.total_death = "Total Deaths: %s " %(soup.find("span",{"class":"red-text"}).text+"\n")
        getdata.total_rec = "Total Recovered: %s " %(soup.find("span",{"class":"green-text"}).text)

print("Welcome to the program.\n")
print("Do you wanna pop up the program in specific time intervals or one time?\n")
ask = int(input("Enter 1 for one time or 2  for time interval any other key to exit: "))

if ask == 1:
        print("\nfetching data\n")
        getdata()
        notifyMe("Corona stats",getdata.total_case+getdata.total_death+getdata.total_rec)
elif ask == 2:
        ti_me = int(input("\nEnter the amount of interval in minutes which the program should pop up: "))
        amount = ti_me*60
        while True:
                getdata()
                notifyMe("Corona stats",getdata.total_case+getdata.total_death+getdata.total_rec)
                print("updating..")
                time.sleep(amount)
else:
        print("\nexiting")
        sys.exit()
