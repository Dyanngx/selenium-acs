from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib3
import time
  
# Main Function
if __name__ == '__main__':
  
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
   

    # Provide the path of chromedriver present on your system.
    '''
    driver = webdriver.Chrome("/Users/tuannd/Documents/GitHub/selenium-acs/selenium/webdriver/chrome/chromedriver2",
                              chrome_options=options)
    #config webdriver chrome manually
    '''
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1920,1080)
  
    # Send a get request to the url
    # driver.get('https://accounts.shopify.com/lookup')
    driver.get('https://partners.shopify.com/1995153/stores/new')
    inputEmail = driver.find_element_by_name('account[email]')
    # inputEmail.get_attribute('value')
    inputEmail.send_keys('dinhtuannguyen469@gmail.com')
    btnNext = driver.find_element_by_name('commit')
    time.sleep(5)
    btnNext.click()
    time.sleep(7)
    inputPass = driver.find_element_by_name('account[password]')
    inputPass.send_keys('Tuan0697@')
    time.sleep(5)
    btnLogin = driver.find_element_by_class_name('ui-button--primary')
    btnLogin.click()
    time.sleep(10)
    checkDevStore = driver.find_element_by_id('PolarisRadioButton1')
    checkDevStore.click()


    
   