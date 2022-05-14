from selenium import webdriver
import time
  
# Main Function
if __name__ == '__main__':
  
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')
  
    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome("/Users/tuannd/Documents/GitHub/selenium-acs/selenium/webdriver/chrome",
                              chrome_options=options)
    driver.set_window_size(1920,1080)
  
    # Send a get request to the url
    driver.get('https://www.geeksforgeeks.org/')
    btnLogin = driver.find_element_by_class_name('login-modal-btn')
    btnLogin.click()
    inputUser = driver.find_element_by_name('user')
    inputPass = driver.find_elements_by_name('pass')
    inputUser.get_attribute('value')
    inputPass.get_attribute('value')
   