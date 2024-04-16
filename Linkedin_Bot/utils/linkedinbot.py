import datetime
import json
import os, sys
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from . import element_locators
import time
import logging
import traceback
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create log directory if it doesn't exist

log_dir = "logs/Linkedin_Bot"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create a file handler for logging
log_file = f"{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
log_file_path = os.path.join(log_dir, log_file)
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.INFO)

# Create a console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# def is_cookie_expired(cookie):
#     expiry_timestamp = cookie.get('expiry')
#     if expiry_timestamp:
#         current_timestamp = int(time.time())
#         return expiry_timestamp < current_timestamp
#     return False

class Linkedin:
    linkedin_url = 'https://www.linkedin.com'

    proxy_urls = [
        "http://154.22.53.69:8800",
        "http://154.22.53.70:8800",
        "http://154.22.53.74:8800",
        "http://154.22.53.77:8800",
        "http://154.22.53.80:8800",
        "http://154.22.53.81:8800",
        "http://154.22.53.85:8800",
        "http://154.22.53.89:8800"
    ]

    def __init__(self, username, password, headless=False):
        self.username = username
        self.password = password

        chrome_options = Options()
        # chrome_options.add_argument('--proxy-server=%s' % random.choice(self.proxy_urls))

        if headless:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_prefs = {}
            chrome_options.experimental_options["prefs"] = chrome_prefs
            chrome_prefs["profile.default_content_settings"] = {"images": 2}
            self.driver = webdriver.Chrome(options=chrome_options)

        else:
            options = webdriver.ChromeOptions()
            # Add options to prevent bot detection
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = webdriver.Chrome(options=options)
            self.driver.maximize_window()
        # self.login_linkedin()

    def login_linkedin(self):

        try:
            # Open LinkedIn
            self.driver.get("https://www.linkedin.com")
            if os.path.isfile(os.getcwd() + '/Linkedin_Bot/cookies.json'):
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
            time.sleep(5)
        except Exception as e:
            raise e

    def saveCookies(self):
        # Get and store cookies after login
        cookies = self.driver.get_cookies()

        # Store cookies in a file
        with open('Linkedin_Bot/cookies.json', 'w') as file:
            json.dump(cookies, file)
        print('New Cookies saved successfully')
        logger.info('New Cookies saved successfully')

    def loadCookies(self):
        if os.path.isfile(os.getcwd() + '/Linkedin_Bot/cookies.json'):
            # print("paisi")

            # Load cookies to a vaiable from a file
            with open('Linkedin_Bot/cookies.json', 'r') as file:
                cookies = json.load(file)
                if any(not self.is_cookie_expired(cookie) for cookie in cookies):
                    for cookie in cookies:
                        self.driver.add_cookie(cookie)
                else:
                    logging.warning('Cookies are expired and cannot be loaded')
                    self.login_linkedin()

            # # Set stored cookies to maintain the session
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        else:
            print('No cookies file found')
            logger.warning(f'No cookies file found.{traceback.format_exc()}')

        self.driver.refresh()  # Refresh Browser after login

    def quit_browser(self):
        self.driver.quit()

    @staticmethod
    def is_cookie_expired(cookie):
        expiry_timestamp = cookie.get('expiry')
        if expiry_timestamp:
            current_timestamp = int(time.time())
            return int(expiry_timestamp) < current_timestamp
        return False

    def post_in_feed(self, post_content):
        self.driver.implicitly_wait(10)
        time.sleep(random.uniform(3.5, 5.7))
        try:
            post_input_field = self.driver.find_element(By.XPATH, element_locators.post_to_feed_input_button_fullXPATH)
            # /html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div[1]/div[2]/div[2]/button
            post_input_field.click()
            time.sleep(random.uniform(7.2, 12.5))
        except:
            # input('Error, ')
            logger.error(f"Something went wrong.{traceback.format_exc()}")
        # self.driver.implicitly_wait(10)

        try:
            # ic('trying..')
            time.sleep(5)
            for char in post_content:
                self.driver.find_element(By.XPATH, element_locators.post_to_feed_input_area_fullXPATH).send_keys(
                    char)
                time.sleep(random.uniform(0.4, 0.9))

        except:
            logger.error(f"Something went wrong.{traceback.format_exc()}")

        # post_input_field.send_keys(post_content)
        # self.driver.implicitly_wait(10
        time.sleep(15)
        # ic('clicking...')

        try:
            # ic('trying..')
            self.driver.find_element(By.XPATH, element_locators.post_to_feed_submit_button_fullXPATH).click()
            self.driver.implicitly_wait(10)
            logger.info("Post Done on feed.")
            time.sleep(random.uniform(7.2, 12.5))

        except:
            logger.error(f"Something went wrong.{traceback.format_exc()}")
            pass
        # ic('done.')

    def like_on_post(self, number_of_posts: int):
        self.driver.implicitly_wait(10)
        time.sleep(random.uniform(5.2, 8.2))
        # main = self.driver.find_element(By.TAG_NAME, 'main')
        allposts = self.driver.find_element(By.CLASS_NAME, "scaffold-finite-scroll__content").find_elements(By.XPATH,
                                                                                                            ".//div")
        # print(f"Tag Name: {allposts}, ")

        # Loop through the first-level child div elements and print their tag and class names
        i = 0
        for element in allposts:
            try:
                if i < number_of_posts:
                    like_button = element.find_element(By.XPATH,
                                                       "//span[contains(@class, 'reactions-react-button "
                                                       "feed-shared-social-action-bar__action-button')]/button[contains("
                                                       "@aria-label, 'React Like')]")
                    like_button.click()
                    time.sleep(random.uniform(5.5, 8.7))
                    i += 1
                else:
                    time.sleep(random.uniform(3.5, 4.7))
                    logger.info('Status:' f"Liked {number_of_posts} post's in feed.")
                    break
            except Exception as e:
                logger.error(f"Something went wrong.{traceback.format_exc()}")

    def post_to_group(self, group_id, post_content):
        try:
            self.driver.implicitly_wait(10)
            time.sleep(random.uniform(5.2, 8.5))
            self.driver.get(f'{self.linkedin_url}/groups/{group_id}/')
            self.driver.implicitly_wait(10)
            # time.sleep(10)
            self.driver.find_element(By.XPATH, element_locators.post_to_group_input_button_fullXPATH).click()
            for char in post_content:
                self.driver.find_element(By.XPATH, element_locators.post_to_group_input_area_fullXPATH).send_keys(
                    char)
                time.sleep(random.uniform(0.4, 0.9))
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, element_locators.post_to_group_submit_button_fullXPATH).click()
            logger.info(f"Post Done on group id: {group_id}.")
            time.sleep(random.uniform(7.2, 12.5))
            # ic('done')
        except Exception as e:
            logger.error(f"Something went wrong.{e}")

    def repost_a_post(self, number_of_posts):
        self.driver.implicitly_wait(10)
        time.sleep(random.uniform(4.3, 7.5))
        allposts = self.driver.find_elements(By.XPATH, "//div[@class='scaffold-finite-scroll__content']/div")
        # print(f"Tag Name: {allposts}, ")

        # Loop through the first-level child div elements and print their tag and class names
        i = 0
        for element in allposts:
            if i < number_of_posts:

                if element.find_element(By.XPATH, ".//span/button[contains(@class,'artdeco-dropdown__trigger')]"):
                    repost_button_icon = element.find_element(By.XPATH,
                                                              ".//span/button[contains(@class,'artdeco-dropdown__trigger')]")
                    repost_button_icon.click()
                    # print("repost icon clicked")
                    time.sleep(random.uniform(2.5, 3.7))
                    repost_button = element.find_element(By.XPATH,
                                                         "//div[contains(@class, 'artdeco-dropdown__item') and contains(@class, 'artdeco-dropdown__item--is-dropdown') and contains(@class, 'ember-view') and contains(@class, 'social-reshare-button__sharing-as-is-dropdown-item')]/span[contains(@class,'t-14 t-bold') and text()='Repost']")
                    time.sleep(random.uniform(1.5, 2))
                    repost_button.click()
                    # print("Etao clicked")
                    i += 1
                    time.sleep(random.uniform(6.9, 8.5))
                else:
                    continue
            else:
                time.sleep(random.uniform(3.5, 4.7))
                logger.info('Status:' f"Repost {number_of_posts} post's in feed.")
                break

    def comment_on_posts(self, number_of_posts, comment_text):
        self.driver.implicitly_wait(10)
        time.sleep(random.uniform(3.5, 6.8))
        allposts = self.driver.find_elements(By.XPATH, "//div[@class='scaffold-finite-scroll__content']/div")
        # print(f"Tag Name: {allposts}, ")

        # Loop through the first-level child div elements and print their tag and class names
        i = 0
        for element in allposts:
            if i < number_of_posts:

                if element.find_element(By.XPATH, ".//span//button[contains(@class, 'comment-button')]"):
                    comment_button_icon = element.find_element(By.XPATH,
                                                               ".//span//button[contains(@class, 'comment-button')]")
                    comment_button_icon.click()
                    # print("repost icon clicked")
                    time.sleep(random.uniform(2.5, 3.7))
                    comment_area = element.find_element(By.XPATH,
                                                        ".//div[@class='comments-comment-box-comment__text-editor']//div[@class='ql-editor ql-blank']")
                    time.sleep(random.uniform(1.5, 2))
                    comment_area.click()
                    for char in comment_text:
                        comment_area.send_keys(char)
                        time.sleep(random.uniform(0.4, 0.9))
                    # print("Etao clicked")
                    time.sleep(random.uniform(4.8, 7.7))
                    self.driver.implicitly_wait(10)
                    comment_post_button_path = "//button[contains(@class, 'comments-comment-box__submit-button')]/span[text()='Post']"
                    comment_post_button = element.find_element(By.XPATH, comment_post_button_path)
                    comment_post_button.click()
                    i += 1
                    time.sleep(random.uniform(6.9, 8.5))
                else:
                    continue
            else:
                time.sleep(random.uniform(3.5, 4.7))
                logger.info('Status:' f"Comment on {number_of_posts} post's in feed.")
                break
