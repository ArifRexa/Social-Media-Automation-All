import os
import sys
import time
from selenium import webdriver
from .auto import numberOfMembers2, get_members_info, join_group_by_link




class WhatsAppAutomation:
    def __init__(self):
        self.chrome_driver_path = "whatsapp_bot/WhatsApp_Automation/chrome_driver/chromedriver"
        self.user_data_dir = ""
        if sys.platform.startswith('win'):
            self.user_data_dir = "C:/Users/{username}/AppData/Local/Google/Chrome/User Data"
        elif sys.platform.startswith('linux'):
            self.user_data_dir = "~/.config/google-chrome/"

    def create_browser(self):
        os.environ['PATH'] += os.pathsep + self.chrome_driver_path
        options = webdriver.ChromeOptions()
        # Add options to prevent bot detection
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        if self.user_data_dir:
            options.add_argument(f"user-data-dir={self.user_data_dir}")
        # browser = webdriver.Chrome(self.chrome_driver_path, options=options)
        service = webdriver.ChromeService(executable_path=self.chrome_driver_path)
        browser = webdriver.Chrome(service=service, options=options)
        browser.maximize_window()
        browser.get('https://web.whatsapp.com/')
        time.sleep(10)
        return browser

    def get_number_of_participants(self, groups, output_choice=1):
        browser = self.create_browser()
        members = numberOfMembers2(browser, groups, output_choice)
        output = f"{groups}: {members[0]}\n"
        browser.close()
        return output

    def get_group_members_info(self, group_name):
        browser = self.create_browser()
        res = get_members_info(browser, group_name)[1]
        browser.close()
        return res

    def join_a_group_by_link(self, group_link):
        browser = self.create_browser()
        res = join_group_by_link(browser, group_link)
        print(res)
        browser.close()
        return "Joined"
