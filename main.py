from selenium import webdriver # pip install selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
from account import Account
import constants as constants
from searches import pcSearches, mobileSearches, edgeSearches
#region User-Agents
# PC User Agent
pcOpt = Options()
pcOpt.add_argument("--disable-infobars")
pcOpt.add_argument("start-maximized")
pcOpt.add_argument("--disable-extensions")
pcOpt.add_argument("--start-maximized")
pcOpt.add_argument("user-data-dir=C:\\Users\\Bob\\AppData\\Local\\Google\\Chrome\\User Data")
pcOpt.add_argument("--profile-directory=Profile 1")
# Mobile User Agent
mobileOpt = Options()
mobileOpt.add_argument("--disable-infobars")
mobileOpt.add_argument("start-maximized")
mobileOpt.add_argument("--disable-extensions")
mobileOpt.add_argument("--start-maximized")
mobileOpt.add_argument("user-data-dir=C:\\Users\\Bob\\AppData\\Local\\Google\\Chrome\\User Data")
mobileOpt.add_argument("--profile-directory=Profile 1")
mobileOpt.add_argument("user-agent=Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36")
# Edge User Agent
edgeOpt = Options()
edgeOpt.add_argument("--disable-infobars")
edgeOpt.add_argument("start-maximized")
edgeOpt.add_argument("--disable-extensions")
edgeOpt.add_argument("--start-maximized")
edgeOpt.add_argument("user-data-dir=C:\\Users\\Bob\\AppData\\Local\\Google\\Chrome\\User Data")
edgeOpt.add_argument("--profile-directory=Profile 1")
edgeOpt.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59")
#endregion
global driver
driver = None
# Account
user = Account("Bob", "bob@outlook.com", "password")

def doActivities(driver):
    navigate(driver, "https://account.microsoft.com/rewards")
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    site1 = driver.window_handles[0]
    completeClass = "mee-icon-SkypeCircleCheck"
    #region Website
    card1Container = driver.find_element_by_xpath('//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/mee-rewards-points/div/div/span[1]')
    if not completeClass in card1Container.get_attribute("class").split():
        card1 = driver.find_element_by_xpath('//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[1]/div/card-content/mee-rewards-daily-set-item-content/div/div[3]/a')
        card1.click()
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        site2 = driver.window_handles[1]
        driver.switch_to.window(site2)
        driver.close()
        driver.switch_to.window(site1)
        print("Website Complete")
    else:
        print("Website Complete")
    #endregion
    #region Poll
    card2Container = driver.find_element_by_xpath('//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/mee-rewards-points/div/div/span[1]')
    if not completeClass in card2Container.get_attribute("class").split():
        card2 = driver.find_element_by_xpath('//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[3]/div/card-content/mee-rewards-daily-set-item-content/div/div[3]/a')
        card2.click()
        site3 = driver.window_handles[1]
        driver.switch_to.window(site3)
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        try:
            # True or False
            driver.find_element_by_xpath('//*[@id="rqStartQuiz"]').click()
            pollOpt1 = driver.find_element_by_xpath('//*[@id="rqAnswerOption0"]')
            pollOpt2 = driver.find_element_by_xpath('//*[@id="rqAnswerOption1"]')
            pollOpts = [pollOpt1, pollOpt2]
            choice = random.choice(pollOpts)
            choice.click()
        except NoSuchElementException:
            # Poll
            pollOpt1 = driver.find_element_by_xpath('//*[@id="btoption0"]')
            pollOpt2 = driver.find_element_by_xpath('//*[@id="btoption1"]')
            pollOpts = [pollOpt1, pollOpt2]
            choice = random.choice(pollOpts)
            choice.click()
        driver.close()
        driver.switch_to.window(site1)
        print("Poll Complete")
    else:
        print("Poll Complete")
    #endregion

def start_browser():
    pcSearches(user, pcOpt)
    mobileSearches(user, mobileOpt)
    edgeSearches(user, edgeOpt)
    print("Searches Complete")
    # Resets user agent to default
    driver = webdriver.Chrome(options=pcOpt)
    doActivities(driver)
    print("Daily Set Activities Done")
    
start_browser()