import time
import praw
import random
import logging
import os
from datetime import datetime


class RedditBot:
    def __init__(self):
        # self.reddit = praw.Reddit(
        #     client_id=client_id,
        #     client_secret=client_secret,
        #     username=username,
        #     password=password,
        #     user_agent=user_agent
        # )
        self.reddit = praw.Reddit(
            client_id=os.getenv("CLIENT_ID_REDDIT"),
            client_secret=os.getenv("CLIENT_SECRET_REDDIT"),
            username=os.getenv("USERNAME_REDDIT"),
            password=os.getenv("PASSWORD_REDDIT"),
            user_agent=os.getenv("USER_AGENT_REDDIT")
        )

        # Configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create a file handler for logging
        log_dir = "logs/Reddit_Bot"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a file handler for logging
        log_file = f"{datetime.now().strftime('%Y-%m-%d')}.log"
        log_file_path = os.path.join(log_dir, log_file)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)

        # Create a formatter and set it to the handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def log_error(self, message):
        self.logger.error(message)

    # ======================================Find Subreddits (new, popular, subscribed)==================================
    def find_subreddits(self, limit=None):
        try:
            subscribed_subreddits = [sub.display_name for sub in self.reddit.user.subreddits()]
            time.sleep(random.uniform(5.5, 7.5))
            new_limit = limit if limit is not None else 10
            time.sleep(random.uniform(5.5, 7.5))
            new_subreddits = [sub.display_name for sub in self.reddit.subreddits.new(limit=new_limit)]
            time.sleep(random.uniform(5.5, 7.5))
            popular_subreddits = [sub.display_name for sub in self.reddit.subreddits.popular(limit=new_limit)]
            time.sleep(random.uniform(5.5, 7.5))

            self.logger.info(f"Your Subscribed Subreddits: {subscribed_subreddits}")
            # self.logger.info(subscribed_subreddits)
            self.logger.info(f"New Subreddits: {new_subreddits}")
            # self.logger.info(new_subreddits)
            self.logger.info(f"Popular Subreddits: {popular_subreddits}")
            # self.logger.info(popular_subreddits)
            return {
                "subscribed_subreddits": subscribed_subreddits,
                "new_subreddits": new_subreddits,
                "popular_subreddits": popular_subreddits
            }

        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while fetching subreddit information: {e}")
            return f"Error while fetching subreddit information: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def get_subscribed_subreddits(self):
        try:
            time.sleep(random.uniform(3.5, 5.5))
            subscribed_subreddits = [sub.display_name for sub in self.reddit.user.subreddits()]
            time.sleep(random.uniform(5.5, 7.5))
            # print("Your Subscribed Subreddits:")
            # print(subscribed_subreddits)
            self.logger.info("Your Subscribed Subreddits:")
            self.logger.info(subscribed_subreddits)
            return subscribed_subreddits
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while fetching subscribed subreddits: {e}")
            return f"Error while fetching subscribed subreddits: {e}"
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred:, {e}"

    def get_new_subreddits(self, limit=None):
        try:
            time.sleep(random.uniform(5.2, 7))
            new_limit = limit if limit is not None else 10
            new_subreddits = [sub.display_name for sub in self.reddit.subreddits.new(limit=new_limit)]
            time.sleep(random.uniform(5.5, 7.5))
            # print("\nNew Subreddits:")
            # print(new_subreddits)
            self.logger.info("New Subreddits:")
            self.logger.info(new_subreddits)
            return new_subreddits
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while fetching new subreddits: {e}")
            return f"Error while fetching new subreddits: {e}"
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"

    def get_popular_subreddits(self, limit=None):
        try:
            time.sleep(random.uniform(3.1, 5.2))
            new_limit = limit if limit is not None else 10
            popular_subreddits = [sub.display_name for sub in self.reddit.subreddits.popular(limit=new_limit)]
            time.sleep(random.uniform(5.5, 7.5))
            # print("\nPopular Subreddits:")
            # print(popular_subreddits)
            self.logger.info("Popular Subreddits:")
            self.logger.info(popular_subreddits)
            return popular_subreddits
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while fetching popular subreddits: {e}")
            return f"Error while fetching popular subreddits: {e}"
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"

    # =========================================Create, Comment, Save====================================================
    def create_submission(self, subreddit, title, url=None):
        # res = self.reddit.subreddit(subreddit).submit(title=title, url=url)
        # print(res)
        try:
            # res = self.reddit.subreddit(subreddit).submit(title=title, url=url)
            time.sleep(random.uniform(2.5, 5.5))
            res = self.reddit.subreddit(subreddit).submit(title, url=url)
            time.sleep(random.uniform(5.5, 7.5))
            self.logger.info(f"Submission created: https://www.reddit.com/comments/{res}")
            # print(f"Submission created: https://www.reddit.com/comments/{res}")
            return f"Submission created: https://www.reddit.com/comments/{res}"
        except Exception as e:
            self.log_error(f"Error while creating submission: {e}")
            return f"Error while creating submission: {e}"

    def comment_on_submission(self, submission_url, text):
        try:
            time.sleep(random.uniform(3.0, 4.5))
            submission = self.reddit.submission(url=submission_url)
            time.sleep(random.uniform(6.5, 9.8))
            res = submission.reply(text)
            self.logger.info(f"Successfully commented on submission: {submission_url}")
            return f"Successfully commented on submission: {submission_url}"
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while commenting: {e}")
            return f"Error while commenting: {e}"
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"

    def repost_by_url(self, url, new_subreddit, comment=None):
        try:
            submission = self.reddit.submission(url=url)
            time.sleep(random.uniform(5.5, 7.5))
            cross_post = submission.crosspost(subreddit=new_subreddit)
            time.sleep(random.uniform(7.5, 9.5))
            if comment:
                cross_post.reply(comment)
            self.logger.info(f"Repost successful: {cross_post.url}")
            return {'success': True, 'url': cross_post.url}
        except Exception as e:
            self.log_error(f"An error occurred while reposting: {e}")
            return {'success': False, 'message': f"An error occurred while reposting: {e}"}

    def repost_random_posts(self, section, num_posts, new_subreddit, comment=None):
        try:
            time.sleep(random.uniform(5.5, 7.5))
            # Fetch random posts based on the specified section
            posts = self.fetch_random_posts(section)
            random.shuffle(posts)
            time.sleep(random.uniform(5.5, 7.5))
            reposted_urls = []

            # Select a random subset of posts to repost
            posts_to_repost = random.sample(posts, min(num_posts, len(posts)))
            time.sleep(random.uniform(5.5, 7.7))
            for post in posts_to_repost:
                time.sleep(random.uniform(10.5, 15.0))
                cross_post = post.crosspost(subreddit=new_subreddit)

                if comment:
                    time.sleep(random.uniform(7.5, 9.5))
                    cross_post.reply(comment)

                reposted_urls.append(cross_post.url)

            self.logger.info("Reposting random posts completed.")
            return {'success': True, 'urls': reposted_urls}
        except Exception as e:
            self.log_error(f"An error occurred while reposting random posts: {e}")
            return {'success': False, 'message': f"An error occurred while reposting random posts: {e}"}

    def comment_on_random_posts(self, section, num_posts, comments):
        commented_posts_info = []
        try:
            # Fetch random posts based on the specified section
            posts = self.fetch_random_posts(section)
            time.sleep(random.uniform(5.5, 8.5))
            random.shuffle(posts)

            # Select a random subset of posts to comment on
            posts_to_comment = random.sample(posts, min(num_posts, len(posts)))
            time.sleep(random.uniform(7.5, 9.5))
            for post in posts_to_comment:
                time.sleep(random.uniform(10.5, 15.5))
                comment = post.reply(comments)
                commented_posts_info.append({
                    'post_id': post.id,
                    'comment_id': comment.id,
                    'url': f"https://www.reddit.com/comments/{post.id}/",
                    'title': post.title,
                })
                self.logger.info(f"Successfully commented on post {post.id}")

            self.logger.info("Commenting on random posts completed.")
        except Exception as e:
            self.log_error(f"An error occurred while commenting on random posts: {e}")

        return commented_posts_info

    def save_submission(self, submission_url):
        try:
            submission = self.reddit.submission(url=submission_url)
            time.sleep(random.uniform(5.5, 7.5))
            submission.save()
            self.logger.info(f"Successfully saved submission {submission_url}")
            return f"Successfully saved submission {submission_url}"
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while saving: {e}")
            return f"Error while saving: {e}"
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return "An unexpected error occurred:", e

    # =========================================Upvote Downvote==========================================================

    def upvote_submission(self, submission_url):
        try:
            submission = self.reddit.submission(url=submission_url)
            time.sleep(random.uniform(5.5, 8.5))
            submission.upvote()
            self.logger.info(f"Successfully upvoted submission: {submission_url}")
            return f"Successfully upvoted submission {submission_url}"
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while upvoting: {e}")
            return f"Error while upvoting: {e}"
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"

    def upvote_random_posts(self, section, num_posts):
        upvoted_posts_info = []

        try:
            # Fetch random posts based on the specified section
            time.sleep(random.uniform(5.5, 7.5))
            posts = self.fetch_random_posts(section)
            random.shuffle(posts)
            time.sleep(random.uniform(7.5, 9.5))
            # Select a random subset of posts to upvote
            posts_to_upvote = random.sample(posts, min(num_posts, len(posts)))

            # Upvote each selected post and collect information
            for post in posts_to_upvote:
                time.sleep(random.uniform(10.5, 13.5))
                post.upvote()
                upvoted_posts_info.append({
                    'id': post.id,
                    'url': post.url,
                    'title': post.title
                })
                self.logger.info(f"Successfully upvoted post: {post.id}")

            self.logger.info("Upvoting random posts completed.")
        except Exception as e:
            self.log_error(f"An error occurred while upvoting random posts: {e}")

        return upvoted_posts_info

    def downvote_submission(self, submission_url):
        try:
            submission = self.reddit.submission(url=submission_url)
            time.sleep(random.uniform(7.5, 9.5))
            submission.downvote()
            self.logger.info(f"Successfully downvoted submission: {submission_url}")
            return f"Successfully downvoted submission {submission_url}"
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error while downvoting: {e}")
            return f"Error while downvoting: {e}"
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred: {e}"

    # ============================================Follow Section========================================================

    def follow_authors(self, subreddit_name, num_of_actions):
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            time.sleep(random.uniform(5.5, 8.5))
            hot_posts = list(subreddit.hot(limit=10))

            # Initialize response list to store details for each action
            responses = []

            for _ in range(num_of_actions):
                time.sleep(random.uniform(8.5, 10.5))
                random_post = random.choice(hot_posts)
                post_author = random_post.author

                response = {}  # Dictionary to store response details for this action

                if post_author:
                    time.sleep(random.uniform(5.5, 7.5))
                    post_author.friend()
                    response['success'] = True
                    response[
                        'message'] = f"Successfully followed user '{post_author.name}' based on a random post in r/{subreddit_name}."
                    response['username'] = post_author.name
                    time.sleep(5)
                    self.logger.info(response['message'])
                else:
                    response['success'] = False
                    response['message'] = "Error: Unable to determine the author of the random post."
                    self.logger.error(response['message'])

                responses.append(response)

            return responses
        except praw.exceptions.RedditAPIException as e:
            self.log_error(f"Error during the process: {e}")
            return [{'success': False, 'message': f"Error during the process: {e}"}]
        except Exception as e:
            self.log_error(f"An unexpected error occurred: {e}")
            return [{'success': False, 'message': f"An unexpected error occurred: {e}"}]

    def unfollow_user(self, username):
        try:
            user = self.reddit.redditor(username)
            time.sleep(random.uniform(5.5, 8.5))
            user.unfriend()
            message = f"Successfully unfollowed user '{username}'."
            self.logger.info(message)
            return {'success': True, 'message': message}
        except praw.exceptions.RedditAPIException as e:
            message = f"Error while unfollowing user '{username}': {e}"
            self.log_error(message)
            return {'success': False, 'message': message}
        except Exception as e:
            message = f"An unexpected error occurred: {e}"
            self.log_error(message)
            return {'success': False, 'message': message}

    def follow_user_by_username(self, username):
        try:
            user = self.reddit.redditor(username)
            time.sleep(random.uniform(5.5, 7.5))
            user.friend()
            message = f"Successfully followed user '{username}'."
            self.logger.info(message)
            return {'success': True, 'message': message}
        except praw.exceptions.RedditAPIException as e:
            message = f"Error while following user '{username}': {e}"
            self.log_error(message)
            return {'success': False, 'message': message}
        except Exception as e:
            message = f"An unexpected error occurred: {e}"
            self.log_error(message)
            return {'success': False, 'message': message}

    def get_followings(self):
        try:
            followings = []  # List to store usernames of users you are following
            friends = self.reddit.user.friends()
            time.sleep(random.uniform(5.5, 7.5))
            if friends:
                message = "Users you are following:"
                self.logger.info(message)

                for friend in friends:
                    time.sleep(random.uniform(5.5, 7.5))
                    username = friend.name
                    followings.append(username)
                    message = f" - {username}"
                    self.logger.info(message)
            else:
                message = "You are not following any users."
                self.logger.info(message)

            return followings  # Return the list of followings
        except praw.exceptions.RedditAPIException as e:
            message = f"Error while retrieving your friends: {e}"
            self.log_error(message)
            return message
        except Exception as e:
            message = f"An unexpected error occurred: {e}"
            self.log_error(message)
            return message

    def fetch_random_posts(self, section):
        try:
            if section == "new":
                posts = list(self.reddit.subreddit('all').new())
                self.logger.info(f"Fetched {len(posts)} new posts.")
                time.sleep(random.uniform(8.5, 13.5))
                return posts
            elif section == "hot":
                posts = list(self.reddit.subreddit('all').hot())
                self.logger.info(f"Fetched {len(posts)} hot posts.")
                time.sleep(random.uniform(9.0, 15.5))
                return posts
            elif section == "top":
                posts = list(self.reddit.subreddit('all').top())
                self.logger.info(f"Fetched {len(posts)} top posts.")
                time.sleep(random.uniform(7.5, 13.5))
                return posts

            else:
                message = "Invalid section provided. Please use 'new', 'hot', or 'top'."
                self.logger.error(message)
                return "Invalid section provided. Please use 'new', 'hot', or 'top'."

        except Exception as e:
            message = f"An error occurred while fetching random {section} posts: {e}"
            self.log_error(message)
            return f"An error occurred while fetching random {section} posts: {e}"

    def perform_random_actions_on_posts(self, section, num_actions):
        try:
            posts = self.fetch_random_posts(section=section)
            # List to store information about the performed actions
            time.sleep(random.uniform(8.5, 15.5))
            action_info = []

            # Randomly choose posts to perform actions on
            posts_to_act_on = random.sample(posts, min(num_actions, len(posts)))
            time.sleep(random.uniform(12.5, 15.5))
            for post in posts_to_act_on:
                time.sleep(random.uniform(5.5, 7.5))
                # Perform random actions on the post
                action = random.choice(["upvote", "save", "comment"])
                action_performed = None
                action_message = None
                time.sleep(random.uniform(6.5, 9.5))
                if action == "upvote":
                    post.upvote()
                    action_performed = "upvote"
                    action_message = f"Upvoted post: {post.title}"
                    time.sleep(random.uniform(5.5, 8.5))

                elif action == "save":
                    post.save()
                    action_performed = "save"
                    action_message = f"Saved post: {post.title}"
                    time.sleep(random.uniform(6.5, 9.5))

                elif action == "comment":
                    post.reply("Random comment!")
                    action_performed = "comment"
                    action_message = f"Commented on post: {post.title}"
                    time.sleep(random.uniform(5.5, 8.5))

                # Collect information about the action
                action_info.append({
                    "url": post.url,
                    "action_performed": action_performed,
                    "post_id": post.id,
                    "post_title": post.title,
                    "author_username": post.author.name if post.author else None,
                    "author_fullname": post.author_fullname if post.author else None,
                    "action_message": action_message
                })

            self.logger.info("Actions performed successfully.")
            return action_info

        except Exception as e:
            message = f"An error occurred while performing random actions: {e}"
            self.log_error(message)
            return f"An error occurred while fetching random {section} posts: {e}"
