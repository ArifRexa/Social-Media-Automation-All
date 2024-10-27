import csv
from datetime import datetime
from server import (like_action_tumblr, like_action_on_tag_tumblr, reblog_action_on_tag_tumblr, reblog_action_tumblr,
                    reblog_action_with_comments_tumblr, reblog_action_on_tag_with_comment_tumblr,
                    random_actions_tumblr, random_actions_on_tag_tumblr, ig_like_action, ig_follow_action,
                    ig_follow_specific_users_by_username, ig_unfollow_specific_users_by_username,
                    ig_relevant_follow_action, ig_unfollow_non_followers, ig_comment_action,
                    ig_comment_action_on_condition, ig_save_media, ig_unlike_action, ig_send_message,
                    ig_login_account_method, ig_logout_account)


# ==================================================================================================================
# ======================================================Tumblr======================================================
# ==================================================================================================================
def get_tumblr_data_as_dict(csv_file):
    tumblr_data = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Get the header row
        for row in reader:
            social_network = row[0]
            if social_network.lower() == 'tumblr':
                tumblr_row = {}
                for i in range(len(header)):
                    if header[i] == 'Like/Unlike':
                        like_tag = row[i].split(';')
                        if len(like_tag) == 2:
                            tumblr_row['Like'] = like_tag[0]
                            tumblr_row['Like_Tag'] = like_tag[1]
                        else:
                            tumblr_row['Like'] = row[i]
                            tumblr_row['Like_Tag'] = None
                    elif header[i] == 'Re-Post/Share Post':
                        repost_tag = row[i].split(';')
                        if len(repost_tag) == 2:
                            tumblr_row['Re-Post'] = repost_tag[0]
                            tumblr_row['Re-Post_Tag'] = repost_tag[1]
                        else:
                            tumblr_row['Re-Post'] = row[i]
                            tumblr_row['Re-Post_Tag'] = None
                    elif header[i] == 'Comment':
                        # Check if the cell contains a comment
                        tumblr_row['Comment'] = row[i] if row[i] else None
                    else:
                        tumblr_row[header[i]] = row[i]
                tumblr_data.append(tumblr_row)
    return tumblr_data


# Example usage:
tumblr_data = get_tumblr_data_as_dict("command_csv_file/Social_Bots_Commands.csv")

# Print the first entry in the list of dictionary format
# print(tumblr_data[0])
first_row = tumblr_data[0]

# Get the values for like, like_tag, repost, and repost_tag
tumblr_like = first_row.get('Like')
tumblr_like_tag = first_row.get('Like_Tag')
tumblr_repost = first_row.get('Re-Post')
tumblr_repost_tag = first_row.get('Re-Post_Tag')
tumblr_first_row_comment = tumblr_data[0].get('Comment')


def perform_reblog_action(total_actions, my_blog_name, comment=None, tag=None):
    if comment:
        if tag:
            reblog_action_on_tag_with_comment_tumblr(total_actions=total_actions, my_blog_name=my_blog_name,
                                                     comment=comment, tag=tag)
        else:
            reblog_action_with_comments_tumblr(total_actions=total_actions, my_blog_name=my_blog_name,
                                               comment=comment)
    else:
        if tag:
            reblog_action_on_tag_tumblr(total_actions=total_actions, my_blog_name=my_blog_name, tag=tag)
        else:
            reblog_action_tumblr(total_actions=total_actions, my_blog_name=my_blog_name)


# Example usage:
my_blog_name = "My_Blog"

# print(like, like_tag, repost, repost_tag)


like_action_tumblr(total_actions=int(tumblr_like)) if tumblr_like_tag is None else like_action_on_tag_tumblr(
    total_actions=int(tumblr_like),
    tag=tumblr_like_tag)
perform_reblog_action(total_actions=int(tumblr_repost), my_blog_name=my_blog_name, comment=tumblr_first_row_comment,
                      tag=tumblr_repost_tag)

random_actions_on_tag_tumblr(tag=tumblr_like_tag, total_actions=int(tumblr_like),
                             my_blog_name=my_blog_name) if tumblr_like_tag else random_actions_tumblr(
    total_actions=int(tumblr_like), my_blog_name=my_blog_name)


# ===================================================================================================================
# =====================================================Instagram=====================================================
# ===================================================================================================================

def read_csv_properties(file_path):
    properties = {}

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Read the header row
        for row in reader:
            social_network = row[0]
            post_type = row[1]
            create_post = row[2] if row[2] else None
            like = int(row[3]) if row[3] else None
            like_hashtag = row[4] if row[4] else None
            unlike = int(row[5]) if row[5] else None
            # unlike_hashtag = row[6] if row[6] else None
            follow_user = int(row[6]) if row[6] else None
            follow_user_hashtag = row[7] if row[7] else None
            follow_user_by_username = row[8] if row[8] else None
            unfollow_user_by_username = row[9] if row[9] else None
            # view_profile_story = row[10] if row[10] else None
            comment = int(row[10]) if row[10] else None
            comment_hashtag = row[11] if row[11] else None
            comment_text = row[12] if row[12] else None
            save_bookmark = int(row[13]) if row[13] else None
            save_hashtag = row[14] if row[14] else None
            send_dm_message = row[15] if row[15] else None
            dm_text = row[16] if row[16] else None

            properties[social_network] = {
                "post_type": post_type,
                "create_post": create_post,
                "like": like,
                "like_hashtag": like_hashtag,
                "unlike": unlike,
                # "unlike_hashtag": unlike_hashtag,
                "follow_user": follow_user,
                "follow_user_hashtag": follow_user_hashtag,
                "follow_user_by_username": follow_user_by_username,
                "unfollow_user_by_username": unfollow_user_by_username,
                # "view_profile_story": view_profile_story,
                "comment": comment,
                "comment_hashtag": comment_hashtag,
                "comment_text": comment_text,
                "save_bookmark": save_bookmark,
                "save_hashtag": save_hashtag,
                "send_dm_message": send_dm_message,
                "dm_text": dm_text
            }

    return properties


# Example usage
file_path = 'command_csv_file/ig_commands.csv'
properties = read_csv_properties(file_path)
# print(properties)
# Extracting values and storing them in variables
ig_post_type = properties['Instagram']['post_type']
ig_create_post = properties['Instagram']['create_post']
ig_like_number = properties['Instagram']['like']
ig_like_hashtag = properties['Instagram']['like_hashtag']
ig_unlike_media_id = properties['Instagram']['unlike']
# ig_unlike_hashtag = properties['Instagram']['unlike_hashtag']
ig_follow_user_number = properties['Instagram']['follow_user']
ig_follow_user_hashtag = properties['Instagram']['follow_user_hashtag']
ig_follow_user_by_username = properties['Instagram']['follow_user_by_username']
ig_unfollow_user_by_username = properties['Instagram']['unfollow_user_by_username']
# ig_view_profile_story = properties['Instagram']['view_profile_story']
ig_comment_number = properties['Instagram']['comment']
ig_comment_hashtag = properties['Instagram']['comment_hashtag']
ig_comment_text = properties['Instagram']['comment_text']
ig_save_bookmark = properties['Instagram']['save_bookmark']
ig_save_hashtag = properties['Instagram']['save_hashtag']
ig_send_dm_message = properties['Instagram']['send_dm_message']
ig_dm_text = properties['Instagram']['dm_text']

# # Printing the variables to verify
# print("post_type:", ig_post_type)
# print("create_post:", ig_create_post)
# print("like:", ig_like_number)
# print("like_hashtag:", ig_like_hashtag)
# print("unlike:", ig_unlike_media_id)
# # print("unlike_hashtag:", unlike_hashtag)
# print("follow_user:", ig_follow_user_number)
# print("follow_user_hashtag:", ig_follow_user_hashtag)
# print("follow_user_by_username:", ig_follow_user_by_username)
# print("unfollow_user_by_username:", ig_unfollow_user_by_username)
# # print("view_profile_story:", view_profile_story)
# print("comment:", ig_comment_number)
# print("comment_hashtag:", ig_comment_hashtag)
# print("comment_text:", ig_comment_text)
# print("save_bookmark:", ig_save_bookmark)
# print("save_hashtag:", ig_save_hashtag)
# print("send_dm_message:", ig_send_dm_message)
# print("send_dm_text:", ig_dm_text)


# ig_login_account_method()
# user_name_list = ig_follow_user_by_username.split(";")
# for username in user_name_list:
#     ig_follow_specific_users_by_username(usernames=username)
#
# user_name_list = ig_unfollow_user_by_username.split(";")
# for username in user_name_list:
#     ig_unfollow_specific_users_by_username(usernames=username)
#
# ig_like_action(hashtag=ig_like_hashtag, total_action=int(ig_like_number))
#
# ig_follow_action(hashtag=ig_follow_user_hashtag, total_action=int(ig_follow_user_number))
#
# ig_relevant_follow_action(hashtag=ig_follow_user_hashtag)
#
# ig_unfollow_non_followers()
#
# ig_comment_action(hashtag=ig_comment_hashtag, total_action=int(ig_comment_number), text=ig_comment_text)
#
# ig_comment_action_on_condition(hashtag=ig_comment_hashtag, text=ig_comment_text)
# ig_save_media(hashtag=ig_save_hashtag, num_posts=int(ig_save_bookmark))
# ig_unlike_action(media_id=ig_unlike_media_id)
# ig_send_message(text=ig_dm_text, username=ig_send_dm_message)
#
# ig_logout_account()
