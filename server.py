import sys
from blacksheep import Application, get, post, put, patch, delete
from Tumblr_bot.actions.actions import TumblrBot
from Instagram_bot_api.actions import InstagramBot
from pinterest_bot.py3pin.Pinterest import Pinterest, PinterestClient
from Reddit_bot.main import RedditBot
from Facebook_Groups_version2.facebook import main, main_nologin
from Facebook_Groups_version2.facebook import login as login_kar
from Facebook_Groups_version2.developer_file_donot_open import login as login_kar
from whatsapp_bot.WhatsApp_Automation.whatsapp_automation_bot import WhatsAppAutomation
from Linkedin_Bot.utils.linkedinbot import Linkedin
from blacksheep.server.openapi.v3 import OpenAPIHandler
from dataclasses import dataclass
from openapidocs.v3 import Info
import os

app = Application()
tumblr_bot = TumblrBot()
instabot = InstagramBot()
# pinterest = Pinterest()
pinterest = Pinterest(
    email=os.getenv("PINTEREST_EMAIL"),
    password=os.getenv("PINTEREST_PASSWORD"),
    username=os.getenv("PINTEREST_USERNAME"),
    cred_root='cred_root')
pinterest_client = PinterestClient()
reddit = RedditBot()
main_instance = main()
main_instance_no_login = main_nologin()
wa = WhatsAppAutomation()

docs = OpenAPIHandler(info=Info(title="Social Media Bot API", version="0.0.1"), ui_path='/')
docs.bind_app(app)


# ==============================================================================================================
#                                                Tumblr Bot
# ==============================================================================================================


@docs.tags('A.1 Tumblr Home')
@docs.summary('Home 🏠.')
@get("/tu/home")
def home():
    return '''
    Hi, This is Tumblr autobot!

    1. Perform random action: /ig/actions/<total_actions>

    2. Perform random action on a tag: /ig/actions/<tag>/<total_actions>

    3. Perform like on random post of dashboard: /ig/actions/like/<total_actions>

    4. Perform like on random post of dashboard on tag: /ig/actions/like/<tag>/<total_actions>

    5. Perform reblog on random post of dashboard: /ig/actions/reblog/<total_actions>

    6. Perform reblog on random post of dashboard on tag: /ig/actions/reblog/<tag>/<total_actions>

    7. Perform reblog on random post of dashboard with comment: /ig/actions/reblog/<total_actions>/<comment>

    8. Perform reblog on random post of dashboard on tag with comment: /ig/actions/reblog/<tag>/<total_actions>/<comment>

    '''


@docs.tags('A.4 Tumblr Random Actions')
@docs.summary('Random actions on random post 👍 🔁.')
@docs(description="""**You can perform random actions on random post from here.**\n
    total_actions = Enter the number of how many posts you want to like and reblog.(ex: 3)""", )
@get("/tu/actions/{my_blog_name}/{total_actions}")
def random_actions_tumblr(total_actions: int, my_blog_name: str = None):
    # Specify the tag you want to use, or set it to None for dashboard posts
    tag_to_use = None  # Change this to your desired tag or set it to None
    post_info_list = tumblr_bot.get_post_info_list(tag=tag_to_use)

    # Perform random actions on posts
    tumblr_bot.perform_random_actions(post_info_list=post_info_list, total_actions=total_actions,
                                      my_blog_name=my_blog_name)
    return "Done all actions."


@docs.tags('A.4 Tumblr Random Actions')
@docs.summary('Random actions on random post using tags 👍 🔁.')
@docs(description="""**You can perform random actions on random post filter by tag from here.**\n
    tag = Enter the tag name.(ex: frog)
    total_actions = Enter the number of how many posts you want to like and reblog.(ex: 3)""", )
@get("/tu/actions/{my_blog_name}/{tag}/{total_actions}")
def random_actions_on_tag_tumblr(tag: str, total_actions: int, my_blog_name: str = None):
    post_info_list = tumblr_bot.get_post_info_list(tag=tag)

    # Perform random actions on posts
    tumblr_bot.perform_random_actions(post_info_list=post_info_list, total_actions=total_actions,
                                      my_blog_name=my_blog_name)
    return "Done all actions on tag."


@docs.tags('A.2 Tumblr Like')
@docs.summary('like on random post 👍.')
@docs(description="""**You can give like on random post from here.**\n
    total_actions = Enter the number of how many posts you want to like.(ex: 3)""", )
@get("/tu/actions/like/{total_actions}")
def like_action_tumblr(total_actions: int):
    # Specify the tag you want to use, or set it to None for dashboard posts
    tag_to_use = None  # Change this to your desired tag or set it to None
    post_info_list = tumblr_bot.get_post_info_list(tag=tag_to_use)

    # Perform random like actions on posts
    tumblr_bot.perform_random_actions(post_info_list, total_actions, 'like')
    return "Like Done."


@docs.tags('A.2 Tumblr Like')
@docs.summary('like on random post using tags 👍.')
@docs(description="""**You can give like on random post filter by tag from here.**\n
    tag = Enter the tag name.(ex: frog)
    total_actions = Enter the number of how many posts you want to like.(ex: 3)""", )
@get("/tu/actions/like/{tag}/{total_actions}")
def like_action_on_tag_tumblr(tag: str, total_actions: int):
    post_info_list = tumblr_bot.get_post_info_list(tag=tag)

    # Perform random like actions on posts
    tumblr_bot.perform_random_actions(post_info_list, total_actions, 'like')
    return "Like Done on tag."


@docs.tags('A.3 Tumblr Reblog')
@docs.summary('Reblog random post 🔁.')
@docs(description="""**You can reblog random post from here.**\n
    total_actions = Enter the number of how many posts you want to reblog.(ex: 3)""", )
@get("/tu/actions/reblog/{my_blog_name}/{total_actions}")
def reblog_action_tumblr(total_actions: int, my_blog_name: str = None):
    # Specify the tag you want to use, or set it to None for dashboard posts
    tag = None  # Change this to your desired tag or set it to None
    post_info_list = tumblr_bot.get_post_info_list(tag=tag)

    # Perform random reblog actions on posts
    tumblr_bot.perform_random_actions(post_info_list=post_info_list, total_actions=total_actions, action_type='reblog',
                                      my_blog_name=my_blog_name)
    return "Reblog Done."


@docs.tags('A.3 Tumblr Reblog')
@docs.summary('Reblog random post using tags 🔁.')
@docs(description="""**You can reblog random post filter by tag from here.**\n
    tag = Enter the tag name.(ex: frog)
    total_actions = Enter the number of how many posts you want to reblog.(ex: 3)""", )
@get("/tu/actions/reblog/{my_blog_name}/{tag}/{total_actions}")
def reblog_action_on_tag_tumblr(tag: str, total_actions: int, my_blog_name: str = None):
    post_info_list = tumblr_bot.get_post_info_list(tag=tag)

    # Perform random reblog actions on posts
    tumblr_bot.perform_random_actions(post_info_list=post_info_list, total_actions=total_actions, action_type='reblog',
                                      my_blog_name=my_blog_name)
    return "Reblog Done on tag."


@docs.tags('A.3 Tumblr Reblog')
@docs.summary('Reblog random post with comment 🔁.')
@docs(description="""**You can reblog random post with from here.**\n
    total_actions = Enter the number of how many posts you want to reblog.(ex: 3)
    comment = Enter your comment.""", )
@get("/tu/actions/reblog/{my_blog_name}/{total_actions}/{comment}")
def reblog_action_with_comments_tumblr(total_actions: int, comment: str, my_blog_name: str = None):
    tag = None  # Change this to your desired tag or set it to None
    post_info_list = tumblr_bot.get_post_info_list(tag=tag)

    # Perform random reblog actions on posts
    tumblr_bot.perform_random_actions(post_info_list=post_info_list, total_actions=total_actions, action_type='reblog',
                                      my_blog_name=my_blog_name, comment=comment)
    return "Reblog Done with comments."


@docs.tags('A.3 Tumblr Reblog')
@docs.summary('Reblog random post using tags with comments 🔁.')
@docs(description="""**You can reblog random post filter by tag with comments from here.**\n
    tag = Enter the tag name.(ex: frog)
    total_actions = Enter the number of how many posts you want to reblog.(ex: 3)
    comment = Enter your comment.""", )
@get("/tu/actions/reblog/{my_blog_name}/{tag}/{total_actions}/{comment}")
def reblog_action_on_tag_with_comment_tumblr(tag: str, total_actions: int, comment: str, my_blog_name: str = None):
    post_info_list = tumblr_bot.get_post_info_list(tag=tag)

    # Perform random reblog actions on posts
    tumblr_bot.perform_random_actions(post_info_list=post_info_list, total_actions=total_actions, action_type='reblog',
                                      my_blog_name=my_blog_name, comment=comment)
    return "Reblog Done on tag with comment."


# ==============================================================================================================
#                                                Instagram Bot
# ==============================================================================================================


@docs.tags('B.1 Instagram Authentications')
@docs.summary("Login.")
@docs(description="""**You should login once when you want to perform any actions.**\n""", )
@get("/ig/actions/login/yes")
def ig_login_account_method():
    instabot.login_permission()
    return "Successfully login"


@docs.tags('B.7 Instagram Message')
@docs.summary("Send Message.")
@docs(description="""**You can send message by username.**\n
    media_path = Enter path of your photos.(ex: my_photo.jpg)""", )
@post("/ig/actions/send_message/{text}/{username}")
def ig_send_message(text: str, username: str):
    res = instabot.send_direct_message(text=text, user_name=username)
    # return "Story uploaded"
    return res


@docs.tags('B.6 Instagram Media')
@docs.summary("Upload Story.")
@docs(description="""**You can upload a story.**\n
    media_path = Enter path of your photos.(ex: my_photo.jpg)""", )
@post("/ig/actions/upload_story/{media_path}")
def upload_story(media_path: str):
    res = instabot.upload_photo_to_story(media_path)
    # return "Story uploaded"
    return res


# @docs.tags('B.6 Instagram Media')
# @docs.summary("Story Seen.")
# @docs(description="""**You can watch a story.**\n
#     username = Enter username(ex: my_photo.jpg)""", )
# @post("/ig/actions/upload_story/{media_path}")
# def upload_story(media_path: str):
#     res = instabot.upload_photo_to_story(media_path)
#     # return "Story uploaded"
#     return res


@docs.tags('B.6 Instagram Media')
@docs.summary("Upload Photo.")
@docs(description="""**You can upload a photo from here.**\n
    media_path = Enter path of your photos.(ex: /home/jp/my_photo.jpg)
    caption = Enter your caption.(ex: Universal Need)""", )
@post("/ig/actions/upload_photo/{media_path}/{caption}")
def upload_photo(media_path: str, caption: str = None, hashtag: str = None, tagged_user_names: str = None):
    user_list = []
    if tagged_user_names:
        user_list = tagged_user_names.split(", ")
    hashtags = ['#' + tag.strip() for tag in hashtag.split(', ')] if hashtag else []  # Extract hashtags from URL
    res = instabot.upload_photo(media_path, caption, tagged_user_names=user_list, hashtags=hashtags)
    return res


@docs.tags('B.6 Instagram Media')
@docs.summary('Save a media')
@docs(description="""**You can saved a post randomly based on hashtag.**\n
    hashtag = Enter your hashtag.(ex: drilling_rigs)
    num_posts = Enter how many post you want to save.(ex: 5)""")
@get("/ig/actions/save_media/{hashtag}/{num_posts}")
def ig_save_media(hashtag: str, num_posts: int):
    res = instabot.save_media(hashtag=hashtag, num_posts=num_posts)
    return res


# @post("/ig/actions/upload_photo/{media_path}/{caption}")
# def upload_photo(media_path: str, caption: str = None, tagged_user_names: str = None):
#     user_list = tagged_user_names.split(", ")
#     res = instabot.upload_photo(media_path, caption, tagged_user_names=user_list)
#     return res


@docs.tags('B.3 Instagram Comment')
@docs.summary("Do Comment.")
@docs(description="""**You can comment a post randomly based on hashtag.**\n
    hashtag = Enter your hashtag.(ex: drilling_rigs)
    total_action = Enter how many like you want to do.(ex: 5)
    text = Enter your comment text.(ex: interesting!)""", )
@post("/ig/actions/comment/{hashtag}/{total_action}/{text}")
def ig_comment_action(hashtag: str, total_action: int, text: str):
    instabot.interact_with_hashtag(hashtag, "comment", total_action, text)
    return f"Comment Done on {total_action} post"


@docs.tags('B.3 Instagram Comment')
@docs.summary("Do Comment Condition.")
@docs(description="""**You can comment a post randomly based on hashtag.**\n
    hashtag = Enter your hashtag.(ex: drilling_rigs)
    text = Enter your comment text.(ex: interesting!)""", )
@post("/ig/actions/comment/on_conditions/{hashtag}/{text}")
def ig_comment_action_on_condition(hashtag: str, text: str):
    res = instabot.Comment_on_media_in_conditions(hashtag, text)
    return res


@docs.tags('B.4 Instagram Follow')
@docs.summary("Do Follow.")
@docs(description="""**You can follow a user randomly based on hashtag.**\n
    hashtag = Enter your hashtag.(ex: drilling_rigs)
    total_action = Enter how many like you want to do.(ex: 5)""", )
@post("/ig/actions/follow/{hashtag}/{total_action}")
def ig_follow_action(hashtag: str, total_action: int):
    instabot.interact_with_hashtag(hashtag, "follow", total_action)
    return f"Follow Done on {total_action} post"


@docs.tags('B.4 Instagram Follow')
@docs.summary("Do Follow by Username.")
@docs(description="""**You can follow a user by their username.**\n
    usernames = falco12,bannan9,oraimo28""", )
@post("/ig/actions/follow/{usernames}")
def ig_follow_specific_users_by_username(usernames: str):
    user_list = usernames.split(",")
    instabot.follow_specific_users_by_username(usernames=user_list)
    return f"Follow Done."


@docs.tags('B.4 Instagram Follow')
@docs.summary("Do Unfollow by Username.")
@docs(description="""**You can unfollow a user by their username.**\n
    usernames = falco12,bannan9,oraimo28""", )
@post("/ig/actions/unfollow/{usernames}")
def ig_unfollow_specific_users_by_username(usernames: str):
    user_list = usernames.split(",")
    instabot.unfollow_specific_users_by_username(usernames=user_list)
    return f"Unfollow Done."


@docs.tags('B.4 Instagram Follow')
@docs.summary("Do Follow Condition.")
@docs(description="""**You can follow a user randomly based on relevant hashtag.**\n
    hashtag = Enter your hashtag.(ex: drilling_rigs)""", )
@post("/ig/actions/follow/relevant/{hashtag}")
def ig_relevant_follow_action(hashtag: str):
    res = instabot.follow_relevant_accounts(hashtag)
    return res


# @get("/ig/actions/my_followers")
# def my_followers():
#     res = instabot.my_followers()
#     return res
#
#
#
# @get("/ig/actions/my_followings")
# def my_followings():
#     res = instabot.my_followings()
#     return res


@docs.tags('B.4 Instagram Follow')
@docs.summary("Unfollow Non-followers.")
@docs(description="""**You can unfollow those user's who are not following you.**\n""", )
@put("/ig/actions/unfollow_non_followers")
def ig_unfollow_non_followers():
    res = instabot.unfollow_unfollowers()
    return res


@docs.tags('B.2 Instagram Like')
@docs.summary("Do Like.")
@docs(description="""**You can liked a post randomly based on hashtag.**\n
    hashtag = Enter your hashtag.(ex: drilling_rigs)
    total_action = Enter how many like you want to do.(ex: 5)""", )
@post("/ig/actions/like/{hashtag}/{total_action}")
def ig_like_action(hashtag: str, total_action: int):
    instabot.interact_with_hashtag(hashtag, "like", total_action)
    return f"Like Done on {total_action} post"


@docs.tags('B.2 Instagram Un-Like')
@docs.summary("Do Unlike.")
@docs(description="""**You can unlike a post by giving media id.**\n
    media_id = Enter media id.(ex: 2155832952940083788_1903424587)""", )
@post("/ig/actions/unlike/{media_id}")
def ig_unlike_action(media_id: str):
    instabot.unlike_on_media(media_id=media_id)
    return f"Unlike Done."


@docs.tags('B.5 Instagram All Actions')
@docs.summary("Perform All Actions.")
@docs(description="""**You can perform all actions randomly based on hashtag.**\n
    hashtag = Enter your hashtag.(ex: drilling_rigs)
    total_action = Enter how many actions you want to do.(ex: 5)
    text = Enter your comment text.(ex: interesting!)""", )
@post("/ig/actions/{hashtag}/{total_action}/{text}")
def random_action_with_hashtag(hashtag: str, total_action: int, text: str):
    instabot.interact_with_hashtag(hashtag=hashtag, num_posts=total_action, text=text)
    # return f"{action_type} Done without hash"
    return f"Done random action with hash"


@docs.tags('B.1 Instagram Authentications')
@docs.summary("Logout.")
@docs(description="""**You can logout whenever you want.**\n""", )
@get("/ig/actions/logout/")
def ig_logout_account():
    return instabot.logout()


# ==============================================================================================================
#                                              Pinterest Bot
# ==============================================================================================================
# ============================ Authentication ==========================
# login will obtain and store cookies for further use, they last around 15 days.
# NOTE: Since login will store the cookies in local file you don't need to call it more than 3-4 times a month.
@docs.tags('C.1 Pinterest AUTHENTICATIONS')
@docs.summary('Login.')
@docs(description="""**Run this for get login if needed.**\n
    """, )
@get("/pinterest/login/yes/")
def login_first():
    res = pinterest.login()
    return res


@docs.tags('C.1 Pinterest AUTHENTICATIONS')
@docs.summary('Logout.')
@docs(description="""**Run this for logout if needed.**\n
    """, )
@get("/pinterest/logout/")
def logout_call():
    res = pinterest.logout()
    return res


# ============================ Follow ==========================
@docs.tags('C.3 Pinterest FOLLOW')
@docs.summary('Get followings.')
@docs(description="""**You can get your followings from here.**\n
    username = if you want to see your own then just leave it and press execute, otherwise give the username.""", )
@get("/pinterest/actions/get/followings/")
def get_followings(username: str = None):
    res = pinterest.get_following(username=username)
    return res


@docs.tags('C.3 Pinterest FOLLOW')
@docs.summary('Get followers.')
@docs(description="""**You can get your followers from here.**\n
    username = if you want to see your own then just leave it and press execute, otherwise give the username.""", )
@get("/pinterest/actions/get/followers/")
def get_followers(username: str = None):
    res = pinterest.get_user_followers(username=username)
    return res


@docs.tags('C.3 Pinterest FOLLOW')
@docs.summary('Follow user by username.')
@docs(description="""**You can follow a user by username from here.**\n
    username = Give the username who you want to follow.""", )
@get("/pinterest/actions/follow_user_by_username/{username}/")
def follow_user_by_username(username: str):
    res = pinterest.follow_user(username)
    return res.json()


@docs.tags('C.3 Pinterest FOLLOW')
@docs.summary('Unfollow user by username.')
@docs(description="""**You can unfollow a user by username from here.**\n
    username = Give the username who you want to unfollow.""", )
@get("/pinterest/actions/unfollow_user_by_username/{username}/")
def unfollow_user_by_username(username: str):
    res = pinterest.unfollow_user(username)
    return res.json()


@docs.tags('C.3 Pinterest FOLLOW')
@docs.summary('Follow user.')
@docs(description="""**You can follow a user randomly from your home feed.**\n
    *total_action = how many actions you want to perform.""", )
@get("/pinterest/actions/follow/randomly/{total_action}/")
def randomly_follow(total_action: int):
    res = pinterest.random_follow_user(total_action)
    # print(res)
    return res


# ============================ Like, Comment & Random Action ==========================

@docs.tags('C.2 Pinterest LIKE, COMMENT & RANDOM ACTIONS')
@docs.summary('Comment on post.')
@docs(description="""**You can comment on random post from you home feed.**\n
    *total_action = how many actions you want to perform.\n
    *comment_text = write the text what you want to write in a comment.""",
      )
@get("/pinterest/actions/comment/randomly/{total_action}/{comment_text}/")
def comment_randomly(total_action: int, comment_text: str):
    res = pinterest.random_comment_on_random_post(total_action, comment_text)
    # print(res)
    return res


@docs.tags('C.2 Pinterest LIKE, COMMENT & RANDOM ACTIONS')
@docs.summary('Random action.')
@docs(description="""**You can perform random action on random post from you home feed.**\n
    *total_action = how many actions you want to perform.\n
    *comment_text = write the text what you want to write in a comment.""")
@get("/pinterest/actions/random_action/{total_action}/{comment_texts}/")
def random_action_on_random_post(total_action: int, comment_texts: str):
    res = pinterest.engage_with_random_posts(total_action, comment_texts)
    print(res)
    return res


@docs.tags('C.2 Pinterest LIKE, COMMENT & RANDOM ACTIONS')
@docs.summary('Like a posts.')
@docs(description="""**You can like on random post from you home feed.**\n
    *total_action = how many actions you want to perform.\n
    react_type = Enter the number for react type {1:"love", 13:"star", 7:"balb", 11:"wow", 5:"haha"}. Default is love.\n
    """)
@get("/pinterest/actions/like/{total_action}")
def like_posts_randomly(total_action: int, react_type: int = None):
    res = pinterest.like_a_post_randomly(total_action, react_type)
    # print(res)
    return res


# pinterest_client = PinterestClient()


# ============================ Boards ==========================
# # Creating new board
@docs.tags("C.4 Pinterest BOARD's")
@docs.summary("Create board.")
@docs(description="""**You can create a new board.**\n
    *name = Enter the board name.
    *description = Enter description.
    *privacy = Enter privacy(PUBLIC, SECRET).
    """, )
@post("/pinterest/actions/creating_board/{name}/{description}/{privacy}")
def creating_board(name: str, description: str, privacy: str):
    board_data = pinterest_client.create_board(name=name, description=description, privacy=privacy.upper())
    return f"{name} is created successfully."


# # Get board id by name
@docs.tags("C.4 Pinterest BOARD's")
@docs.summary("Get board id.")
@docs(description="""**You can get a board id using board name.**\n
    *name = Enter the board name.
    """, )
@get("/pinterest/actions/get_board_id/{name}")
def get_board_id_by_name(name: str):
    res = pinterest_client.get_board_id_by_name(name=name)
    return f"Board ID: {res[0]}, Board Name: {res[1]}"


# # Update board using name
@docs.tags("C.4 Pinterest BOARD's")
@docs.summary("Update a board.")
@docs(description="""**You can update a board info using board name.**\n
    *board_name = Enter the current board name which one you want to update.
    new_name = Enter the new name for board that you want to update.
    description = Enter description.
    privacy = Enter privacy(PUBLIC, SECRET).
    """, )
@patch("/pinterest/actions/update_board/{board_name}/")
def update_board_info(board_name: str, new_name: str = None, description: str = None, privacy: str = None):
    res = pinterest_client.upadte_board(name=board_name,
                                        new_name=new_name,
                                        description=description,
                                        privacy=privacy)
    return res


# # Delete board using name
@docs.tags("C.4 Pinterest BOARD's")
@docs.summary("Delete a board.")
@docs(description="""**You can delete a board using board name.**\n
    *name = Enter the board name which one you want to delete.
    """, )
@delete("/pinterest/actions/delete_board/{name}")
def delete_board_by_name(name: str):
    res = pinterest_client.delete_board(name)
    return f"Delete the board name: {name}"


# ============================ Pins ==========================
# # Get pins of a specific board find out by board name.
@docs.tags("C.5 Pinterest PIN's")
@docs.summary('Get boards pins.')
@docs(description="""**You can get all pins from a specific board.**\n
    *name = Enter the board name.""", )
@get("/pinterest/actions/get_boards_pins/{name}")
def get_pins_of_specific_board(name: str):
    res = pinterest_client.get_pins_on_board(name=name)
    return res


# # Creating pin in a board
@docs.tags("C.5 Pinterest PIN's")
@docs.summary('Create pin on boards.')
@docs(description="""**You can create pins on a specific board.**\n
    *board_name = Enter the board name.
    *pin_title = Enter the pin_title.
    *pin_description = Enter the pin_description.
    *img_url = Enter the image path.
    note = Enter a note on this pin.
    """, )
@post("/pinterest/actions/create_pin/{board_name}/{pin_title}/{pin_description}/{img_url}")
def create_pin_on_board(board_name: str, pin_title: str, pin_description: str, img_url: str, note: str = None):
    res = pinterest_client.create_pin(board_name=board_name, pin_title=pin_title,
                                      pin_description=pin_description, img_url=img_url, note=note)
    return res


# # Get pins list
@docs.tags("C.5 Pinterest PIN's")
@docs.summary("Get pin's.")
@docs(description="""**You can get all pin's from all board's.**\n""", )
@get("/pinterest/actions/get_pins_list/")
def get_pins_list():
    res = pinterest_client.get_pins_list()
    return res


# # All pins details
@docs.tags("C.5 Pinterest PIN's")
@docs.summary("Get pin's details.")
@docs(description="""**You can get all pin's details from all board's.**\n""", )
@get("/pinterest/actions/pins_details/")
def get_all_pins_details():
    res = pinterest_client.get_all_pins_details()
    return res


# # Get pins ID by pins title
@docs.tags("C.5 Pinterest PIN's")
@docs.summary("Get pin ID.")
@docs(description="""**You can create pins on a specific board.**\n
    *board_name = Enter the board name where the pin is located.
    *pin_title = Enter the pin_title.
    """, )
@get("/pinterest/actions/get_pin_id_by_title/{board_name}/{pin_title}")
def get_pin_id_by_title(board_name: str, pin_title: str):
    res = pinterest_client.get_pin_id_by_title(board_name=board_name, pin_title=pin_title)
    return res


# # Save a pin
@docs.tags("C.5 Pinterest PIN's")
@docs.summary("Save a pin.")
@docs(description="""**You can save a pins on a specific board.**\n
    *board_name = Enter the board name where the pin is located.
    *pin_id = Enter the pin_id.
    """, )
@post("/pinterest/actions/save_pin/{board_name}/{pin_id}/")
def save_a_pin(board_name: str, pin_id: str):
    res = pinterest_client.save_pin(name=board_name, pin_id=pin_id)
    return res.json()


# # Delete a pin by giving board name and pin title
@docs.tags("C.5 Pinterest PIN's")
@docs.summary("Delete a pin.")
@docs(description="""**You can delete a pin from a board.**\n
    *board_name = Enter the board name where the pin is located.
    *pin_title = Enter the pin_title.
    """, )
@delete("/pinterest/actions/delete_pin/{board_name}/{pin_title}/")
def delete_pin(board_name: str, pin_title: str):
    res = pinterest_client.delete_pin(board_name=board_name, pin_title=pin_title)
    return f"Delete Successfully! Board Name: {board_name}, Pin Title: {pin_title}"


# # # Get followers list
# @get("/actions/followers_list/")
# def follower_list():
#     res = pinterest_client.follower_list()
#     return res.json()
#
#
# # # Get followings list
# @get("/actions/following_list/")
# def following_list():
#     res = pinterest_client.following_list()
#     return res.json()


# ===================== This is currently in BETA mode ========================================
# @post("/actions/follow_user/{user_name}")
# def follow_user(user_name: str):
#     res = pinterest_client.follow_user(username=user_name)
#     return res.json()


# ==============================================================================================================
#                                                   Reddit Bot
# ==============================================================================================================
# ========================================== Creating Submission ======================================================
@docs.tags('D.1 Reddit Create')
@docs.summary('Create submission.')
@docs(description="""**You can create a submission from here.**\n
    subreddit = Enter the subreddit name. (ex: test)
    title = Enter the submissions title. (ex: this is a title)
    url = Enter your desired url if you want to add. Otherwise leave it blank. (ex: https://www.reddit.com/r/goldenretriever/comments/1bmy50z/8_years_his_names_max/)
    """, )
@post("/reddit/actions/create/submissions/{subreddit}/{title}")
def create_submission(subreddit: str, title: str, url: str = None):
    res = reddit.create_submission(subreddit=subreddit, title=title, url=url)
    return res


# ========================================== Comment Section ======================================================
@docs.tags('D.2 Reddit Comment')
@docs.summary('Comment by url.')
@docs(description="""**You can create a comment on a submission by url from here.**\n
    submission_url = Enter the URL of the submission where you want to comment. (ex: https://www.reddit.com/comments/1bmnkcf)
    text = Enter the text of your comment. (ex: wow)
    """, )
@get("/reddit/actions/create/comment/{submission_url}/{text}")
def create_comment(submission_url: str, text: str):
    try:
        # Call the method to create a comment
        res = reddit.comment_on_submission(submission_url=submission_url, text=text)
        return res
    except Exception as e:
        return {'success': False, 'message': f"An error occurred while creating comment: {e}"}


@docs.tags('D.2 Reddit Comment')
@docs.summary('Comment randomly.')
@docs(description="""**You can create comments on random posts from here.**\n
    section = Specify the section from where to fetch random posts (e.g., new, hot, top).
    num_posts = Specify the number of random posts to fetch.
    text = Enter the text of your comment.
    """, )
@get("/reddit/actions/create/comment/random/{section}/{num_posts}/{text}")
def create_comment_on_random_posts(section: str, num_posts: int, text: str):
    try:
        # Call the method to fetch random posts and create comments
        res = reddit.comment_on_random_posts(section=section, num_posts=num_posts, comments=text)
        return res
    except Exception as e:
        return {'success': False, 'message': f"An error occurred while creating comments on random posts: {e}"}


# ========================================== Save Section ======================================================

@docs.tags('D.3 Reddit Save')
@docs.summary('Save by url.')
@docs(description="""**You can create a comment on a submission by url from here.**\n
    submission_url = Enter the URL of the submission that you want to save. (ex: https://www.reddit.com/comments/1bmnkcf)
    """, )
@get("/reddit/actions/save/{submission_url}")
def save_submission_by_url(submission_url: str):
    res = reddit.save_submission(submission_url=submission_url)
    return res


# ========================================== Follow Section ======================================================

@docs.tags('D.4 Reddit FOLLOW')
@docs.summary('Get all following.')
@docs(description="""**You can get all followings from here.**\n""", )
@get("/reddit/actions/get/followings/")
def get_followings():
    res = reddit.get_followings()
    return res


@docs.tags('D.4 Reddit FOLLOW')
@docs.summary('Follow random user by subreddit.')
@docs(description="""**You can follow a user from here.**\n
    subreddit_name = Enter the subreddit name which type of contents users you want to follow.(ex: "python", "television")
    num_of_action = Enter number of how many actions you want to perform.""")
@get("/reddit/actions/follow_user/{subreddit_name}/{num_of_action}/")
def follow_authors(subreddit_name: str, num_of_action: int):
    res = reddit.follow_authors(subreddit_name=subreddit_name, num_of_actions=num_of_action)
    return res


@docs.tags('D.4 Reddit FOLLOW')
@docs.summary('Follow user by username.')
@docs(description="""**You can follow a user by username from here.**\n
    username = Give the username who you want to follow.""", )
@get("/reddit/actions/follow_user/{username}/")
def follow_author_by_username(username: str):
    res = reddit.follow_user_by_username(username=username)
    return res


@docs.tags('D.4 Reddit FOLLOW')
@docs.summary('Unfollow user by username.')
@docs(description="""**You can unfollow a user from here.**\n
    username = Enter the username who you want to unfollow.""", )
@get("/reddit/actions/unfollow_user/{username}/")
def unfollow_author_by_username(username: str):
    res = reddit.unfollow_user(username=username)
    return res


# ========================================== Random Action =====================================================

@docs.tags('D.5 Reddit Random Action')
@docs.summary('Perform random action.')
@docs(description="""**Randomly choose posts and perform randomly upvote, comment, and save post.**\n
    section = Enter the section name.(ex: new, hot, top)
    num_of_action = Enter number of how many actions you want to perform.""", )
@get("/reddit/actions/random_action/{section}/{num_of_action}/")
def random_action(section: str, num_of_action: int):
    res = reddit.perform_random_actions_on_posts(section=section, num_actions=num_of_action)
    # print(res.json())
    return res


# ========================================== Voting Section ======================================================

@docs.tags('D.6 Reddit Vote')
@docs.summary('Random upvoting.')
@docs(description="""**Randomly choose posts and perform upvoting.**\n
    section = Enter the section name.(ex: new, hot, top)
    num_of_action = Enter number of how many actions you want to perform.""", )
@get('/reddit/actions/upvote/{section}/{num_of_action}')
def upvote_on_random_post(section: str, num_of_action: int):
    res = reddit.upvote_random_posts(section=section, num_posts=num_of_action)
    return res


@docs.tags('D.6 Reddit Vote')
@docs.summary('Upvoting by url.')
@docs(description="""**You can upvoting on posts by giving url.**\n
    url = Enter the url. (ex: https://www.reddit.com/comments/1bmnkcf)""")
@get('/reddit/actions/upvote_by_url/{url}/')
def upvote_by_url(url: str):
    res = reddit.upvote_submission(submission_url=url)
    return res


@docs.tags('D.6 Reddit Vote')
@docs.summary('Downvoting by url.')
@docs(description="""**You can downvoting on posts by giving url.**\n
    url = Enter the url. (ex: https://www.reddit.com/comments/1bmnkcf)""")
@get('/reddit/actions/downvote_by_url/{url}/')
def downvote_by_url(url: str):
    res = reddit.downvote_submission(submission_url=url)
    return res


# ========================================== Share Section ======================================================

@docs.tags("D.7 Reddit Share")
@docs.summary('Share by url.')
@docs(description="""**You can share a post by giving url.**\n
    url = Enter the url. (ex: https://www.reddit.com/comments/1bmnkcf)
    new_subreddit = Enter your subreddit. (ex: test)
    comment = Enter a comment.""")
@get("/reddit/actions/repost/{url}/{new_subreddit}")
def repost_by_url(url: str, new_subreddit: str, comment: str = None):
    res = reddit.repost_by_url(url, new_subreddit, comment)
    print(res)
    return res


@docs.tags("D.7 Reddit Share")
@docs.summary('Share random posts.')
@docs(description="""**You can share random post.**\n
    section = Enter the section name.(ex: new, hot, top).
    num_posts = Enter number of how many actions you want to perform.
    new_subreddit = Enter your subreddit. (ex: test)
    comment = Enter a comment.""")
@get("/reddit/actions/repost/{section}/{num_posts}/{new_subreddit}")
def repost_randomly(section: str, num_posts: int, new_subreddit: str, comment: str = None):
    res = reddit.repost_random_posts(section=section, num_posts=num_posts, new_subreddit=new_subreddit, comment=comment)
    print(res)
    return res


# ==============================================================================================================
#                                              Facebook Group Bot
# ==============================================================================================================

@docs.tags('F.2 FB Group Authentication')
@docs.summary('Login First.')
@docs(description="""**You should log-in first for perform action or you cant perform any actions.**\n
    email = Enter your facebook email.
    password = Enter your facebook password.
    """, )
@get("/fb/action/login/{email}/{password}")
def login(email: str, password: str):
    res = login_kar.login1(email, password)
    if 'SomeThing Went Wrong' in res:
        return res
    elif 'Facebook Account Is In Checkpoint' in res:
        return "Facebook Account Is In Checkpoint. Login Another Account"
    return "Successfully login done!"


@docs.tags('F.2 FB Group Authentication')
@docs.summary('Check authentication.')
@docs(description="""**Check if you are log in or not.**\n
    """, )
@get("/fb/check/authentication/")
def check_if_authenticated_or_not():
    path = 'Facebook_Groups_version2/developer_file_donot_open/token.txt'
    if os.path.exists(path):
        return 'Welcome! You are already logged in!'
    else:
        return 'Sorry! You are not logged-in. You should log-in first to make actions. Thank You'


@docs.tags('F.2 FB Group Authentication')
@docs.summary('Logout.')
@docs(description="""**Logout from here if you need.**\n
    """, )
@get('/fb/actions/logout/')
def delete_tokens():
    path1 = 'Facebook_Groups_version2/developer_file_donot_open/token.txt'
    path2 = 'cookies/facebook.pkl'
    if os.path.exists(path1):
        os.remove(path1)
    if os.path.exists(path2):
        os.remove(path2)


# ================================================================================================================
@docs.tags('F.1 FB Group See All Actions')
@docs.summary('See all actions.')
@docs(description="""**You can see what actions you can perform from here.**\n""", )
@get("/fb/actions/options/")
def all_actions():
    menu = (
        f"1. Extract groups by names, keywords (Most Demand)  \n"
        f"2. Extract groups by other groups ids (Unlimmited Groups) \n"
        f"3. Extract groups by names with countries   (Filter Country)  \n"
        f"4. Perform actions on groups    Need-Login    \n"
    )
    return menu


# ================================================================================================================

@docs.tags('F.3 FB Group Group Operations')
@docs.summary('Group by keyword.')
@docs(description="""**You can find groups using keywords.**\n
    group_names = Enter keyword what type of groups you want to find.
    """, )
@get("/fb/actions/group/by/groups_name/{group_names}")
def group_by_groups_name(group_names: str):
    return main_instance.groups_by_names_keywords(group_names=group_names)


@docs.tags('F.3 FB Group Group Operations')
@docs.summary('Group by id.')
@docs(description="""**You can find groups using groups id. From collected groups data you should copy past the ID in
input.txt. Should be more than 1 group ID in the file.**\n
    """, )
@get("/fb/actions/group/by/id")
def group_by_id():
    return main_instance.group_by_id()


@docs.tags('F.3 FB Group Group Operations')
@docs.summary('Group by country.')
@docs(description="""**You can filtering groups using country name.**\n
    group_names = Enter group names.
    country_names = Enter country names.
    """, )
@get("/fb/actions/group/by/country/{group_names}/{country_names}")
def group_by_country(group_names: str, country_names: str):
    return main_instance.group_by_country(group_names=group_names, country_names=country_names)


@docs.tags('F.3 FB Group Group Operations')
@docs.summary('Perform action on group.')
@docs(description="""**You can like comment share on groups post. This is performing on input.txt file.**\n
    """, )
@get("/fb/actions/perform/action/")
def perform_random_action_on_groups():
    return main_instance_no_login.perform_actions_on_groups()


# ================================================================================================================
@docs.tags('F.4 FB Group Grab ID')
@docs.summary('Separate ID from file.')
@docs(description="""**You can separate ID from text files which is need for finding groups.**\n
    file_name = Enter file_name.(ex: groups_by_names_2024-02-14.15.42.54.txt)
    """, )
@get("/fb/actions/split/data/{file_name}")
def split_endpoint(file_name):
    # Read data from the input text file
    with open('./Facebook_Groups_version2/data/' + file_name, 'r') as file:
        data = file.readlines()

    # Extract IDs from the data
    ids = []
    for line in data:
        parts = line.split('|')
        ids.append(parts[0])

    # Write IDs to a new text file
    with open('Facebook_Groups_version2/data/split.txt', 'w') as file:
        for id in ids:
            file.write(id + '\n')

    return "IDs have been extracted and stored in 'Facebook_Groups_version2/data/split.txt' file."


# ===============================================================================================================
#                                              Whats App Group Bot
# ===============================================================================================================


@docs.tags('E.1 WhatsApp Home')
@docs.summary('See all actions 🏠.')
@get("/wa/home")
def home():
    return (f"You can find the group info of the whatsapp group.\n1. Check Groups Members 👥: "
            f"'You will find out how many participant in a group by giving the group name.'\n"
            f"2. Collect Contact Info ☎️:'You can collect the phone numbers of participants by giving the group name.'")


@docs.tags('E.2 WhatsApp Group')
@docs.summary("Check Groups Member's 👥.")
@docs(description="""**You can find the total number of group members.**\n
    group_name = Enter the name of group.(ex: My Test Group)""", )
@get("/wa/actions/group/number_of_members/{group_name}")
def number_of_members(group_name: str):
    res = wa.get_number_of_participants(group_name)
    print(res)
    return res


@docs.tags('E.2 WhatsApp Group')
@docs.summary('Collect Contact Info ☎️.')
@docs(description="""**You can collect contact Info of group members from a group.**\n
    group_name = Enter the name of group.(ex: My Test Group)""", )
@get("/wa/actions/group/contact/number_of_members/{group_name}")
def contact_info_of_members(group_name: str):
    res = wa.get_group_members_info(group_name)

    return res


@docs.tags('E.2 WhatsApp Group')
@docs.summary('Join by invite link 🔗.')
@docs(description="""**You can join a group by groups invitation.**\n
    link = Enter the link.(ex: https://chat.whatsapp.com/4fy62abhcGb9tmmVP3AQtI)""", )
@get("/wa/action/join/group/{link}")
def join_group(link: str):
    res = wa.join_a_group_by_link(link)
    return res


# ===============================================================================================================
#                                              Linked-in Bot
# ===============================================================================================================

@dataclass
class Linked_in_Credentials:
    email: str
    password: str


@docs.tags('G.2 Linkedin Post Create')
@docs.summary('Create Post.')
@post("/in/create_post/{content}")
def create_post(credentials: Linked_in_Credentials, content: str):
    # return 'hello'
    try:
        # ic(credentials)
        linkedinbot = Linkedin(username=credentials.email, password=credentials.password)
        linkedinbot.login_linkedin()
        linkedinbot.post_in_feed(content)
        linkedinbot.quit_browser()
        return {'Status': 'Posted'}
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_type, exc_tb.tb_lineno)
        return {'error': f'{exc_type}, {exc_tb.tb_lineno}'}


@docs.tags('G.2 Linkedin Post Create')
@docs.summary('Create Post in a Group.')
@post("/in/create_post_group/{content}/{group_id}")
def create_post_to_group(credentials: Linked_in_Credentials, content: str, group_id):
    linkedinbot = Linkedin(username=credentials.email, password=credentials.password)
    linkedinbot.login_linkedin()
    linkedinbot.post_to_group(group_id, content)
    linkedinbot.quit_browser()
    return {'Status': f'Posted to group {group_id}'}


@docs.tags('G.1 Linkedin Like')
@docs.summary('Like.')
@post("/in/like_posts_in_feed/{number_of_posts}")
def like_post_in_feed(credentials: Linked_in_Credentials, number_of_posts: int):
    linkedinbot = Linkedin(username=credentials.email, password=credentials.password)
    linkedinbot.login_linkedin()
    linkedinbot.like_on_post(number_of_posts)
    linkedinbot.quit_browser()
    return {'Status': f'Liked {number_of_posts} post(s) in feed.'}


@docs.tags('G.3 Linkedin Post Share')
@docs.summary('Create Re-Post.')
@post("/in/repost/{number_of_posts}")
def re_post(credentials: Linked_in_Credentials, number_of_posts: int):
    # return 'hello'
    try:
        # ic(credentials)
        linkedinbot = Linkedin(username=credentials.email, password=credentials.password)
        linkedinbot.login_linkedin()
        linkedinbot.repost_a_post(number_of_posts)
        linkedinbot.quit_browser()
        return {'Status': f"Re-post Done on {number_of_posts} post's"}
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_type, exc_tb.tb_lineno)
        return {'error': f'{exc_type}, {exc_tb.tb_lineno}'}


@docs.tags('G.4 Linkedin Comment')
@docs.summary('Comment on a post.')
@post("/in/comment_on_post/{number_of_posts}/{comment_text}")
def comment_on_post(credentials: Linked_in_Credentials, number_of_posts: int, comment_text: str):
    # return 'hello'
    try:
        # ic(credentials)
        linkedinbot = Linkedin(username=credentials.email, password=credentials.password)
        linkedinbot.login_linkedin()
        linkedinbot.comment_on_posts(number_of_posts, comment_text)
        linkedinbot.quit_browser()
        return {'Status': f"Comment Done on {number_of_posts} post's"}
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_type, exc_tb.tb_lineno)
        return {'error': f'{exc_type}, {exc_tb.tb_lineno}'}
