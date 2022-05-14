from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
  
# Main Function
if __name__ == '__main__':
  
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
   

    # Provide the path of chromedriver present on your system.
    '''driver = webdriver.Chrome("/Users/tuannd/Documents/GitHub/selenium-acs/selenium/webdriver/chrome/chromedriver2",
                              chrome_options=options)
    #config webdriver chrome manually
    '''
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1920,1080)
  
    # Send a get request to the url
    driver.get('https://accounts.shopify.com/lookup')
    inputEmail = driver.find_element_by_class_name('next-input type-ahead-input email-typo-input')
    inputEmail.get_attribute('value')
    # btnLogin.click()
   
    # inputUser = driver.find_element_by_name('user')
    # inputPass = driver.find_elements_by_name('pass')
    # inputUser.get_attribute('value')
    # inputPass.get_attribute('value')
    # btnNext = driver.find_element_by_class_name('ui-button ui-button--primary ui-button--full-width ui-button--size-large')
    # btnNext.click()
   