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



class Bot:
    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument('--lang=en')
        options.add_argument("--disable-extensions")  
        options.add_argument("--disable-popup-blocking")  
        options.add_argument("--disable-default-apps")  
        options.add_argument("--disable-infobars")  
        options.add_argument("--disable-web-security")  
        options.add_argument(  
            "--disable-features=IsolateOrigins,site-per-process"  
        )  
        options.add_argument(  
            "--enable-features=NetworkService,NetworkServiceInProcess"  
        )  
        options.add_argument("--profile-directory=Default")  
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
            
    def load_cookies(self, initial_site: str, second_site: str):
        self.driver.get(initial_site)
        self.driver.add_cookie({
            "name": "sessionid",
            "value": "", # INSTAGRAM SESSION ID COOKIE VALUE
            "domain": ".instagram.com",
        })
        self.driver.refresh()
        time.sleep((random.random()+0.5)*3)
        self.driver.get(second_site)   
        time.sleep(random.randint(10,20))
        
        
    def search_username(self, username: str):
        print(f"Searching username {username}")
        search_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search input']"))
        )
        print("Search box found...")
        search_box.clear()
        time.sleep((random.random()+1)*3)
        for letter in username:
            search_box.send_keys(letter)
            time.sleep((random.random()/2))
        
    def eliminate_follower(self):    
        time.sleep((random.random()*2) + 2)
        remove_btns = self.driver.find_elements(By.XPATH, "//div[text()='Remove']")
        if not remove_btns:
            return "not found"
        if len(remove_btns) == 1:
            time.sleep(random.random()*4)
            self.driver.execute_script("arguments[0].click();", remove_btns[0])
            time.sleep((random.random()+1)*2)
            
            sure_btn = self.driver.find_element(By.XPATH, "//button[text()='Remove']")
            self.driver.execute_script("arguments[0].click();", sure_btn)
            
    def elimitaded_follower(self):
        try:
            is_removed = self.driver.find_elements(By.XPATH, "//span[text()='Removed']")
            return True
        except:
            return False
        
        
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
            print(f"Scrapping the follower number {x} of this run...")
            bot.search_username(row['username'])
            if bot.eliminate_follower() == "not found":
                print(f"The user {row["username"]} was not found...")
                df.at[index, 'eliminated'] = True
                df.to_excel("Public.xlsx")
                continue
            
            else:
                if bot.elimitaded_follower() == True:
                    df.at[index, 'eliminated'] = True
                    print(f"The user {row["username"]} was correctly removed...")
                    df.to_excel("Public.xlsx")
                
                else:
                    print(f"The user {row["username"]} could not be removed...")
                    time.sleep(500)
                    bot.reload_page()
            
            if x == 17:
                time.sleep(500)
                x = 0
            
            

    # bot.search_username("")
    
