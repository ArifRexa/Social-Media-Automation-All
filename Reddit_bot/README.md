
# Reddit Bot
## Description
**The Reddit Bot** is a Python script designed to automate various tasks on the Reddit platform using the Reddit API. It performs a range of actions such as posting submissions, commenting on posts, interacting with users, and analyzing subreddit content. The bot can be customized and configured to perform specific tasks based on user-defined parameters.
## Tech Stack

- Python >= 3.7
- praw


## Features

- Comment

- Create

- FOLLOW

- Random Action

- Save

- Share

- Vote
## Installation and set up the project

### Clone this project from

```bash
  git clone https://github.com/MojoCreator/Bot-Social-Media.git
```
### Setup a virtual environment
- Ubuntu
```bash
  python3 -m venv venv
```
- Windows
```bash
  python -m venv venv
```
### Activate the virtual environment
- Ubuntu
```bash
  source venv/bin/activate
```
- Windows
```bash
  venv/Scripts/activate
```
### Run requirements.txt file to install all requirements
```bash
  pip install -r requirements.txt
```

### To run this project, you will need to add the following environment variables to your .env file in actions folder
```bash
CLIENT_ID="<your_client_id>"
CLIENT_SECRET="<your_client_secret_key>"
PASSWORD="<your_id_password>"
USER_AGENT="<app_name> by u/<username>"
REDDIT_USERNAME="<username>"
```
If you don't have any reddit app then goto 
```
https://www.reddit.com/prefs/apps/
```
Now create a new app and set up the credentials.


### Now run in you terminal 
```bash
  uvicorn server:app --port 44777 --reload
```




## Usage/Examples
Go to 
```bash
 http://127.0.0.1:44777
```

Other details and instructions are describe there
## Acknowledgements

**⇒ Project Structure**
```bash
Reddit-bot
|
|---venv
|
|---.env
|
|---.env.examples
|
|---reddit_bot.py
|
|---server.py
|
|---.gitignore
|
|---requirements.txt
|
|---README.md
```


## Important Notice
- **Prioritize Login:** Always initiate the login process before accessing other functionalities to ensure authentication and enable full API access.
- **Minimize Function Calls:** Avoid excessive calls to API functions to prevent potential rate limits or other restrictions. Use the functions judiciously and only when necessary.
- **Optimize Login Frequency:** Reduce the frequency of login requests to minimize strain on our servers and maintain a smooth user experience.
- **Stay Informed:** Keep yourself updated with any changes or announcements regarding API usage guidelines to ensure compliance and optimal utilization of our services.
## API Reference


#### ⇒ Vote
- Up voting by url.
```http
GET /actions/upvote_by_url/{url}
```
| Parameter | Type     | Description     | Required |
|:----------|:---------|:----------------|:---------|
| `url`     | `string` | Enter post url. | `YES`    |

- Down-voting by url.
```http
GET /actions/downvote_by_url/{url}
```
| Parameter | Type     | Description     | Required |
|:----------|:---------|:----------------|:---------|
| `url`     | `string` | Enter post url. | `YES`    |

- Random up voting.
```http
GET /actions/upvote/{section}/{num_of_action}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `section`       | `string` | Enter the section name.(ex: new, hot, top).           | `YES`    |
| `num_of_action` | `int`    | Enter number of how many actions you want to perform. | `YES`    |







#### ⇒ Comments
- Comments by url

```http
  GET /actions/create/comment/{submission_url}/{text}
```
| Parameter        | Type     | Description                                                | Required |
|:-----------------|:---------|:-----------------------------------------------------------|:---------|
| `submission_url` | `string` | Enter the URL of the submission where you want to comment. | `YES`    |
| `text`           | `string` | Enter your comment text. (ex: interesting!)                | `YES`    |


- Comments randomly

```http
  GET /actions/create/comment/random/{section}/{num_posts}/{text}
```
| Parameter   | Type     | Description                                                                 | Required |
|:------------|:---------|:----------------------------------------------------------------------------|:---------|
| `section`   | `string` | Specify the section from where to fetch random posts (e.g., new, hot, top). | `YES`    |
| `num_posts` | `int`    | Specify the number of random posts to fetch.                                | `YES`    |
| `text`      | `string` | Enter your comment text. (ex: interesting!)                                 | `YES`    |




#### ⇒ Follow/Unfollow
- Get Followings
```http
GET /actions/get/followings
```


- Follow user by username
```http
GET /actions/follow_user/{username}
```

| Parameter  | Type     | Description                                | Required |
|:-----------|:---------|:-------------------------------------------|:---------|
| `username` | `string` | Enter the username who you want to follow. | `YES`    |


- Unfollow user by username
```http
GET /actions/unfollow_user/{username}
```

| Parameter  | Type     | Description                                  | Required |
|:-----------|:---------|:---------------------------------------------|:---------|
| `username` | `string` | Enter the username who you want to unfollow. | `YES`    |


- Follow random user by subreddit.
```http
GET /actions/follow_user/{subreddit_name}/{num_of_action}
```
| Parameter        | Type     | Description                                                                                           | Required |
|:-----------------|:---------|:------------------------------------------------------------------------------------------------------|:---------|
| `subreddit_name` | `string` | Enter the subreddit name which type of contents users you want to follow.(ex: "python", "television") | `YES`    |
| `num_of_action`  | `int`    | Enter number of how many actions you want to perform.                                                 | `YES`    |



#### ⇒ Random Action

**You can perform random action on random post from you home feed.**
```http
  GET /actions/random_action/{section}/{num_of_action}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `section`       | `string` | Enter the section name.(ex: new, hot, top)            | `YES`    |
| `num_of_action` | `int`    | Enter number of how many actions you want to perform. | `YES`    |




#### ⇒ Create submission.
```bash
POST /actions/create/submissions/{subreddit}/{title}
```
| Parameter   | Type     | Description                                                          | Required |
|:------------|:---------|:---------------------------------------------------------------------|:---------|
| `subreddit` | `string` | Enter the subreddit name.                                            | `YES`    |
| `title`     | `string` | Enter the submissions title.                                         | `YES`    |
| `url`       | `string` | Enter your desired url if you want to add. Otherwise leave it blank. | `NO`     |




#### ⇒ Save submission.
```bash
POST /actions/save/{submission_url}
```
| Parameter        | Type     | Description                                            | Required |
|:-----------------|:---------|:-------------------------------------------------------|:---------|
| `submission_url` | `string` | Enter the URL of the submission that you want to save. | `YES`    |



#### ⇒ Share submission.
- Share submissions by url.
```bash
GET /actions/repost/{url}
```
| Parameter | Type     | Description      | Required |
|:----------|:---------|:-----------------|:---------|
| `url`     | `string` | Enter the url.   | `YES`    |
| `comment` | `string` | Enter a comment. | `NO`     |

- Share random submissions.
```bash
GET /actions/repost/{url}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `section`       | `string` | Enter the section name.(ex: new, hot, top)            | `YES`    |
| `num_of_action` | `int`    | Enter number of how many actions you want to perform. | `YES`    |
| `comment`       | `string` | Enter a comment.                                      | `NO`     |



## Conclusion
The Reddit Bot is a versatile tool designed to automate various tasks on the Reddit platform. From managing submissions to interacting with users and analyzing subreddit content, the bot streamlines processes and enhances user engagement. 