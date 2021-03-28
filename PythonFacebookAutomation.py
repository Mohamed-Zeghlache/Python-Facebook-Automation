from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


fb_post = 'facebook_post_link'
email = 'email'
motDePass = 'password'
groups_file = 'file.txt'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})
driver=webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities = chrome_options.to_capabilities())
driver.get('https://www.facebook.com/login/')

try:
    user_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
except:
    print("Error")

user_name.send_keys(email)
password=driver.find_element_by_name("pass")
password.send_keys(motDePass)
password.submit()
time.sleep(10)

driver.get(fb_post)



#share using Page account
with open(groups_file, 'r', encoding='utf-8') as file:
    for group in file:
        try:
            share = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[normalize-space()="Partager"]/div'))
            )
            share.click()
        except:
            print(group)
            driver.get(fb_post)
            time.sleep(10)
            continue



        try:
            shareToGroup = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[normalize-space()="Partager dans un groupe"]/div'))
            )
            time.sleep(5)
            shareToGroup.click()
        except:
            print(group)
            driver.get(fb_post)
            time.sleep(10)
            continue

        

        try:
            group_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , "//input[@role='textbox']"))
            )
            group_name.send_keys(group)
            time.sleep(5)
        except:
            print(group)
            driver.get(fb_post)
            time.sleep(10)
            continue
        

        try:
            click_group = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , "//div[@class='b20td4e0 muag1w35']//div[@role='button']"))
            )
            click_group.click()
        except:
            print(group)
            driver.get(fb_post)
            time.sleep(10)
            continue

        try:
            publish = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , "//div[normalize-space()='Publier']//div[@role='button']"))
            )
            time.sleep(3)
            publish.click()
        except:
            print(group)
            driver.get(fb_post)
            time.sleep(10)
            continue

        time.sleep(10)

print('Done Sharing')
driver.quit()
