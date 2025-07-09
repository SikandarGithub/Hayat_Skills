from browser import create_browser, get_element_by_xpath
from dotenv import load_dotenv
import os
from twocaptcha import TwoCaptcha
import time

# Load the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


#######  Three Step process ##### 

#### 1. Read Text 
#### 2. Fill Input Field 
#### 3. Submit


def solve_captcha(image_path):
    api_key = os.getenv('APIKEY_2CAPTCHA', API_KEY)
    solver = TwoCaptcha(api_key)

    try:
        result = solver.normal(image_path)
    except Exception as e:
        print("Error solving captcha:", e)
        return None
    else:
        print("Captcha solved:", result)
        return result['code']




##### Browser Section #######
driver = create_browser(headless=False)

try:
    driver.get("https://2captcha.com/demo/normal")
    driver.maximize_window()
    time.sleep(5)

    # Example usage of get_element_by_xpath
    img_element = get_element_by_xpath(driver, "//img[@alt='normal captcha example']")
   
    if img_element:
        img_src = img_element.get_attribute("src")
        print(f"Image: {img_src}")

        Captcha_Result = solve_captcha(img_src)



        ######  Fill Input example:####
        input_element = get_element_by_xpath(driver, "//input[@id='simple-captcha-field']")
        
        if input_element:
            input_element.send_keys(Captcha_Result)

            Button_element = get_element_by_xpath(driver,"//button[@type='submit']")
            if Button_element:
               Button_element.click()
               time.sleep(5)

               print("Solve Successfully!")
               time.sleep(10)
             

finally:
    driver.quit()
