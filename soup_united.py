import mechanicalsoup
from bs4 import BeautifulSoup
from playsound import playsound
import time
browser = mechanicalsoup.StatefulBrowser()
# url = 'https://www.iqstudentaccommodation.com/edinburgh/fountainbridge?year=2022-23&sorting=priceAsc'
url = 'https://www.iqstudentaccommodation.com/edinburgh/elliott-house?year=2022-23&sorting=availability'
url = 'https://www.unitestudents.com/edinburgh'
browser.open(url)
x = browser.get_current_page()
# states = x.findall('text')
print(type(x))
# playsound('./Requiem.m4a')
while 1:
    i=0
    texts = BeautifulSoup.find_all(x, class_="sc-163ynfv-6 kRwDun")
    for text in texts:
        if text.text == 'Sold out':
            # print(1)
            i=i+1
        else:
            # print(text.text)
            print('FIND!!!!!!!!!United')
            while 1:
                playsound('./Requiem.m4a')
    if i != 4:
        print('FIND!!!!!!!!!United')
        while 1:
            playsound('./Requiem.m4a')
    # print(i)
    browser.refresh()
    time.sleep(10)




