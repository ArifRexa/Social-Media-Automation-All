from py3pin.Pinterest import Pinterest, PinterestClient
from blacksheep import Application, get, post, delete, patch
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info
import os
from dotenv import load_dotenv

# import requests

app = Application()
docs = OpenAPIHandler(info=Info(title="Pinterest API", version="0.0.1"), ui_path="/")
docs.bind_app(app)
load_dotenv()
pinterest = Pinterest()
# pinterest = Pinterest(
#     email=os.getenv("PINTEREST_EMAIL"),
#     password=os.getenv("PINTEREST_PASSWORD"),
#     username=os.getenv("PINTEREST_USERNAME"),
#     cred_root='cred_root')


# ============================ Authentication ==========================
# login will obtain and store cookies for further use, they last around 15 days.
# NOTE: Since login will store the cookies in local file you don't need to call it more then 3-4 times a month.
@docs.tags('AUTHENTICATIONS')
@docs.summary('Login.')
@docs(description="""**Run this for get login if needed.**\n
    """, )
@get("/login/yes/")
def login_first():
    res = pinterest.login()
    return res


@docs.tags('AUTHENTICATIONS')
@docs.summary('Logout.')
@docs(description="""**Run this for logout if needed.**\n
    """, )
@get("/logout/")
def logout_call():
    res = pinterest.logout()
    return res


# ============================ Follow ==========================
@docs.tags('FOLLOW')
@docs.summary('Get followings.')
@docs(description="""**You can get your followings from here.**\n
    username = if you want to see your own then just leave it and press execute, otherwise give the username.""", )
@get("/actions/get/followings/")
def get_followings(username: str = None):
    res = pinterest.get_following(username=username)
    return res


@docs.tags('FOLLOW')
@docs.summary('Get followers.')
@docs(description="""**You can get your followers from here.**\n
    username = if you want to see your own then just leave it and press execute, otherwise give the username.""", )
@get("/actions/get/followers/")
def get_followers(username: str = None):
    res = pinterest.get_user_followers(username=username)
    return res


@docs.tags('FOLLOW')
@docs.summary('Follow user by username.')
@docs(description="""**You can follow a user by username from here.**\n
    username = Give the username who you want to follow.""", )
@get("/actions/follow_user_by_username/{username}/")
def follow_user_by_username(username: str):
    res = pinterest.follow_user(username)
    return res.json()


@docs.tags('FOLLOW')
@docs.summary('Unfollow user by username.')
@docs(description="""**You can unfollow a user by username from here.**\n
    username = Give the username who you want to unfollow.""", )
@get("/actions/unfollow_user_by_username/{username}/")
def unfollow_user_by_username(username: str):
    res = pinterest.unfollow_user(username)
    return res.json()


@docs.tags('FOLLOW')
@docs.summary('Follow user.')
@docs(description="""**You can follow a user randomly from your home feed.**\n
    *total_action = how many actions you want to perform.""", )
@get("/actions/follow/randomly/{total_action}/")
def randomly_follow(total_action: int):
    res = pinterest.random_follow_user(total_action)
    # print(res)
    return res


# ============================ Like, Comment & Random Action ==========================

@docs.tags('LIKE, COMMENT & RANDOM ACTIONS')
@docs.summary('Comment on post.')
@docs(description="""**You can comment on random post from you home feed.**\n
    *total_action = how many actions you want to perform.\n
    *comment_text = write the text what you want to write in a comment.""",
)
@get("/actions/comment/randomly/{total_action}/{comment_text}/")
def comment_randomly(total_action: int, comment_text: str):
    res = pinterest.random_comment_on_random_post(total_action, comment_text)
    # print(res)
    return res


@docs.tags('LIKE, COMMENT & RANDOM ACTIONS')
@docs.summary('Random action.')
@docs(description="""**You can perform random action on random post from you home feed.**\n
    *total_action = how many actions you want to perform.\n
    *comment_text = write the text what you want to write in a comment.""")
@get("/actions/random_action/{total_action}/{comment_texts}/")
def random_action_on_random_post(total_action: int, comment_texts: str):
    res = pinterest.engage_with_random_posts(total_action, comment_texts)
    print(res)
    return res


@docs.tags('LIKE, COMMENT & RANDOM ACTIONS')
@docs.summary('Like a posts.')
@docs(description="""**You can like on random post from you home feed.**\n
    *total_action = how many actions you want to perform.\n
    react_type = Enter the number for react type {1:"love", 13:"star", 7:"balb", 11:"wow", 5:"haha"}. Default is love.\n
    """)
@get("/actions/like/{total_action}")
def like_posts_randomly(total_action: int, react_type: int = None):
    res = pinterest.like_a_post_randomly(total_action, react_type)
    # print(res)
    return res


# '''
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# '''

pinterest_client = PinterestClient()


# ============================ Boards ==========================
# # Creating new board
@docs.tags("BOARD's")
@docs.summary("Create board.")
@docs(description="""**You can create a new board.**\n
    *name = Enter the board name.
    *description = Enter description.
    *privacy = Enter privacy(PUBLIC, SECRET).
    """, )
@post("/actions/creating_board/{name}/{description}/{privacy}")
def creating_board(name: str, description: str, privacy: str):
    board_data = pinterest_client.create_board(name=name, description=description, privacy=privacy.upper())
    return f"{name} is created successfully."


# # Get board id by name
@docs.tags("BOARD's")
@docs.summary("Get board id.")
@docs(description="""**You can get a board id using board name.**\n
    *name = Enter the board name.
    """, )
@get("/actions/get_board_id/{name}")
def get_board_id_by_name(name: str):
    res = pinterest_client.get_board_id_by_name(name=name)
    return f"Board ID: {res[0]}, Board Name: {res[1]}"


# # Update board using name
@docs.tags("BOARD's")
@docs.summary("Update a board.")
@docs(description="""**You can update a board info using board name.**\n
    *board_name = Enter the current board name which one you want to update.
    new_name = Enter the new name for board that you want to update.
    description = Enter description.
    privacy = Enter privacy(PUBLIC, SECRET).
    """, )
@patch("/actions/update_board/{board_name}/")
def update_board_info(board_name: str, new_name: str = None, description: str = None, privacy: str = None):
    res = pinterest_client.upadte_board(name=board_name,
                                        new_name=new_name,
                                        description=description,
                                        privacy=privacy)
    return res


# # Delete board using name
@docs.tags("BOARD's")
@docs.summary("Delete a board.")
@docs(description="""**You can delete a board using board name.**\n
    *name = Enter the board name which one you want to delete.
    """, )
@delete("/actions/delete_board/{name}")
def delete_board_by_name(name: str):
    res = pinterest_client.delete_board(name)
    return f"Delete the board name: {name}"


# ============================ Pins ==========================
# # Get pins of a specific board find out by board name.
@docs.tags("PIN's")
@docs.summary('Get boards pins.')
@docs(description="""**You can get all pins from a specific board.**\n
    *name = Enter the board name.""", )
@get("/actions/get_boards_pins/{name}")
def get_pins_of_specific_board(name: str):
    res = pinterest_client.get_pins_on_board(name=name)
    return res


# # Creating pin in a board
@docs.tags("PIN's")
@docs.summary('Create pin on boards.')
@docs(description="""**You can create pins on a specific board.**\n
    *board_name = Enter the board name.
    *pin_title = Enter the pin_title.
    *pin_description = Enter the pin_description.
    *img_url = Enter the image path.
    note = Enter a note on this pin.
    """, )
@post("/actions/create_pin/{board_name}/{pin_title}/{pin_description}/{img_url}")
def create_pin_on_board(board_name: str, pin_title: str, pin_description: str, img_url: str, note: str = None):
    res = pinterest_client.create_pin(board_name=board_name, pin_title=pin_title,
                                      pin_description=pin_description, img_url=img_url, note=note)
    return res


# # Get pins list
@docs.tags("PIN's")
@docs.summary("Get pin's.")
@docs(description="""**You can get all pin's from all board's.**\n""", )
@get("/actions/get_pins_list/")
def get_pins_list():
    res = pinterest_client.get_pins_list()
    return res


# # All pins details
@docs.tags("PIN's")
@docs.summary("Get pin's details.")
@docs(description="""**You can get all pin's details from all board's.**\n""", )
@get("/actions/pins_details/")
def get_all_pins_details():
    res = pinterest_client.get_all_pins_details()
    return res


# # Get pins ID by pins title
@docs.tags("PIN's")
@docs.summary("Get pin ID.")
@docs(description="""**You can create pins on a specific board.**\n
    *board_name = Enter the board name where the pin is located.
    *pin_title = Enter the pin_title.
    """, )
@get("/actions/get_pin_id_by_title/{board_name}/{pin_title}")
def get_pin_id_by_title(board_name: str, pin_title: str):
    res = pinterest_client.get_pin_id_by_title(board_name=board_name, pin_title=pin_title)
    return res


# # Save a pin
@docs.tags("PIN's")
@docs.summary("Save a pin.")
@docs(description="""**You can save a pins on a specific board.**\n
    *board_name = Enter the board name where the pin is located.
    *pin_id = Enter the pin_id.
    """, )
@post("/actions/save_pin/{board_name}/{pin_id}/")
def save_a_pin(board_name: str, pin_id: str):
    res = pinterest_client.save_pin(name=board_name, pin_id=pin_id)
    return res.json()


# # Delete a pin by giving board name and pin title
@docs.tags("PIN's")
@docs.summary("Delete a pin.")
@docs(description="""**You can delete a pin from a board.**\n
    *board_name = Enter the board name where the pin is located.
    *pin_title = Enter the pin_title.
    """, )
@delete("/actions/delete_pin/{board_name}/{pin_title}/")
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


def get_user_profile():
    return pinterest.get_user_overview(username='username')


def get_user_boards_batched(username=None):
    boards = []
    board_batch = pinterest.boards(username=username)
    while len(board_batch) > 0:
        boards += board_batch
        board_batch = pinterest.boards(username=username)

    return boards


def get_boards(username=None):
    return pinterest.boards_all(username=username)


def get_board_pins_batched(board_id=''):
    board_feed = []
    feed_batch = pinterest.board_feed(board_id=board_id)
    while len(feed_batch) > 0:
        board_feed += feed_batch
        feed_batch = pinterest.board_feed(board_id=board_id)

    return board_feed


def delete_pin(pin_id=''):
    # if pin doesn't exist or you have no rights to delete http 404 or 401 will be thrown
    return pinterest.delete_pin(pin_id=pin_id)


def follow(user_id=''):
    # even if you already follow this user a successful message is returned
    return pinterest.follow_user(user_id=user_id)


def unfollow(user_id=''):
    # even if you don't follow this user a successful message is returned
    return pinterest.unfollow_user(user_id=user_id)


def get_following_batched(username=None, max_items=500):
    # you can get following on any user, default is current user
    # pinterest.get_following(username='some_user')
    following = []
    following_batch = pinterest.get_following(username=username)
    while len(following_batch) > 0 and len(following) < max_items:
        following += following_batch
        following_batch = pinterest.get_following(username=username)

    return following


def get_following(username=None):
    # Gets full following list of a user
    return pinterest.get_following_all(username=username)


def get_followers_batched(username=None, max_items=500):
    followers = []
    followers_batch = pinterest.get_user_followers(username=username)
    while len(followers_batch) > 0 and len(followers) < max_items:
        followers += followers_batch
        followers_batch = pinterest.get_user_followers(username=username)

    return followers


def get_followers(username=None):
    # Gets a full list of user followers
    return pinterest.get_user_followers_all(username=username)


def get_home_feed(max_items=100):
    # This is what pinterest displays on your home page
    # useful for auto repins
    home_feed_pins = []
    home_feed_batch = pinterest.home_feed()
    while len(home_feed_batch) > 0 and len(home_feed_pins) < max_items:
        home_feed_pins += home_feed_batch
        home_feed_batch = pinterest.home_feed()

    return home_feed_pins


def repin(pin_id='', board_id='', section_id=None):
    return pinterest.repin(board_id=board_id, pin_id=pin_id, section_id=section_id)


def get_website_pinnable_images():
    # Pinterest endpoint that gives all images on website
    return pinterest.get_pinnable_images(url='https://www.tumblr.com/search/food')


def get_board_pin_recommendations(board_id='', max_items=100):
    rec_pins = []
    rec_batch = pinterest.board_recommendations(board_id=board_id)
    while len(rec_batch) > 0 and len(rec_pins) < max_items:
        rec_pins += rec_batch

    return rec_pins


def pin(board_id='',
        section_id=None,
        image_url='https://i.pinimg.com/170x/32/78/bd/3278bd27073e1ec9c8a708409279768b.jpg',
        description='this is auto pin',
        title='a bot did this',
        alt_text='alt text',
        link='https://www.google.com/'):
    return pinterest.pin(board_id=board_id, section_id=section_id, image_url=image_url,
                         alt_text=alt_text, description=description, title=title, link=link)


def upload_pin(board_id='',
               section_id=None,
               image_path='my_imag.png',
               description='this is auto pin',
               title='a bot did this',
               link='https://www.google.com/'):
    return pinterest.upload_pin(board_id=board_id, section_id=section_id, image_file=image_path,
                                description=description, title=title, link=link)


def search(max_items=100, scope='boards', query='food'):
    # After change in pinterest API, you can no longer search for users
    # Instead you need to search for something else and extract the user data from there.
    # current pinterest scopes are: pins, buyable_pins, my_pins, videos, boards
    results = []
    search_batch = pinterest.search(scope=scope, query=query)
    while len(search_batch) > 0 and len(results) < max_items:
        results += search_batch
        search_batch = pinterest.search(scope=scope, query=query)

    return results


def follow_board(board_id=''):
    return pinterest.follow_board(board_id=board_id)


def unfollow_board(board_id=''):
    return pinterest.unfollow_board(board_id=board_id)


def invite(board_id='', target_user_id=''):
    # If user is already invited to the board, you get 403 error.
    return pinterest.invite(board_id=board_id, user_id=target_user_id)


def delete_invite(board_id='', target_user_id=''):
    # If user is not invited to the board, you get 403 error.
    return pinterest.delete_invite(board_id=board_id, invited_user_id=target_user_id)


def get_board_invites(board_id=''):
    return pinterest.get_board_invites(board_id=board_id)


def comment_on_pin(pin_id='', comment_text='comment'):
    # Forbidden and not found are thrown if you don't have permissions or comment does not exist
    return pinterest.comment(pin_id=pin_id, text=comment_text)


def delete_comment(pin_id='', comment_id=''):
    # Forbidden and not found are thrown if you don't have permissions or comment does not exist
    return pinterest.delete_comment(pin_id=pin_id, comment_id=comment_id)


def get_pin_comments(pin_id=''):
    return pinterest.get_comments(pin_id=pin_id)


def load_pin_by_id(pin_id=''):
    return pinterest.load_pin(pin_id=pin_id)


# to pin/repin to section you just need to provide section id parameter to the respective function
# repin(board_id=board_id, section_id=section_id, pin_id='pin_id')
# pin(board_id=board_id, section_id=section_id)


# Careful with category names. They have different names than as shown on Pinterest
def create_board(name='',
                 description='',
                 category='other',
                 privacy='public',
                 layout='default'):
    return pinterest.create_board(name=name, description=description, category=category,
                                  privacy=privacy, layout=layout)


def create_board_section(board_id='', section_name=''):
    return pinterest.create_board_section(board_id=board_id, section_name=section_name)


def delete_board_section(section_id=''):
    return pinterest.delete_board_section(section_id=section_id)


def get_board_sections(board_id=''):
    return pinterest.get_board_sections(board_id=board_id)


def get_board_section_feed(section_id=''):
    return pinterest.get_section_pins(section_id=section_id)


def type_ahead(term="apple"):
    return pinterest.type_ahead(term=term)


def add_pin_note(pin_id, note='test note'):
    pinterest.add_pin_note(pin_id=pin_id, note=note)
