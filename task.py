"""
Using Python Selenium Automation and the URL https://www.instagram.com/guviofficial/ kindly
do the following mentioned tasks:

1) Use either relative or Absolute XPATH only for the task.
2) Extract the total number of Followers and Following from the URL mentioned above.


"""

# Importing the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Creating a class to handle Instagram profile operations
class Guvi:

    def __init__(self,url):
        self.url=url
        # Initializing Chrome driver using WebDriver Manager for Chrome
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Method for extracting the followers
    def followers(self):
        # Maximizing the window and navigating to the Instagram profile URL
        self.driver.maximize_window()
        self.driver.get(self.url)
        # Adding a delay to ensure page loads completely
        sleep(3)
        # Finding the element for followers count using XPATH and printing the followers
        print("Followers: ",self.driver.find_element(by=By.XPATH,value="//div/ul[@class='x78zum5 x1q0g3np xieb3on']/li[2]/div/button").text)
        # Adding a delay
        sleep(3)


    # Method for extracting the following
    def following(self):
        # Adding a delay
        sleep(3)
        # Finding the element for following count using XPATH and printing the following count
        print("Following: ",self.driver.find_element(by=By.XPATH,value="//div/ul[@class='x78zum5 x1q0g3np xieb3on']/li[3]/div/button").text)

    # Method for closing the webdriver session
    def shutdown(self):
        # Closing the WebDriver session
        self.driver.quit()

# Main execution starts here
if __name__=="__main__":
    # Defining the Instagram profile URL
    url="https://www.instagram.com/guviofficial/"
    # Creating an instance of Guvi class with the URL
    guvi=Guvi(url)
    # Calling methods to extract followers and following counts
    guvi.followers()
    guvi.following()
    # Shutting down the WebDriver session
    guvi.shutdown()