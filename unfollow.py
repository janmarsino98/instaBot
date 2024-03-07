#IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
from selenium.webdriver.common.by import By
import pandas as pd
import random
def load_database():
    df = pd.read_excel("Public.xlsx", index_col=0)
    df = df[df]
    usernames = list(df['username'])
    return usernames

class Bot:
    def __init__(self):
        options = Options()
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
            
    def load_cookies(self, initial_site: str, second_site: str):
        self.driver.get(initial_site)
    
        time.sleep(3)
        
        with open('cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
            
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            
        self.driver.get(second_site)        
        time.sleep(random.randint(10,20))
        
        
    def search_username(self, username: str):
        search_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search input']"))
        )
        search_box.clear()
        time.sleep((random.random()+1)*3)
        for letter in username:
            search_box.send_keys(letter)
            time.sleep((random.random()/2))
        
    def eliminate_follower(self):    
        time.sleep((random.random()*2) + 2)
        remove_btns = self.driver.find_elements(By.XPATH, "//div[text()='Remove']")
        if len(remove_btns) == 1:
            time.sleep(random.random()*4)
            self.driver.execute_script("arguments[0].click();", remove_btns[0])
            time.sleep((random.random()+1)*2)
            
            sure_btn = self.driver.find_element(By.XPATH, "//button[text()='Remove']")
            self.driver.execute_script("arguments[0].click();", sure_btn)
            try:
                is_removed = self.driver.find_element(By.XPATH, "//span[text()='Removed']")
                return True
            except:
                return False
        else:
            pass
        
        
    def reload_page(self):
        self.driver.refresh()
        
if __name__ == "__main__":
    bot = Bot()
    bot.load_cookies("https://www.instagram.com/", "https://www.instagram.com/kithe_furniture/followers/")
    
    df = pd.read_excel("Public.xlsx", index_col=0)
    x = 0
    for index, row in df.iterrows():
        if row['eliminated'] == False:
            x += 1
            bot.search_username(row['username'])
            if bot.eliminate_follower() == True:
                df.at[index, 'eliminated'] = True
                print(f"Eliminated a total of {x} followers.")
                df.to_excel("Public.xlsx")
                
            else:
                time.sleep(60)
                bot.reload_page()
            
            
            

    # bot.search_username("")
    
