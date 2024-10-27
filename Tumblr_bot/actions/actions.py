import pytumblr
import random
import time
import os
from dotenv import load_dotenv
import logging
from datetime import datetime
from multidb_request_handler import DatabaseOperation


class TumblrBot:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create log directory if it doesn't exist
        load_dotenv()
        log_dir = "logs/Tumblr_Bot"
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
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # obj = DatabaseOperation(host='http://127.0.0.1', port='44777',
        #                         database_name='checkbot', table_name='base_cred',
        #                         username='postgres', password='123456789')
        obj = DatabaseOperation(host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'),
                                database_name=os.getenv('DB_NAME'), table_name=os.getenv('TABLE_NAME'),
                                username=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'))
        # Assuming `obj.post_request(endpoint="get")` returns a tuple of status code and list of dictionaries
        status_code, data = obj.post_request(endpoint="get?social_media_name__like=tumblr&company_name__like=rig_network")
        consumer_key = None
        consumer_secret = None
        token_key = None
        token_secret = None
        start_time = None
        end_time = None

        if status_code == 200:
            consumer_key = data[0].get('consumer_key')
            consumer_secret = data[0].get('client_secret_key')
            token_key = data[0].get('access_token_key')
            token_secret = data[0].get('access_token_secret_key')
            start_time = data[0].get('start_time')
            end_time = data[0].get('end_time')
        else:
            self.logger.error(f"Failed to retrieve data. Status code: {status_code}")


        # consumer_key = os.getenv("TUMBLR_CONSUMER_KEY")
        # consumer_secret = os.getenv("TUMBLR_CONSUMER_SECRET")
        # token_key = os.getenv("TUMBLR_TOKEN_KEY")
        # token_secret = os.getenv("TUMBLR_TOKEN_SECRET")

        self.start_time = start_time
        self.end_time = end_time
        # Authenticate via OAuth
        self.client = pytumblr.TumblrRestClient(consumer_key, consumer_secret, token_key, token_secret)

        self.liked_posts = set()
        self.reblogged_posts = set()

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_post_info_list(self, limit=200, tag=None):
        post_info_list = []
        if tag is None:
            rs = self.client.dashboard(limit=limit)
            for post in rs.get('posts', []):
                reblog_key = post.get('reblog_key', None)
                id_string = post.get('id_string', None)
                blog_name = post.get('blog_name', None)

                # Check if all required information is present before adding to the list
                if reblog_key is not None and id_string is not None and blog_name is not None:
                    post_info_list.append([blog_name, id_string, reblog_key])
            random.shuffle(post_info_list)
        else:
            rs = self.client.tagged(tag, limit=limit)
            for post in rs:
                reblog_key = post.get('reblog_key', None)
                id_string = post.get('id_string', None)
                blog_name = post.get('blog_name', None)

                if reblog_key is not None and id_string is not None and blog_name is not None:
                    post_info_list.append([blog_name, id_string, reblog_key])
            random.shuffle(post_info_list)

        return post_info_list

    def like_post(self, id_string, reblog_key, blog_name):
        try:
            if id_string not in self.liked_posts:
                self.client.like(id_string, reblog_key)
                self.liked_posts.add(id_string)
                self.logger.info("Successfully liked post: Blog Name - %s, ID String - %s, Reblog Key - %s", blog_name,
                                 id_string,
                                 reblog_key)
        except Exception as e:
            self.logger.error("Failed to like post: Blog Name - %s, ID String - %s, Reblog Key - %s, Error - %s",
                              blog_name, id_string,
                              reblog_key, str(e))

    def reblog_post(self, id_string, reblog_key, blog_name, my_blog_name, comment=None):
        try:
            if id_string not in self.reblogged_posts:
                if comment:
                    self.client.reblog(my_blog_name, id=id_string, reblog_key=reblog_key, comment=comment)
                else:
                    self.client.reblog(my_blog_name, id=id_string, reblog_key=reblog_key)
                self.reblogged_posts.add(id_string)
                self.logger.info("Successfully reblogged post: Blog Name - %s, ID String - %s, Reblog Key - %s",
                                 blog_name, id_string,
                                 reblog_key)
        except Exception as e:
            self.logger.error("Failed to reblog post: Blog Name - %s, ID String - %s, Reblog Key - %s, Error - %s",
                              blog_name, id_string,
                              reblog_key, str(e))

    def perform_action(self, id_string, reblog_key, blog_name, action_type, my_blog_name=None, comment=None):
        if action_type == 'like':
            self.like_post(id_string, reblog_key, blog_name)
        elif action_type == 'reblog':
            if comment:
                self.reblog_post(id_string, reblog_key, blog_name, my_blog_name, comment)
            else:
                self.reblog_post(id_string, reblog_key, blog_name, my_blog_name)

    def delay(self):
        seconds = random.uniform(1, 2)
        # self.logger.info("Waiting for %s seconds before the next action...", seconds)
        time.sleep(seconds)

    def text_post(self, blogname, state, slug, title, body):
        # self.client.create_text(blogname, state="published", slug="testing-text-posts", title="Testing", body="testing1 2 3 4")
        self.client.create_text(blogname, state, slug, title, body)

    def perform_random_actions(self, post_info_list, total_actions, action_type=None, my_blog_name=None, comment=None):
        param_action_type = action_type
        for _ in range(total_actions):
            post = random.choice(post_info_list)
            blog_name, id_string, reblog_key = post

            if param_action_type is None:
                action_type = random.choice(['like', 'reblog'])
                if action_type == 'like' and id_string not in self.liked_posts:
                    self.perform_action(id_string, reblog_key, blog_name, 'like')
                elif action_type == 'reblog' and id_string not in self.reblogged_posts:
                    if comment:
                        self.perform_action(id_string, reblog_key, blog_name, 'reblog', my_blog_name, comment)
                    else:
                        self.perform_action(id_string, reblog_key, blog_name, 'reblog', my_blog_name)
            else:
                if action_type == 'like' and id_string not in self.liked_posts:
                    self.perform_action(id_string, reblog_key, blog_name, 'like')
                elif action_type == 'reblog' and id_string not in self.reblogged_posts:
                    if comment:
                        self.perform_action(id_string, reblog_key, blog_name, 'reblog', my_blog_name, comment)
                    else:
                        self.perform_action(id_string, reblog_key, blog_name, 'reblog', my_blog_name)

            self.delay()
