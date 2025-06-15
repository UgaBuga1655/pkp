from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://bilkom.pl/podroz?basketKey=&carrierKeys=PZ%2CP2%2CP1%2CP5%2CP7%2CP9%2CP0%2CO1%2CP4%2CP3&trainGroupKeys=G.EXPRESS_TRAINS%2CG.FAST_TRAINS%2CG.REGIONAL_TRAINS&returnForOrderKey=&fromStation=Krak%C3%B3w+G%C5%82%C3%B3wny&poczatkowa=A%3D1%40O%3DKrak%C3%B3w+G%C5%82%C3%B3wny%40X%3D19947423%40Y%3D50067192%40U%3D55%40L%3D5100028%40B%3D1%40p%3D1749820732%40&toStation=Warszawa+Centralna&docelowa=A%3D1%40O%3DWarszawa+Centralna%40X%3D21003233%40Y%3D52228864%40U%3D55%40L%3D5100065%40B%3D1%40p%3D1749820732%40&middleStation1=&posrednia1=&posrednia1czas=&middleStation2=&posrednia2=&posrednia2czas=&data=160620251001&date=16%2F06%2F2025&time=10%3A01&minChangeTime=10&przyjazd=false&bilkomAvailOnly=on&_csrf=')
# print(driver.title)
# print(driver.find_element(By.ID, 'search-btn').text)

prices = driver.find_elements(by=By.CLASS_NAME, value='price')
while prices[0].text == '': 
    time.sleep(1)
    prices = driver.find_elements(by=By.CLASS_NAME, value='price')
# print(prices)
prices = [p.text for p in prices]
print(prices)
driver.quit()