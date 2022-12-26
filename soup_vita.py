import mechanicalsoup
from bs4 import BeautifulSoup
from playsound import playsound
import time
browser = mechanicalsoup.StatefulBrowser()
# url = 'https://www.iqstudentaccommodation.com/edinburgh/fountainbridge?year=2022-23&sorting=priceAsc'
url = 'https://www.iqstudentaccommodation.com/edinburgh/elliott-house?year=2022-23&sorting=availability'
url = 'https://www.vitastudent.com/en/student-accommodation/edinburgh/fountainbridge/room-types'
browser.open(url)
x = browser.get_current_page()

while 1:
    i=0
    texts = BeautifulSoup.find_all(x, class_= "sold_out_notice_Ew7Y-")
    for text in texts:
        # print(text.text)
        # print(len(text.text))
    # quit()
        if text.text.strip() == 'Sold out':
            i=i+1
        else:
            # print(text.text)
            while 1:
                print('FIND!!!!!!VITA')
                playsound('./Requiem.m4a')
    if i != 5:
        while 1:
            print('FIND!!!!!!VITA')
            playsound('./Requiem.m4a')
    # print(i)
    browser.refresh()
    time.sleep(10)




