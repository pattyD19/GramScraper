#Sunday Funday
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import sys
import time

#open CSV file
f = open(sys.argv[1])
csv_f = csv.reader(f)
myList = []

#create list from CSV values
for row in csv_f:
  #ignore leading '@' in the values
  myList.append(row[1][1:])

#show accounts about to check from CSV
print("About the check the following account total:")
print(myList.count)

#Web site base URL
main_url = "https://www.instagram.com/"
#let use chrome browser to get around instagram "page not found" nonsense

options = Options()
options.add_experimental_option("debuggerAddress","127.0.0.1:1111")
driver = webdriver.Chrome(chrome_options=options)

#Iterate through accounts from CSV file
length = len(myList)
for i in range(length):
    counter = i
    try:
        #print(main_url + myList[i]);
        driver.get(main_url + myList[i])
        #rkEop is class id holding "Account is private text"
        element = driver.find_element_by_class_name("rkEop")
        print(str(counter) + "," + myList[i] + ",Private",flush=True)
    except:
        #assume if we cant find the element and we get exception
        #that the account is public
        print(str(counter) + "," +myList[i] + ",Public",flush=True)

#clouse Chrome
#driver.close
