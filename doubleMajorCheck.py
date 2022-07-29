import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

# testing automating sign in with Gmail

# if __name__ == '__main__':
#   #open google chrome
#   driver = uc.Chrome()

#   # delete all cookies
#   driver.delete_all_cookies()

#   # navigate to the url
#   driver.get("https://www.gmail.com")

#   # maximize window size
#   driver.maximize_window()

#   # identify the username text box and enter the value
#   email = driver.find_element("id", "identifierId")
#   email.send_keys("padovano.jamie@gmail.com")
#   email.send_keys(Keys.RETURN)

#   time.sleep(3)

#   # find the password text box and insert password into it
#   password = driver.find_element("name", "password")
#   password.send_keys("5Hn@(k3rZ!")
#   password.send_keys(Keys.RETURN)

#   time.sleep(3)

#   driver.close()
#   print("Successful login")


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
  # driver.switch_to.frame(driver.find_element(By.NAME, "frBody"))
  table = driver.find_elements(By.TAG_NAME, "frame")
  tableNames = [item.name for item in table]


  print(tableNames)

  



  





# url = "https://degreeworks-c.messiah.edu:8471/dwprodDashboard/"

# need to figure out how to login before scraping - probably use selenium

# page = requests.get(url)
# soup = BeautifulSoup(page.text, "lxml")

# class_names = soup.find_all('tr', class_="RuleLabelTitleNotNeeded")

# print(class_names)