import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
# from icecream import ic

class Linkedin:

    linkedin_url = 'https://www.linkedin.com'

    def __init__(self, username, password, headless=True):
        self.username = username
        self.password = password
        if headless:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.driver = webdriver.Chrome()
        # self.login_linkedin()

    def login_linkedin(self):
        # Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
        # driver = webdriver.Chrome(executable_path='path/to/chromedriver')
        # driver = webdriver.Chrome(ChromeDriverManager().install())


        try:
            # Open LinkedIn
            self.driver.get("https://www.linkedin.com")
            if os.path.isfile(os.getcwd() + '/cookies.json'):

                self.loadCookies()
            else:
                # Locate the username and password fields and input the credentials
                username_field = self.driver.find_element("id", "session_key")
                username_field.send_keys(self.username)

                password_field = self.driver.find_element("id", "session_password")
                password_field.send_keys(self.password)

                # Submit the form
                password_field.send_keys(Keys.RETURN)
                self.saveCookies()

            # It's a good practice to wait for some time to allow the page to load
            time.sleep(2)
        except Exception as e:
            raise e

    def saveCookies(self):
        # Get and store cookies after login
        cookies = self.driver.get_cookies()

        # Store cookies in a file
        with open('cookies.json', 'w') as file:
            json.dump(cookies, file)
        print('New Cookies saved successfully')

    def loadCookies(self):
        # Check if cookies file exists
        if 'cookies.json' in os.listdir():

            # Load cookies to a vaiable from a file
            with open('cookies.json', 'r') as file:
                cookies = json.load(file)

            # Set stored cookies to maintain the session
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        else:
            print('No cookies file found')

        self.driver.refresh()  # Refresh Browser after login

    def quit_browser(self):
        self.driver.quit()

    def post_in_feed(self, post_content):
        self.driver.implicitly_wait(10)
        post_input_field = self.driver.find_element(By.XPATH, '//*[@id="ember27"]/span')
        post_input_field.click()
        # self.driver.implicitly_wait(10)
        while(1):
            try:
                # ic('trying..')
                time.sleep(5)
                self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]').send_keys(post_content)
                break
            except:
                pass
        # post_input_field.send_keys(post_content)
        # self.driver.implicitly_wait(10
        time.sleep(5)
        # ic('clicking...')
        while (1):
            try:
                # ic('trying..')
                self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button').click()
                self.driver.implicitly_wait(10)
                break
            except:
                pass
        # ic('done.')

    def like_on_post(self, number_of_posts:int):
        self.driver.implicitly_wait(10)
        main = self.driver.find_element(By.TAG_NAME, 'main')
        # main.find_element()
        first_level_divs = main.find_elements(By.XPATH, "./div")
        # allposts = first_level_divs[2].find_elements(By.XPATH, "./div")[0].find_elements(By.XPATH, "./div")[0].find_elements(By.XPATH, "./div")
        allposts = first_level_divs[2].find_elements(By.XPATH, "./div[1]/div[1]/div")

        # Loop through the first-level child div elements and print their tag and class names
        for div_element in allposts[:number_of_posts]:
            try:
                lkbr = div_element.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[1]/div[1]').find_element(By.CLASS_NAME,
                                                                                                        'update-v2-social-activity\n    ')
                lkbr.find_element(By.CLASS_NAME,
                                  'feed-shared-social-action-bar__button-and-count-wrapper\n              ').find_element(By.TAG_NAME,
                                                                                                               'button').click()


                tag_name = div_element.tag_name
                class_name = div_element.get_attribute("class")

                print(f"Tag Name: {tag_name}, Class Name: {class_name}")
            except:
                print('Skipping..')

        # return allposts


    def post_to_group(self, group_id, post_content):
        self.driver.implicitly_wait(10)
        self.driver.get(f'{self.linkedin_url}/groups/{group_id}/')
        self.driver.implicitly_wait(10)
        # time.sleep(10)
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[3]/div/div/main/div/div[6]/div[2]/div[2]/button/span/span').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]').send_keys(post_content)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/span').click()
        # ic('done')

# if __name__ == '__main__':
#     shaheenbot = Linkedin('shaheenmediusware@gmail.com', 'T%uV:-DAVd5y/=G')
#     # grp_id = '14347500'
#     # grp_id = '14341553'
#     # shaheenbot.post_to_group(grp_id, 'hello')
#     main = shaheenbot.like_on_post(10)
#     input()
