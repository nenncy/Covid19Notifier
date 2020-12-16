#IMPORT ALL REQUIRED LIBRARIES
import requests
import time
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
n = ToastNotifier()
#for webscraping get url of required website
def getdata(url):

	r = requests.get(url)

	return r.text

#translate in html form
htmldata = getdata("https://www.worldometers.info/coronavirus/country/india/")

soup = BeautifulSoup(htmldata, 'html.parser')

#found required data from website using BeautifulSoup library

current_case = soup.find('div',{'class':'maincounter-number'}).span.text
current_death = soup.find_all('div',{'class':'maincounter-number'})[1].span.text
current_recover = soup.find_all('div',{'class':'maincounter-number'})[2].span.text

case = str(current_case)
death=str(current_death)
recover=str(current_recover)

#notification result 
result = " Total Current cases " + case + "Total death " + death +" and Total recover cases "+ recover  +" In India."

#notifier on desktop
n.show_toast("Covid-19 Update", result, duration = 20,threaded=True,icon_path="Corona.ico")
while n.notification_active():
    time.sleep(2000)
