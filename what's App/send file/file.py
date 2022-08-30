import time
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\hostw\\AppData\\Local\\Google\\Chrome\\User Data") 
options.add_argument('--profile-directory=Profile 1')
browser = webdriver.Chrome(options = options)




df = pd.read_excel('data.xlsx')
for ind in df.index:
    contact = df['Number'][ind]
    filepath = df['location'][ind]
    


    browser.get(f"https://web.whatsapp.com/send?phone={contact}")
    
    while True:
        try:
           attachment_box = browser.find_element( By.XPATH,"//div[@title = 'Attach']")
           attachment_box.click()
           time.sleep(3)
           break
        except:
            pass
        

    file_box = browser.find_element(By.XPATH,"//input[@accept='*']")
    file_box.send_keys(filepath)
    
    time.sleep(2)
    browser.find_element(By.XPATH,"//span[@data-testid='send']").click()
    time.sleep(5)
    
    
browser.close()    



