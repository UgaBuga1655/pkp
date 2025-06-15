from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from random import randint

def show_class(driver, class_name):
    driver.execute_script(f'Array.from(document.getElementsByClassName("{class_name}")).forEach((el)=>el.style.display = "block")')


def get_trips_at(driver, check_time):
    date = check_time.strftime('%d%m%Y%H%M')
    driver.get(f'https://bilkom.pl/podroz?basketKey=&carrierKeys=PZ%2CP2%2CP1%2CP5%2CP7%2CP9%2CP0%2CO1%2CP4%2CP3&trainGroupKeys=G.EXPRESS_TRAINS%2CG.FAST_TRAINS%2CG.REGIONAL_TRAINS&returnForOrderKey=&fromStation=Krak%C3%B3w+G%C5%82%C3%B3wny&poczatkowa=A%3D1%40O%3DKrak%C3%B3w+G%C5%82%C3%B3wny%40X%3D19947423%40Y%3D50067192%40U%3D55%40L%3D5100028%40B%3D1%40p%3D1749820732%40&toStation=Warszawa+Centralna&docelowa=A%3D1%40O%3DWarszawa+Centralna%40X%3D21003233%40Y%3D52228864%40U%3D55%40L%3D5100065%40B%3D1%40p%3D1749820732%40&middleStation1=&posrednia1=&posrednia1czas=&middleStation2=&posrednia2=&posrednia2czas=&data={date}&date=16%2F06%2F2025&time=00%3A01&minChangeTime=&przyjazd=false&bilkomAvailOnly=on&directOnly=on&_csrf=')
    driver.implicitly_wait(3)

    while 1: 
        show_class(driver, 'date-time-hidden')
        departures = driver.find_elements(By.CLASS_NAME, 'date-time-hidden')
        departures = [
            datetime.fromtimestamp(int(d.get_attribute('textContent'))/1000) 
            for d in departures
            ]

        show_class(driver, 'date-time-arrival-hidden')
        arrivals = driver.find_elements(By.CLASS_NAME, 'date-time-arrival-hidden')
        arrivals = [
            datetime.strptime(a.get_attribute('textContent'), '%d/%m/%Y %H:%M')
            for a in arrivals
            ]

        show_class(driver, 'main-carrier')
        carriers = driver.find_elements(By.CLASS_NAME, 'main-carrier')
        carriers = [c.get_attribute('textContent') for c in carriers[::2]]

        prices = driver.find_elements(by=By.CLASS_NAME, value='buy-tickets-wrapper')
        prices = [p.text.split(' ')[0] for p in prices]

        if '' not in prices:
            break
        time.sleep(1)
    trip_data = []
    for d,a,c,p in zip(departures, arrivals, carriers, prices):
        trip_data.append([check_time, d, a, c, p])
    return trip_data

def main():
    trips = []
    driver = webdriver.Firefox()
    start = datetime.now()
    check_time = datetime.now() + timedelta(minutes=6)

    while check_time - start < timedelta(days=1):
        # print(date_string)
        trips += get_trips_at(driver, check_time)
        check_time = trips[-1][1] + timedelta(minutes=1)
        time.sleep(randint(1,3))

    for t in trips:
        print(f'check_time: {t[0]}, departure: {t[1]}, arrival: {t[2]} carrier: {t[3]}, price: {t[4]}')
    driver.quit()

if __name__ == '__main__':
    main()