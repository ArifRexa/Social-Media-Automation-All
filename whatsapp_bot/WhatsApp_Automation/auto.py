import os
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import pyautogui
import time
from datetime import datetime
import logging
from prettytable import PrettyTable
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a file handler for logging
log_dir = "logs/WhatsApp_Group_Bot"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Create a file handler for logging
log_file = f"{datetime.now().strftime('%Y-%m-%d')}.log"
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


def check_exists(browser, csspath, elem_xpath):
    try:
        if elem_xpath:
            browser.find_element(By.CSS_SELECTOR, elem_xpath)
        if csspath:
            browser.find_element(By.CSS_SELECTOR, csspath)
    except NoSuchElementException:
        return False
    return True


def save_numberOfMembers_to_csv(group_name, ans, directory_path):
    ans = ans.replace(' members', '')
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_path = os.path.join(directory_path, "group_members.csv")

    # Check if the file exists, if not, write the header
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Group Name", "Number of Members"])

    # Append new data to the CSV file
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([group_name, ans])


def numberOfMembers(browser, groups, output_choice):
    time.sleep(5)
    res = []
    for group_name in groups:
        if check_exists(browser, "p.selectable-text", None):
            # search_box = browser.find_element_by_css_selector("p.selectable-text")
            wait = WebDriverWait(browser, 50)
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.selectable-text")))
            search_box.click()
            search_box.send_keys(group_name)
            time.sleep(5)

            if check_exists(browser, f"""span[title*='{group_name}']""", None):
                # browser.find_element_by_css_selector(f"""span[title*='{group_name}']""").click()
                browser.find_element(By.CSS_SELECTOR, f"""span[title*='{group_name}']""").click()
                time.sleep(10)
                response = HtmlResponse(url="My HTML STRING", body=browser.page_source, encoding='utf-8')

                if response.css("div#main").extract():
                    # browser.find_element_by_css_selector("div#main header").click()
                    browser.find_element(By.CSS_SELECTOR, "div#main header").click()
                    time.sleep(10)

                    response = HtmlResponse(url="My HTML STRING", body=browser.page_source, encoding='utf-8')
                    time.sleep(5)

                    ans = response.css("button:contains('members') ::text").extract_first()

                    if output_choice == "2":
                        send_on_whatsapp(browser, "*Number of participants in Group:* " + str(ans))
                    res.append(ans)
                    directory_path = "Collected_data/number_of_group_members"
                    save_numberOfMembers_to_csv(group_name, ans, directory_path)
                    logger.info(f"Number of members for group '{group_name}' saved to {directory_path} in a CSV.")
                    return res

        else:
            # print("No Data")
            logger.error("No Data Found.")


def save_numberOfMembers2_to_csv(group_name, members, directory_path):
    members = members.replace(' members', '')
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    file_path = os.path.join(directory_path, "group_members.csv")

    # Save the new entry to the CSV file
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Check if the file is empty
        file_empty = os.stat(file_path).st_size == 0

        if file_empty:
            writer.writerow(["Group Name", "Number of Members"])

        # Check if the entry already exists in the CSV file
        if not file_empty:
            with open(file_path, 'r', newline='') as csvfile_read:
                reader = csv.reader(csvfile_read)
                for row in reader:
                    if row and row[0] == group_name and row[1] == members:
                        return  # Entry already exists, so no need to save again

        writer.writerow([group_name, members])


def numberOfMembers2(browser, groups, output_choice):
    time.sleep(5)
    res = []
    # for group_name in groups:
    if check_exists(browser, "p.selectable-text", None):
        # search_box = browser.find_element_by_css_selector("p.selectable-text")
        wait = WebDriverWait(browser, 50)
        search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.selectable-text")))
        search_box.click()
        search_box.send_keys(groups)
        time.sleep(5)

        if check_exists(browser, f"""span[title*='{groups}']""", None):
            # browser.find_element_by_css_selector(f"""span[title*='{groups}']""").click()
            browser.find_element(By.CSS_SELECTOR, f"""span[title*='{groups}']""").click()
            time.sleep(10)
            response = HtmlResponse(url="My HTML STRING", body=browser.page_source, encoding='utf-8')

            if response.css("div#main").extract():
                # browser.find_element_by_css_selector("div#main header").click()
                browser.find_element(By.CSS_SELECTOR, "div#main header").click()
                time.sleep(10)

                response = HtmlResponse(url="My HTML STRING", body=browser.page_source, encoding='utf-8')
                time.sleep(5)

                ans = response.css("button:contains('members') ::text").extract_first()

                if output_choice == "2":
                    send_on_whatsapp(browser, "*Number of participants in Group:* " + str(ans))
                res.append(ans)
                directory_path = "Collected_data/number_of_group_members"
                save_numberOfMembers2_to_csv(groups, ans, directory_path)
                return res

    else:
        # print("No Data")
        logger.error("No Data Found.")


def get_members_info(browser, group_name):
    # search group
    search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    click_on(browser, search_box_xpath)
    pyperclip.copy(group_name)
    search_box.send_keys(Keys.SHIFT, Keys.INSERT)
    click_on(browser, search_box_xpath)
    search_box.send_keys(Keys.ENTER)

    click_on(browser, '//*[@id="main"]/header/div[2]/div[1]/div/span')
    time.sleep(10)
    time.sleep(2)
    response_data = browser.page_source

    if response_data:
        response = HtmlResponse(url="my HTML string", body=response_data, encoding='utf-8')

    number_xpath = '//*[@id="app"]/div/div/div[5]/span/div/span/div/div/div/section/div[1]/div/div[3]/span/span/button'  # complete Xpath of the element that contains number of participants.

    number_of_part = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, number_xpath)))

    num = number_of_part.get_attribute('innerHTML')

    all_num_xpath = "//div[@class='p357zi0d r15c9g6i g4oj0cdv ovllcyds l0vqccxk pm5hny62']/span"

    # Extract and print the text content of each element
    # sel_elements = browser.find_element_by_xpath(all_num_xpath)
    sel_elements = browser.find_element(By.XPATH, all_num_xpath)

    # Directory where you want to save the CSV file
    directory_path = "Collected_data/contact_info_data"

    # Ensure that the directory exists, create it if it doesn't
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    group_name_for_file = group_name.replace(" ", "_")
    file_name = f"{group_name_for_file}_Phone_Number.csv"
    file_path = os.path.join(directory_path, file_name)
    phone_num = []
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Phone Number's"])
        text = sel_elements.text.replace("You", "").strip()
        phone_numbers = text.split(',')
        for phone_number in phone_numbers:
            phone_number = phone_number.strip()
            if phone_number:
                phone_num.append(phone_number)
                writer.writerow([phone_number])

    # with open("phone_numbers.txt", "w") as file:
    #     for element in elements:
    #         # Remove "You" if it exists in element.text
    #         phone_number = element.text.replace(", You", "").strip()
    #
    #         # Write the phone number to the file if it's not empty
    #         if phone_number:
    #             # For the last element, do not add a newline character
    #             cleaned_phone = phone_number.replace(', ', '\n').strip() if ',' in phone_number else str(
    #                     phone_number)
    #             # cleaned_phone = phone_number.replace(', ', '\n').strip() if ',' in phone_number else str(
    #             # phone_number) + "\n"
    #             file.write(cleaned_phone)

    total_participants = int(num.split(' ')[0])

    # create table
    table = PrettyTable()
    # print("Table: ", table)
    # table.field_names = ["Sr. No.", "Name", "Mobile No."]
    table.field_names = ["Sr. No.", "Mobile No."]
    # Add phone numbers to the table
    for idx, phone_number in enumerate(phone_numbers, start=1):
        if phone_number:
            table.add_row([idx, phone_number])
    logger.info(f"Contact number has been save to {directory_path} in CSV file")
    return table, phone_num


def get_members_phone_numbers(browser, group_name):
    # search group
    search_box_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    click_on(browser, search_box_xpath)
    pyperclip.copy(group_name)
    search_box.send_keys(Keys.SHIFT, Keys.INSERT)
    click_on(browser, search_box_xpath)
    search_box.send_keys(Keys.ENTER)

    click_on(browser, '//*[@id="main"]/header/div[2]/div[1]/div/span')
    time.sleep(10)
    time.sleep(2)
    response_data = browser.page_source

    if response_data:
        response = HtmlResponse(url="my HTML string", body=response_data, encoding='utf-8')

    number_xpath = '//*[@id="app"]/div/div/div[5]/span/div/span/div/div/div/section/div[1]/div/div[3]/span/span/button'  # complete Xpath of the element that contains number of participants.

    number_of_part = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, number_xpath)))

    num = number_of_part.get_attribute('innerHTML')

    all_num_xpath = "//div[@class='p357zi0d r15c9g6i g4oj0cdv ovllcyds l0vqccxk pm5hny62']/span"

    # sel_elements = browser.find_element_by_xpath(all_num_xpath)
    sel_elements = browser.find_element(By.XPATH, all_num_xpath)

    phone_numbers = sel_elements.text.replace("You", "").strip().split(',')
    phone_numbers_string = "{" + ",".join(phone_numbers) + "}"

    return phone_numbers_string


def send_on_whatsapp(browser, result):
    msg_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'
    msg_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, msg_box_xpath)))
    msg_box.click()

    pyperclip.copy(result)
    msg_box.send_keys(Keys.SHIFT, Keys.INSERT)
    msg_box.click()
    msg_box.send_keys(Keys.ENTER)


def click_on(browser, xpath):
    WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, xpath))).click()


def join_group_by_link(browser, link):
    try:
        # Open the link in the browser
        browser.get(link)
        time.sleep(4)

        # # Wait for the 'Join Chat' button to be clickable
        button1 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Join Chat')]"))
        )
        button1.click()
        time.sleep(10)

        pyautogui.press('enter')

        use_whatsapp_web_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'use WhatsApp Web')]"))
        )
        use_whatsapp_web_button.click()

        joining_group_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-disabled,'false')]"))
        )
        joining_group_button.click()

        # Wait for the 'Join group' button to be clickable
        if "//button/div/div[contains(text(), 'Close')]":
            button3 = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button/div/div[contains(text(), 'Close')]"))
            )
            button3.click()
        else:
            pass
        logger.info(f"Joined to the group.")

        return 'Joined'
    except Exception as e:

        # print("Error:", e)
        logger.error("Error:", e)
        return "Something went wrong!"
