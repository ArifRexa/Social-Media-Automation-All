import os
import random
import time
import json
import logging
from instagrapi import Client
from dotenv import load_dotenv
from instagrapi.types import Usertag, UserShort
from instagrapi.exceptions import LoginRequired
from datetime import datetime
from multidb_request_handler import DatabaseOperation
from pathlib import Path

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create log directory if it doesn't exist

log_dir = "logs/Instagram_Bot"
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


class InstagramBot:
    def __init__(self):
        # username = os.getenv("INSTAGRAM_USERNAME")
        # password = os.getenv("INSTAGRAM_PASSWORD")
        self.username = None
        self.password = None
        self.email_id = None
        self.cookies = None
        self.id = None
        self.client = Client()
        # Flag to track login status
        self.logged_in = False
        self.obj = DatabaseOperation(host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'),
                                     database_name=os.getenv('DB_NAME'), table_name=os.getenv('TABLE_NAME'),
                                     username=os.getenv('DB_USERNAME'), password=os.getenv('DB_PASSWORD'))
        status_code, data = self.obj.post_request(
            endpoint="get?social_media_name__like=instagram&company_name__like=rig_network")

        if status_code == 200:
            # print("Start Time:", data[0].get('start_time'))
            # print("End Time:", data[0].get('end_time'))
            self.username = data[0].get('username')
            self.password = data[0].get('password')
            self.email_id = data[0].get('account_email')
            self.cookies = json.loads(data[0].get('cookies'))
            self.id = data[0].get('id')

        else:
            logger.error(f"Failed to retrieve data. Status code: {status_code}")

    def login_permission(self):
        # Check if already logged in
        if not self.logged_in:
            self.login()

    # def login(self):
    #     try:
    #         self.client.login(self.username, self.password)
    #         self.logged_in = True
    #         logger.info("Successfully login")
    #     except Exception as e:
    #         logger.error(f"Login failed: {e}")
    #         # Handle the error as needed, for example, exit the script or retry
    def login(self):
        try:
            # Check if there's a valid session stored in the database
            if self.cookies:
                # Load session from cookies if available
                session = self.client.set_settings(self.cookies)
                if session:
                    # self.client.set_settings(session)
                    self.client.set_settings(self.cookies)

                    # Verify session validity
                    try:
                        self.client.get_timeline_feed()
                        self.logged_in = True
                        logger.info("Successfully logged in using session.")
                        return
                    except LoginRequired:
                        logger.warning("Session is invalid, need to login via username and password.")
                        # Continue to login via username and password if session is invalid

            # If session is not valid or not available, attempt login using username and password
            logger.info("Logging in using username and password.")
            if self.client.login(self.username, self.password):
                self.logged_in = True
                logger.info("Successfully logged in using username and password.")
                try:
                    logging.info(self.client.settings)
                    self.client.get_timeline_feed()
                    self.logged_in = True
                    logger.info("Successfully logged in using  username and password.")

                    # Save session after successful login
                    logger.info("Session data saved.")

                    data = {
                        "cookies": json.dumps(self.client.get_settings())
                    }
                    # print(data)
                    self.obj.patch_request(endpoint=f"update/{self.id}", data=data)
                    return
                except LoginRequired:
                    logger.warning("Session is invalid, need to login via username and password.2")

            else:
                logger.warning("Failed to login using username and password.")

        except Exception as e:
            logger.error(f"An error occurred during login: {e}")

    def logout(self):
        self.logged_in = False
        res = self.client.logout()
        if res:
            logger.info("Log out.")
            return 'log out'
        logger.error("Something went wrong!")
        return 'Something went wrong!'

    def upload_photo_to_story(self, media_path):
        if self.logged_in:
            try:
                self.client.photo_upload_to_story(path=media_path)
            except Exception as e:
                logger.error(f"Photo uploaded but: {e}")
        else:
            return "You should log in first"

    def save_media(self, hashtag, num_posts):
        if self.logged_in:
            try:
                medias = self.client.hashtag_medias_recent(hashtag, 50)
                # selected_medias = random.sample(medias, num_posts)
                random.shuffle(medias)
                # print(selected_medias)
                count = 0
                for media in medias:
                    if count < num_posts:
                        res = self.client.media_save(media.id)
                        if res:
                            logger.info("Media Saved.")
                            count += 1

                return 'Saved Successfully'

            except Exception as e:
                logger.exception(f"Couldn't save {e}")
                return e
        # print("watched")
        else:
            return "You Should Login First."

    # def upload_photo(self, media_path, caption=None, tagged_user_names=None):
    #     if not self.logged_in:
    #         return "You should log in first"
    #
    #     try:
    #         usertags = []
    #         i = 0.5
    #         if tagged_user_names:
    #             for tagged_user_name in tagged_user_names:
    #                 tagged_user_pk = self.client.user_id_from_username(tagged_user_name)
    #                 tagged_user = UserShort(pk=tagged_user_pk, username=tagged_user_name)
    #                 usertags.append(Usertag(user=tagged_user, x=i, y=i))
    #                 i += 0.1
    #
    #         # Upload photo with usertag if provided
    #         self.client.photo_upload(
    #             path=media_path,
    #             caption=caption,
    #             usertags=usertags
    #         )
    #         logger.info("Photo uploaded")
    #     except Exception as e:
    #         logger.error(f"Photo is not uploaded: {e}")
    def upload_photo(self, media_path, caption=None, tagged_user_names=None, hashtags=None):
        if not self.logged_in:
            return "You should log in first"

        try:
            usertags = []
            i = 0.5
            if tagged_user_names:
                for tagged_user_name in tagged_user_names:
                    tagged_user_pk = self.client.user_id_from_username(tagged_user_name)
                    tagged_user = UserShort(pk=tagged_user_pk, username=tagged_user_name)
                    usertags.append(Usertag(user=tagged_user, x=i, y=i))
                    i += 0.1

            # Append hashtags to the caption
            if hashtags:
                if caption:
                    caption += ' ' + ' '.join(hashtags)
                else:
                    caption = ' '.join(hashtags)

            # Upload photo with usertag if provided
            self.client.photo_upload(
                path=media_path,
                caption=caption,
                usertags=usertags
            )
            logger.info("Photo uploaded")
        except Exception as e:
            logger.error(f"Photo is not uploaded: {e}")

    def send_direct_message(self, text, user_name, thread_ids=None, send_attribute="message_button"):
        send_to = int(self.client.user_id_from_username(user_name))

        try:
            return self.client.direct_send(text=text, user_ids=[send_to], thread_ids=thread_ids,
                                           send_attribute=send_attribute)
        except Exception as e:
            logger.error(f"Error sending direct message: {e}")

    def direct_send_photo(self, media_path, user_name, thread_ids=None):
        send_to = int(self.client.user_id_from_username(user_name))
        try:
            return self.client.direct_send_photo(media_path, user_ids=[send_to], thread_ids=thread_ids)
        except Exception as e:
            logger.error(f"Error sending direct photo: {e}")

    def Like_on_media(self, media_id):
        if self.logged_in:
            try:
                self.client.media_like(media_id)
                logger.info(f"Liked post with id {media_id}")
            except Exception as e:
                logger.error(f"Can't like: {e}")
        else:
            return "You should log in first"

    def unlike_on_media(self, media_id):
        if self.logged_in:
            try:
                self.client.media_unlike(media_id)
                logger.info(f"Unliked post with id {media_id}")
            except Exception as e:
                logger.error(f"Can't unlike: {e}")
        else:
            return "You should log in first"

    def Comment_on_media(self, media_id, text):
        if self.logged_in:
            try:
                self.client.media_comment(media_id, text)
                logger.info(f"Commented on post with id {media_id}")
            except Exception as e:
                logger.error(f"Can't comment: {e}")
        else:
            return "You should log in first"

    def Follow_an_user(self, media_user_pk, media_user_username):
        if self.logged_in:
            try:
                self.client.user_follow(media_user_pk)
                logger.info(f"Followed user {media_user_username}")
            except Exception as e:
                logger.error(f"Can't Follow: {e}")
        else:
            return "You should log in first"

    def follow_relevant_accounts(self, hashtag):
        followed_users = []
        if self.logged_in:
            try:
                medias = self.client.hashtag_medias_recent(hashtag, 50)
                my_info = self.client.user_info_by_username(self.username)
                my_followings = self.client.user_following(my_info.pk)

                for media in medias:
                    user = media.user
                    if str(user.pk) in my_followings.keys():
                        logger.info(f"Already Followed user {user.username}.")
                        continue
                    user_info = self.client.user_info_by_username(user.username)
                    follower_count = user_info.follower_count

                    if follower_count >= 2000:
                        self.client.user_follow(user.pk)
                        logger.info(f"Followed user {user.username} with follower count {follower_count}")
                        followed_users.append({'username': user.username, 'pk': user.pk})
                        time.sleep(random.uniform(1.5, 2.5))
                    else:
                        logger.info(f"Not following user {user.username} with follower count {follower_count}")
                return followed_users
            except Exception as e:
                logger.error(f"Error while interacting with hashtag: {e}")
        else:
            logger.error("You should log in first")

    def Comment_on_media_in_conditions(self, hashtag, text):
        commented_posts = []
        unique_media = set()
        if self.logged_in:
            try:
                medias = self.client.hashtag_medias_recent(hashtag, 50)
                for media in medias:
                    user_info = self.client.user_info_by_username(media.user.username)
                    follower_count = user_info.follower_count

                    if follower_count >= 2000 and media.id not in unique_media:
                        self.client.media_comment(media.id, text)
                        unique_media.add(media.id)
                        commented_posts.append(media.code)
                        logger.info(f"Commented on post with pk {media.pk} id {media.id} by user {media.user.username}")
                        time.sleep(random.uniform(1.5, 2.5))
                    else:
                        logger.info(
                            f"Not commenting on post with id {media.pk} by user {media.user.username} because "
                            f"follower count is less than 2000")
                        time.sleep(random.uniform(1.5, 2.5))

                logger.info("Comments processed for all relevant posts.")
                return commented_posts
            except Exception as e:
                logger.error(f"Error while processing comments: {e}")
                return commented_posts
        else:
            logger.error("You should log in first")
            return "You should log in first"

    def my_followers(self):
        my_user_id = self.client.user_id_from_username(self.username)
        res = self.client.user_followers(my_user_id)
        return res

    def my_followings(self):
        my_user_id = self.client.user_id_from_username(self.username)
        res = self.client.user_following(my_user_id)
        return res

    def unfollow_unfollowers(self):
        followers = self.my_followers()
        following = self.my_followings()

        nonfollowers = list(set(following) - set(followers))
        unfollowed_names = []

        for nonfollower in nonfollowers:
            self.client.user_unfollow(nonfollower)
            unfollowed_names.append(nonfollower)
            logger.info(f"Unfollowed {nonfollower}.")
            time.sleep(random.uniform(8.5, 12))
        return unfollowed_names

    def follow_specific_users_by_username(self, usernames):
        for username in usernames:
            res = self.client.user_info_by_username(username)
            self.client.user_follow(res.pk)
            logger.info(f"Followed user {username}")

    def unfollow_specific_users_by_username(self, usernames):
        for username in usernames:
            res = self.client.user_info_by_username(username)
            self.client.user_unfollow(res.pk)
            logger.info(f"Unfollowed user {username}")

    def interact_with_hashtag(self, hashtag, action_type=None, num_posts=None, text=None):
        if self.logged_in:
            medias = self.client.hashtag_medias_recent(hashtag, 50)
            selected_medias = random.sample(medias, num_posts)

            if action_type is None:
                for media in selected_medias:
                    choice = random.choice(["like", "comment", "follow"])

                    if choice == "like":
                        self.Like_on_media(media.id)
                        time.sleep(random.uniform(2.5, 3.5))

                    elif choice == "comment":
                        self.Comment_on_media(media.id, text=text)
                        time.sleep(random.uniform(2.5, 3.5))

                    else:
                        self.Follow_an_user(media.user.pk, media.user.username)
                        time.sleep(random.uniform(2.5, 3.5))
            else:
                for media in selected_medias:
                    if action_type == "like":
                        self.Like_on_media(media.id)
                        time.sleep(random.uniform(2.5, 3.5))

                    elif action_type == "comment":
                        self.Comment_on_media(media.id, text=text)
                        time.sleep(random.uniform(2.5, 3.5))

                    else:
                        self.Follow_an_user(media.user.pk, media.user.username)
                        time.sleep(random.uniform(2.5, 3.5))
        else:
            return "You should log in first"
