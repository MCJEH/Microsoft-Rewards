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

global search
search = 1

def check(driver, user):
    driver.get("https://account.microsoft.com/rewards")
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    rewardName = driver.find_element_by_xpath('//*[@id="dashboard-set-goal"]/mee-card/div/card-content/mee-rewards-redeem-goal-card/div/div[2]/h3').text
    rewardPoints = driver.find_element_by_xpath('//*[@id="dashboard-set-goal"]/mee-card/div/card-content/mee-rewards-redeem-goal-card/div/div[2]/p').text
    rewardPointsTotal = int(rewardPoints.split(" / ")[1].replace(",", ""))
    total = int(rewardPoints.split(" / ")[0].replace(",", ""))

    driver.get("https://account.microsoft.com/rewards/pointsbreakdown")
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body"))) 
    pcCurrent = int(int(driver.find_element_by_xpath('//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text) / 5)
    pcTotal = int(int(driver.find_element_by_xpath('//*[@id="userPointsBreakdown"]/div/div[2]/div/div[1]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(" / ")[1]) / 5)
    mobileCurrent = int(int(driver.find_element_by_xpath('//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text) / 5)
    mobileTotal = int(int(driver.find_element_by_xpath('//*[@id="userPointsBreakdown"]/div/div[2]/div/div[2]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(" / ")[1]) / 5)
    edgeCurrent = int(int(driver.find_element_by_xpath('//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]/b').text) / 5)
    edgeTotal = int(int(driver.find_element_by_xpath('//*[@id="userPointsBreakdown"]/div/div[2]/div/div[3]/div/div[2]/mee-rewards-user-points-details/div/div/div/div/p[2]').text.split(" / ")[1]) / 5) 

    user.resetInfo(total, rewardName, rewardPointsTotal, pcCurrent, pcTotal, mobileCurrent, mobileTotal, edgeCurrent, edgeTotal)

def pcSearches(user, userAgent):
    global search
    driver = webdriver.Chrome(options=userAgent)
    
    check(driver, user)

    while not user.checkPCInfo():
        driver.get("https://www.bing.com/search?q=" + str(search))
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

        check(driver, user)
        search = search + 1

    driver.quit()
    driver = None
    print("PC Searches Done")

def mobileSearches(user, userAgent):
    global search
    driver = webdriver.Chrome(options=userAgent)

    check(driver, user)

    while not user.checkMobileInfo():
        driver.get("https://www.bing.com/search?q=" + str(search))
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

        check(driver, user)
        search = search + 1

    driver.quit()
    driver = None
    print("Mobile Searches Done")

def edgeSearches(user, userAgent):
    global search
    driver = webdriver.Chrome(options=userAgent)

    check(driver, user)

    while not user.checkEdgeInfo():
        driver.get("https://www.bing.com/search?q=" + str(search))
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

        check(driver, user)
        search = search + 1

    driver.quit()
    driver = None
    print("Edge Searches Done")