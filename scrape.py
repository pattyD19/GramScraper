#Sample command usage:
#>scrape.py realAccounts.csv 2300 > 2300PlusResults.csv
#will start at line 2300 in CSV file "realAccounts.csv"
#
#Need to start Chrome first with this command:
#>/Applications/Google Chrome.app/Contents/MacOS ./Google\ Chrome --remote-debugging-port=1111

#Import the Selenium and CSV libraries
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import sys
import time

#open CSV file
f = open(sys.argv[1])
csv_f = csv.reader(f)
myList = []

#process file starting at this point
intialPos = int(sys.argv[2])

#create list from CSV values in input find
rowCount = 0
for row in csv_f:
  #respect starting position in file
  if rowCount >= intialPos:
    #ignore leading '@' in the values
    myList.append(row[1][1:])
  rowCount = rowCount + 1

#sleep time
sleep_time = 45
sleep_interval = 400

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
    #print(main_url + myList[i]);
    driver.get(main_url + myList[i])
    try:
        #rkEop is class id holding "Account is private text"
        element = driver.find_element_by_class_name("rkEop")
        print(str(counter) + "," + myList[i] + ",Private",flush=True)
    except NoSuchElementException:
        try:
            #_7UhW9 is class id holding "Page is not available"
            element = driver.find_element_by_class_name("_7UhW9.x-6xq.qyrsm.KV-D4.uL8Hv.l4b0S")
            print(str(counter) + "," + myList[i] + ",DNE",flush=True)
        except NoSuchElementException:
            print(str(counter) + "," +myList[i] + ",Public",flush=True)
    #pause every sleep_interval for sleep_time amount
    if (counter != 0) and (counter % sleep_interval) == 0:
      print("<---> sleeping " + str(sleep_time))
      time.sleep(sleep_time)

#close Chrome dont want to do this since we are using same browser over runs
#driver.close
