import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

if __name__ == '__main__':
  # open chrometab
  driver = uc.Chrome()

  # navigate to the URL
  driver.get("https://degreeworks-c.messiah.edu:8471/dwprodDashboard/")

  # identify the username box and input user's username
  usernameBox = driver.find_element(By.ID, "username")
  username = input("Username: ")
  usernameBox.send_keys("jp1483@messiah.edu")
  
  # identify the password box and input user's password
  passwordBox = driver.find_element(By.ID, "password")
  password = input("Password: ")
  passwordBox.send_keys("(R4(k7h!58!5h")
  passwordBox.send_keys(Keys.RETURN)

  time.sleep(10)

  # get titles of all classes