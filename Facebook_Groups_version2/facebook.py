import datetime
# from datetime import datetime
import json
import os
import random
import re
import sys
import time
import uuid
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .helper.scraper import Scraper
from time import sleep
from os import system as stm
import platform, unicodedata
from .developer_file_donot_open import login as login_kar

try:
    import requests
except:
    os.system('pip install requests')
    import requests

# --->>> colors
# red = '\033[1;91m'
# green = '\033[1;92m'
# yellow = '\033[1;93m'
# blue = '\033[1;94m'
# pink = '\033[1;95m'
# cyan = '\033[1;96m'
# lred = '\033[1;31m'
# lgreen = '\033[1;32m'
# lyellow = '\033[1;33m'
# lblue = '\033[1;34m'
# lpink = '\033[1;35m'
# lcyan = '\033[1;36m'
# dark = '\033[31;44m'
# dark2 = '\033[35;43m'
# dark3 = '\033[33;5;41m'
# stop = '\033[0m'
total = []

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# # Create a file handler for logging

log_dir = "logs/FB_Group_Bot"
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

def slow_writter(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        sleep(0.05)


if platform.system() == 'Windows':
    c = 95
    cls = 'cls'
else:
    c = 50
    cls = 'clear'

# # --->>> logo
# logo = f"""
# {c * '-'}
#           -> Tool Is Developed by : MOJO
# {c * '-'}{stop}"""


class login():
    def __init__(self):
        # stm(cls)
        # print(logo)
        try:
            token_file = 'Facebook_Groups_version2/developer_file_donot_open/token.txt'
            self.token = open(token_file, 'r').read()
            otw = requests.get('https://graph.facebook.com/me?access_token=' + self.token)
            a = json.loads(otw.text)
            try:
                name = a['name']
            except Exception as c:
                os.remove(token_file)
                print(f" Login Again ! \n {c}")
                time.sleep(2.5)
                # stm(cls)
                # print(logo)
                self.login_me()
        except FileNotFoundError:
            self.login_me()

    def login_me(self):
        # print(f' {lpink} Login Account ! Select Any One Method From Here')
        # print(c * f'{lcyan}-{stop}')
        # print(f" {yellow}[{cyan}1{stop}{yellow}]. {green}Login Account Using Facebook Method ")
        # print(f" {yellow}[{lred}2{stop}{yellow}]. {green}Login Account Using Facebook Lite Method{stop}")
        # print(c * f'{lcyan}-{stop}')
        parser = input(' Select Option To Login -> ')

        if parser in ['1', '01']:
            # stm(cls)
            # print(logo)
            login_kar.login1(input(' Email : '), input(' Pasword : '))
            # stm(cls)
            # print(logo)
        elif parser in ['2', '02']:
            # stm(cls)
            # print(logo)
            login_kar.login2(input(' Email : '), input(' Pasword : '))
            # stm(cls)
            # print(logo)


class main():
    def __init__(self):
        # stm(cls)
        # print(logo)
        from .developer_file_donot_open import headers_agents
        token_file = '.Facebook_Groups_version2/developer_file_donot_open/token.txt'
        # if os.path.exists(token_file):
        self.token = open(token_file, 'r').read() if os.path.exists(token_file) else None
        # self.token = open(token_file, 'r').read()
        self.page1 = ('AbpzrKcXajr_FYRZ2uLB4wTguP7HHQaRTuIufuuoIsshT_Pli4xZmMxDleMqmNCpN9BAcR43bEMs'
                      '-QEfXYSoStlH6jaIZzS2zzVB98DBW0Eg1iMUMw76lfBZUzPH6pKaYym4MIIsIs-IoFajKzKaF264'
                      '-k0Kb99YmVdHnQlj4SSHhOo-VkP1ovP7ap8BFgLhfMKmeCS4-N1vl5'
                      '-zy2IAi2gnbBpMmRlOmwi43_811mb4RSbmhG2r763ru-UCOKQrVZBFwG8IOWCF3pJXH26d2V8ETgE6LC1TvS1dG'
                      '-aIVOrffq0OAnIVSssbGZaJ1hsqTd_bPB-7Vn'
                      '-Da17SWWEimWwflJZxCx8ylEayQ4kgrqqdlDJZihia7Jtgz_jjYFwKQLld3AHlCsaqt6o7apNQ7OKHC-Rnv9s5Gn'
                      '-EllGApqCWWgXpQ03bH9oGMOITM7nSbctc-kxebtlEGji2cSVPc82bz2AVLrTuqWWCzya5-XCM_w6'
                      '-RnfdKg2i1CRaO9eY9KEOFbdeb07uZloUxHZ1QmmWE'
                      '-ADnVv7LGMK77yTRQ0ME4WgTZAFj6VDtm_dV85XqTkJiCEd0ciwX3YnH_iEnwcaxStzpGL9Y1huXHPRM6yNo0EJSflmZtrIV_RW3pd-LbBb0j1RTc08uMGeGLbnUJcAV4PD7c1ms5u8ExsdRzfGndWFra62HHJScyMamnQUbSFpzo2i7eHIyN3j4QwxHEKHGcMM_0LcUZhr5vsKinXN-58nZWTiqbWDPY1uRCNAyX4X0QKrvxINc3FgGqQcfrocBXUNX0W-WPE1M2em31me3sbwp5ON0GXH0PJe6P6ZHCvIOkUBhY91HFqwRE414t0Dl_Spdu2sJJT3yMTEfMAcFCc00OCY7eOeh-yoJqeIdn38N-RhOOAM0UNkLCjbrBPo5HhLLzwP986j-xwQjVzcC7XKCb83Gk5uXR7AhAL8u2lerWQ5YhCqjBH6q6TBOHxVeOuwtdCBao-YvC3wnljOpWOlobNQvLi7tf3MOhpVYVJwWbiRrNJz-70oBGS_3Ee0Lfr1jRRI3V-vPyCfF3MSxco6lxZOPBzLDYzYPxecqsk6Yp5RUDoOmzo21jbsdFYr5-ZOe8J3CZ_R8ySgHjQLc5o2svFIfe7QlUH0ygQfIckrrW3x2scv7Z763hcUr5vPtku65VLR3nSnVphSCWQoLhZNs0GFrVfyy4Siy68YuEveVckzH-RSbCSQXEKZA3824h-Kj4lgSeHJBZ-34yKb62ehLGpjbA52dBgBDeyvUYZmdqvAD1L_1iWfwQZnKQUQKUUay-bIJdcgNJrJTSjRrm-cogfgs7sJpOPM5NKFVnoI3cTWWzGTpbwwcATbFxLyQoPegw3yhxErWZDV8wAe2V7775VdAc1cBnl68kS5e88N9guhozW7CDpTqSsyndgJRncT3BlJ8L0LSLzTt8SgW8QNetNtKeSQpLXp2_fUvG1DWtn9URvayws_7uN489db-5FGm1iO-BQBlDEXfOxIljrEN4DtDQEQ6Rr1f1rWhJRk3ohkrhF30a4GYEEgEQPjv9hcZLQx4aeGSi3SzUNZENZ67ASzJfwWtiOjpb3BZbYCVp0uil-1dY2ZALFXFfor6jlkbRVGPqI4Ez-8V0KChUnpk39vlqoUuGa6Sps7EkXiAB8-1K5xctBns__Mj_aQ7wubq24D0VbS9-wBQtsyEI09hUFWn4Eo6t1qpQcvO0qT8qfcB0tKiwOtAh60rtVVufBhoP8a6JWLCsZOSGC0XUn14k-9QoSt3sBlT2elGFNlSm6bvGJ0tjhlwUMXunZc5msuLBUxj4V1seJLv6h3kTQAgOzeFi--8y_AwLCY6E4uUOZe6vMwPAb56cGjE7Q9LSfXUHD5y4vvZksBqIEL0nQRQ9H8Se0geRZlJ3Ed9zs')
        self.file = open('Facebook_Groups_version2/input_data.txt', 'r').readlines()
        time.sleep(random.uniform(10.9, 15.7))
        self.headers = headers_agents.headers1()
        time.sleep(random.uniform(10.9, 15.7))
        self.headers2 = headers_agents.headers2()
        time.sleep(random.uniform(10.9, 15.7))
        self.namefile = datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S")

    def data_http(self, groups_name):
        data = {
            "client_doc_id": "395907910716176498299001478287",
            "method": "post",
            "locale": "en_US",
            "pretty": "false",
            "format": "json",
            "variables": '{"default_image_scale":3,"nt_context":{"using_white_navbar":true,"pixel_ratio":3,'
                         '"styles_id":"c86e2eaa6c16a4f0fa7d2a955a7a8004",'
                         '"bloks_version":"f7474c5acff3b37762d44692791f804159a49cf699021ba3623bcb76ea1576a2"},'
                         '"bsid":"' + str(
                uuid.uuid4()) + '","entered_query_text":"","image_low_width":240,"disable_story_menu_actions":false,"query_source":"unknown","ui_theme_name":"","end_cursor":"' + self.page1 + '","supported_experiences":["FAST_FILTERS","FILTERS","FILTERS_AS_SEE_MORE","INSTANT_FILTERS","MARKETPLACE_ON_GLOBAL","MIXED_MEDIA","NATIVE_TEMPLATES","NT_ENABLED_FOR_TAB","NT_SPLIT_VIEWS","PHOTO_STREAM_VIEWER","SEARCH_SNIPPETS_ICONS_ENABLED","USAGE_COLOR_SERP","commerce_groups_search","keyword_only"],"image_large_aspect_width":720,"image_high_width":720,"inline_comments_location":"search","callsite":"android:group_search","image_large_aspect_height":376,"image_medium_width":360,"product_item_image_size":342,"profile_image_size":212,"scale":"3","bqf":"keywords_groups(' + groups_name + ')","tsid":"' + str(
                uuid.uuid4()) + '","request_index":0}',
            "fb_api_req_friendly_name": "SearchResultsGraphQL",
            "fb_api_caller_class": "graphservice",
            "fb_api_analytics_tags": '["pagination_query","GraphServices"]',
            "server_timestamps": "true"
        }
        try:
            po = requests.post('https://graph.facebook.com/graphql?', headers=self.headers, data=data).text
            time.sleep(random.uniform(10.9, 15.7))
            if 'Rate limit exceeded' in po:
                slow_writter(
                    ' You are restricted from facebook for sometime with this facebook account try after some hours or login other id ')
                exit()
            else:
                return po
        except requests.exceptions.ConnectionError:
            # text = f'{red} Your network is slow due to that tool also work slow {stop}'
            text = f'Your network is slow due to that tool also work slow.'
            time.sleep(random.uniform(3, 5))
            return text

    def groups_by_names_keywords(self, group_names):
        groups_names = group_names.replace(' ', '+').split(',')
        group_data = []  # List to store group data
        processed_group_ids = set()
        for groups_name in groups_names:
            po = self.data_http(groups_name)
            time.sleep(random.uniform(10.9, 15.7))
            if po is not None and 'Your network' in po:
                print(po)
            else:
                finding_tags = set(re.findall(
                    '"strong_id__":null,"recent_search_entity_value":{"__typename":"Group","id":"(.*?)","name":"(.*?)",',
                    str(po)))
                time.sleep(random.uniform(10.9, 15.7))
                for group_id, group_name in finding_tags:
                    time.sleep(random.uniform(10.9, 15.7))
                    try:
                        group_name = group_name.encode('utf-8').decode('unicode-escape')
                    except:
                        group_name = group_name
                    group_name = ''.join(
                        c if unicodedata.category(c)[0] in ['L', 'N', 'Z'] else '?' for c in group_name)

                    # Fetch additional information from the group's page
                    group_info = self.extract_group_info(group_id)
                    time.sleep(random.uniform(10.9, 15.7))
                    total_members = group_info.get('total_members', 'N/A')
                    post_count = group_info.get('post_count', 'N/A')

                    # Construct the URL
                    group_url = f'https://facebook.com/groups/{group_id}'

                    if group_id not in processed_group_ids:
                        # Append group data to group_data list
                        group_data.append({
                            'Group ID': group_id,
                            'Group Name': group_name,
                            'Total Members': total_members,
                            'New Post Count': post_count,
                            'URL': group_url
                        })
                        processed_group_ids.add(group_id)

                        # print(f'{lgreen} Successfully Obtained {yellow}{group_id}{stop} | {yellow}{group_name}{stop} | '
                        #       f'Total Members: {total_members} | New Post Count: {post_count}')
                        logger.info(f'Successfully Obtained: {group_id} | {group_name} | '
                                    f'Total Members: {total_members} | New Post Count: {post_count}')
                        time.sleep(random.uniform(1.5, 2.5))

        # Sort the group data based on total members
        for group in group_data:
            if group['Total Members'] == 'N/A':
                group['Total Members'] = 0
        group_data.sort(key=lambda x: int(x['Total Members'].replace(",", "")), reverse=True)

        # Write the data to the file
        with open(f'Facebook_Groups_version2/data/groups_by_names_{self.namefile}.txt', 'a', encoding='utf-8') as file:
            for group in group_data:
                file.write(
                    f"{group['Group ID']}|{group['Group Name']}|Total Members: {group['Total Members']}|"
                    f"New Post Count: {group['New Post Count']}|URL: {group['URL']}\n"
                )

        # Return the processed group data
        return group_data

    def extract_group_info(self, group_id):
        try:
            # Fetch the group's page
            response = requests.get(f'https://web.facebook.com/groups/{group_id}/about', headers=self.headers2)
            time.sleep(random.uniform(10.9, 15.7))
            if response.status_code == 200:
                content = response.text
                # Extract total members count and post count
                total_members = re.search(r'"group_total_members_info_text":"\s*([\d,]+)\s*', content).group(1)
                post_count = re.search(r'number_of_posts'
                                       r'_in_last_day":(.*?),', content).group(1)
                time.sleep(random.uniform(10.9, 15.7))
                return {'total_members': total_members, 'post_count': post_count}
            else:
                # print(f'Failed to fetch group information for group ID: {group_id}')
                logger.warning(f'Failed to fetch group information for group ID: {group_id}')
                return {'total_members': 'N/A', 'post_count': 'N/A'}
        except Exception as e:
            # print(f'Error occurred while fetching group information for group ID {group_id}: {str(e)}')
            logger.exception(f'Error occurred while fetching group information for group ID {group_id}: {str(e)}')
            return {'total_members': 'N/A', 'post_count': 'N/A'}

    def group_by_id(self):
        group_data = []  # List to store group data
        processed_group_ids = set()  # Set to store processed group IDs

        if len(self.file) < 1:
            # slow_writter(f' {lpink} Paste All Groups Ids To input_data.txt File Then It Will Start')
            slow_writter(f'  Paste All Groups Ids To input_data.txt File Then It Will Start')
            return 'Paste All Groups Ids To input_data.txt File Then It Will Start.'

        for groups_name in self.file:
            time.sleep(random.uniform(10.9, 15.7))
            try:
                po = requests.get(f'https://web.facebook.com/groups/{groups_name}/about', headers=self.headers2).text
                time.sleep(random.uniform(10.9, 15.7))
            except requests.exceptions.ConnectionError as e:
                # print(f'{red} Error: Connection error occurred: {e}')
                logger.error(f'Error: Connection error occurred: {e}')
                continue

            groups_name = re.search(r':"Group","name":"(.*?)",', str(po)).group(1)
            time.sleep(random.uniform(10.9, 15.7))
            po = self.data_http(groups_name)
            if po is not None and 'Your network' in po:
                print(po)
            else:
                finding_tags = set(re.findall(
                    '"strong_id__":null,"recent_search_entity_value":{"__typename":"Group","id":"(.*?)","name":"(.*?)",',
                    str(po)))
                for group_id, group_name in finding_tags:
                    time.sleep(random.uniform(10.9, 15.7))
                    try:
                        group_name = group_name.encode('utf-8').decode('unicode-escape')
                    except:
                        group_name = group_name
                    group_name = ''.join(
                        c if unicodedata.category(c)[0] in ['L', 'N', 'Z'] else '?' for c in group_name)

                    # Extract group information
                    group_info = self.extract_group_info(group_id)
                    group_url = f'https://facebook.com/groups/{group_id}'

                    # Check if the group ID has already been processed
                    if group_id not in processed_group_ids:
                        # Append group data to group_data list
                        group_data.append({
                            'Group ID': group_id,
                            'Group Name': group_name,
                            'Total Members': group_info.get("total_members", "N/A"),
                            'New Post Count': group_info.get("post_count", "N/A"),
                            'URL': group_url
                        })
                        processed_group_ids.add(group_id)  # Add the processed group ID to the set

                        # Display total members and post count
                        # print(
                        #     f'{lgreen} SucessFully Obtained {yellow}{group_id}{stop} | {yellow}{group_name}{stop} | Total '
                        #     f'Members: {group_info["total_members"]} | Post Count: {group_info["post_count"]}')
                        logger.info(
                            f'Sucessfully Obtained {group_id} | {group_name} | Total '
                            f'Members: {group_info["total_members"]} | Post Count: {group_info["post_count"]}')
                        total.append(group_name)
                        time.sleep(random.uniform(1.5, 2.5))

        # Sort the group data based on total members
        for group in group_data:
            if group['Total Members'] == 'N/A':
                group['Total Members'] = 0
        group_data.sort(key=lambda x: int(x['Total Members'].replace(",", "")), reverse=True)

        # Write the data to the file
        with open(f'Facebook_Groups_version2/data/groups_by_id_{self.namefile}.txt', 'a', encoding='utf-8') as file:
            for group in group_data:
                file.write(
                    f'{group["Group ID"]}|{group["Group Name"]}|Total Members: {group["Total Members"]}|New Post Count: {group["New Post Count"]}|URL: {group["URL"]}\n')

        return group_data

    def group_by_country(self, group_names, country_names):
        groups_names = group_names.replace(' ', '+').split(',')
        country_by_users = country_names.replace(' ', '+').split(',')
        page_ids_and_names = []
        group_data = []  # List to store group data
        processed_group_ids = set()  # Set to store processed group IDs

        for groups_name in groups_names:
            time.sleep(random.uniform(10.9, 15.7))
            for country_by_user in country_by_users:
                time.sleep(random.uniform(10.9, 15.7))
                try:
                    # Make request to fetch group IDs
                    data = {
                        # Your request payload
                        'client_doc_id': '26181989761915706844914575290',
                        'method': 'post',
                        'locale': 'en_US',
                        'pretty': 'false',
                        'format': 'json',
                        'variables': '{"count":12,"profile_picture_size":72,"filterID":"Z3NxZjp7IjAiOiJicm93c2VfaW5zdGFudF9maWx0ZXIiLCIxIjoia2V5d29yZHNfZ3JvdXBzKGxpb24pIiwiMyI6Ijg3OGJhMDEzLWY0ZTctNDczZi1hMjQ1LTkwMTQzNWZjZTQ2YiIsImN1c3RvbV92YWx1ZSI6IkJyb3dzZUdyb3Vwc0NpdHlJbnN0YW50RmlsdGVyQ3VzdG9tVmFsdWUifQ==","substring":"' + country_by_user + '","location_filter_fetch":true}',
                        'fb_api_req_friendly_name': 'FB4AGraphSearchFilterQuery',
                        'fb_api_caller_class': 'graphservice',
                        'fb_api_analytics_tags': '["GraphServices"]',
                        'server_timestamps': 'true'
                    }

                    po = requests.post('https://graph.facebook.com/graphql?', headers=self.headers, data=data).json()
                    time.sleep(random.uniform(10.9, 15.7))
                    node = po['data']['node']
                    for edge in node['filter_values']['edges']:
                        time.sleep(random.uniform(10.9, 15.7))
                        page = edge['node']['value_object']
                        page_ids_and_names.append(page['id'])

                    # Simulated loop for processing group IDs
                    # Replace this with your actual logic
                    for i in range(len(page_ids_and_names)):
                        time.sleep(random.uniform(10.9, 15.7))
                        id = page_ids_and_names[i]
                        data2 = {
                            # Your request payload
                            "client_doc_id": "395907910716176498299001478287",
                            "method": "post",
                            "locale": "en_US",
                            "pretty": "false",
                            "format": "json",
                            "variables": "{\"default_image_scale\":3,"
                                         "\"bsid\":\"c6f54b43-f131-4db4-a60f-8b8f9eebf42f\","
                                         "\"entered_query_text\":\"\",\"image_low_width\":240,"
                                         "\"image_large_aspect_height\":376,\"disable_story_menu_actions\":false,"
                                         "\"query_source\":\"unknown\",\"ui_theme_name\":\"\","
                                         "\"image_medium_width\":360,\"product_item_image_size\":342,"
                                         "\"image_high_width\":720,\"nt_context\":{\"using_white_navbar\":true,"
                                         "\"pixel_ratio\":3,\"styles_id\":\"c86e2eaa6c16a4f0fa7d2a955a7a8004\","
                                         "\"bloks_version"
                                         "\":\"f7474c5acff3b37762d44692791f804159a49cf699021ba3623bcb76ea1576a2\"},"
                                         "\"scale\":\"3\",\"enable_at_stream\":true,"
                                         "\"callsite\":\"android:group_search\",\"bqf\":\"keywords_groups(" +
                                         groups_name + ")\",\"tsid\":\""'' + id + ''"\",\"first_unit_only\":true,"
                                                                                  "\"supported_experiences\":["
                                                                                  "\"FAST_FILTERS\",\"FILTERS\","
                                                                                  "\"FILTERS_AS_SEE_MORE\","
                                                                                  "\"INSTANT_FILTERS\","
                                                                                  "\"MARKETPLACE_ON_GLOBAL\","
                                                                                  "\"MIXED_MEDIA\","
                                                                                  "\"NATIVE_TEMPLATES\","
                                                                                  "\"NT_ENABLED_FOR_TAB\","
                                                                                  "\"NT_SPLIT_VIEWS\","
                                                                                  "\"PHOTO_STREAM_VIEWER\","
                                                                                  "\"SEARCH_SNIPPETS_ICONS_ENABLED\","
                                                                                  "\"USAGE_COLOR_SERP\","
                                                                                  "\"commerce_groups_search\","
                                                                                  "\"keyword_only\"],\"filters\":[{"
                                                                                  "\"value\":\"{"
                                                                                  "\\\"name"
                                                                                  "\\\":\\\"filter_groups_location"
                                                                                  "\\\",\\\"args\\\":\\\""'' + id +
                                         ''"\\\"}\",\"name\":\"filter_groups_location\",\"handle\":\"\","
                                         "\"action\":\"add\"},{\"value\":\"{\\\"name\\\":\\\"groups_tab\\\","
                                         "\\\"args\\\":\\\"\\\"}\",\"name\":\"tab_filter\",\"handle\":\"\","
                                         "\"action\":\"add\"}],\"request_index\":0,\"profile_image_size\":212,"
                                         "\"network_start_time\":\"1681164769554\",\"image_large_aspect_width\":720,"
                                         "\"inline_comments_location\":\"search\"}",
                            "fb_api_req_friendly_name": "SearchResultsGraphQL-main_query",
                            "fb_api_caller_class": "graphservice",
                            "fb_api_analytics_tags": "[\"main_query\",\"GraphServices\"]",
                            "server_timestamps": "true"
                        }
                        po = requests.post('https://graph.facebook.com/graphql?', headers=self.headers, data=data2).text
                        time.sleep(random.uniform(10.9, 15.7))
                        finding_tags = set(re.findall(
                            '"strong_id__":null,"recent_search_entity_value":{"__typename":"Group","id":"(.*?)",'
                            '"name":"(.*?)",',
                            str(po)))
                        for group_id, group_name in finding_tags:
                            time.sleep(random.uniform(10.9, 15.7))
                            try:
                                group_name = group_name.encode('utf-8').decode('unicode-escape')
                            except:
                                group_name = group_name
                            group_name = ''.join(
                                c if unicodedata.category(c)[0] in ['L', 'N', 'Z'] else '?' for c in group_name)

                            # Extract group information
                            group_info = self.extract_group_info(group_id)
                            group_url = f'https://facebook.com/groups/{group_id}'

                            # Check if the group ID has already been processed
                            if group_id not in processed_group_ids:
                                group_data.append({
                                    'Group ID': group_id,
                                    'Group Name': group_name,
                                    'Total Members': group_info.get("total_members", "N/A"),
                                    'New Post Count': group_info.get("post_count", "N/A"),
                                    'URL': group_url
                                })
                                processed_group_ids.add(group_id)  # Add the processed group ID to the set
                                # print(
                                #     f'Successfully Obtained {group_id} | {group_name} | Total Members: {group_info["total_members"]} | Post Count: {group_info["post_count"]}')
                                logger.info(
                                    f'Successfully Obtained {group_id} | {group_name} | Total Members: {group_info["total_members"]} | Post Count: {group_info["post_count"]}')
                except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
                    # print(f'Error: {e}')
                    logger.error(f'Error: {e}')
                    continue  # Continue to the next iteration if an error occurs

        # Sort the group data based on total members
        for group in group_data:
            if group['Total Members'] == 'N/A':
                group['Total Members'] = 0
        group_data.sort(key=lambda x: int(x['Total Members'].replace(",", "")), reverse=True)

        # Write the data to the file
        with open(f'Facebook_Groups_version2/data/groups_by_country_{self.namefile}.txt', 'a', encoding='utf-8') as file:
            for group in group_data:
                file.write(
                    f'{group["Group ID"]}|{group["Group Name"]}|Total Members: {group["Total Members"]}|New Post Count: {group["New Post Count"]}|URL: {group["URL"]}\n')

        return group_data


class main_nologin():
    def __init__(self):
        # stm(cls)
        # print(logo)
        from .developer_file_donot_open import headers_agents
        self.config = json.load(open('Facebook_Groups_version2/config.json', 'r'))
        self.headers2 = headers_agents.headers2()
        self.namefile = datetime.datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
        self.file = open('Facebook_Groups_version2/input_data.txt', 'r').readlines()

    def perform_actions_on_groups(self):
        scraper = self.login_to_facebook()
        group_ids = self.read_group_ids_from_file('Facebook_Groups_version2/input_data.txt')

        for group_id in group_ids:
            time.sleep(random.uniform(10.9, 15.7))
            self.scrape_group_posts(group_id, scraper)

        scraper.driver.quit()

    def login_to_facebook(self):
        # Implement login functionality here
        scraper = Scraper('https://facebook.com')
        scraper.add_login_functionality('https://facebook.com', 'svg[aria-label="Your profile"]', 'facebook')
        time.sleep(random.uniform(3, 5))
        return scraper
        # pass

    def read_group_ids_from_file(self, file_path):
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def scrape_group_posts(self, group_id, scraper):
        scraper.driver.get(f'https://web.facebook.com/groups/{group_id}')
        time.sleep(random.uniform(3, 6))
        screen_height = scraper.driver.execute_script("return window.screen.height;")
        self.scroll_page(screen_height, scraper)

    def scroll_page(self, screen_height, scraper):
        i = 1
        while i < 7:
            scraper.driver.execute_script(f"window.scrollTo(0, {screen_height}*{i});")
            i += 1
            time.sleep(random.uniform(2, 4))
            self.process_posts(scraper)

    def process_posts(self, scraper):
        elements = scraper.driver.find_elements(By.XPATH,
                                                '//div[contains(@role,"feed")]//div[@class="x1yztbdb x1n2onr6 xh8yej3 '
                                                'x1ja2u2z"]')
        for element in elements:
            action = random.choice(['like', 'comment', None, 'share'])
            self.perform_action(element, action)

    def perform_action(self, element, action):
        try:
            if action == 'like':
                like_button = element.find_element(By.XPATH,
                                                   ".//div[contains(@class,'x168nmei x13lgxp2 x30kzoy x9jhf4c x6ikm8r "
                                                   "x10wlt62')]//div[contains(@class, 'xq8finb x16n37ib')]//div/div["
                                                   "@aria-label='Like']")
                time.sleep(random.uniform(1, 2))
                like_button.click()
                time.sleep(random.uniform(5, 8))

            elif action == 'comment':
                comment_box = element.find_element(By.XPATH,
                                                   ".//div[contains(@class,'x168nmei x13lgxp2 x30kzoy x9jhf4c x6ikm8r "
                                                   "x10wlt62')]//div/div[@aria-label='Write a public comment…' or "
                                                   "@aria-label='Write an answer…'or @aria-label='Submit your first "
                                                   "comment…']")
                comment_box.clear()
                time.sleep(random.uniform(1, 2))
                comment = random.choice(['WOW', 'Nice', 'Awesome', 'Joss'])
                comment_text = comment
                for char in comment_text:
                    time.sleep(random.uniform(0.5, 0.9))
                    comment_box.send_keys(char)
                comment_box.send_keys(Keys.RETURN)
                time.sleep(random.uniform(5, 8))

            elif action == 'share':
                share_button = element.find_element(By.XPATH,
                                                    ".//div[contains(@class,'x168nmei x13lgxp2 x30kzoy x9jhf4c "
                                                    "x6ikm8r x10wlt62')]//div/div[@aria-label='Send this to friends "
                                                    "or post it on your profile.']")
                time.sleep(random.uniform(1, 2))
                share_button.click()
                time.sleep(random.uniform(1.8, 3))
                share_now_button = element.find_element(By.XPATH,
                                                        '//div[@aria-label="Share options"]//div[contains(@class, '
                                                        '"x1i10hfl")]//span[text()="Share now (Public)" or text('
                                                        ')="Share now (Friends)"]')
                share_now_button.click()
                time.sleep(random.uniform(5, 8))

            elif action is None:
                time.sleep(random.uniform(5, 8))

        except Exception as e:
            # print(f"Error while performing action: {str(e)}")
            logger.error(f"Error while performing action: {str(e)}")
