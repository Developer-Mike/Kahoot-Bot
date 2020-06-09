from selenium import webdriver
from time import sleep

site = 'https://kahoot.it/'

gamePin = input('Game PIN: ')
botNames = input('Bot Names: ')
botNumber = int(input('Quantity: '))

driver = webdriver.Chrome('chromedriver.exe')
driver.get(site)

for i in range(botNumber):
    error = True
    while error:
        try:
            pinField = driver.find_element_by_id('game-input')
            pinField.clear()
            pinField.send_keys(gamePin)
            del pinField
            
            enterButton = driver.find_element_by_css_selector('.enter-button__EnterButton-sc-1o9b9va-0.gSoXKU')
            enterButton.click()
            del enterButton
            
            sleep(0.5)
            
            nickField = driver.find_element_by_css_selector('.game-input__GameInput-sc-1mk0jn3-0.VqIfa')
            nickField.clear()
            nickField.send_keys(botNames + str(i))
            del nickField
            
            enterButton = driver.find_element_by_css_selector('.enter-button__EnterButton-sc-1o9b9va-0.gSoXKU')
            enterButton.click()
            del enterButton
            
            driver.execute_script('window.open("' + site + '","' + str(i) + '");')
            driver.switch_to.window(str(i))
            
            error = False
        except:
            pass