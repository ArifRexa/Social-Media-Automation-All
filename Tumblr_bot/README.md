
# Tumblr Bot
## Description
**The Tumblr Bot** for interacting with Tumblr's API. The bot enables users to like, reblog with comment on Tumblr dashboards or blogs randomly. 
## Tech Stack

- Python >= 2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*
- PyTumblr 0.1.2


## Features

- Like
- Reblog
- Random Action
- Filtered by tag

## Installation and setup the project

### Clone this project from

```bash
  git clone https://github.com/MojoDevAgentNine/Tumlr-api-blacksheep.git
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

### To run this project, you will need to add the following environment variables to your .env file
```bash
TUMBLR_CONSUMER_KEY='<your_consumer_key>'
TUMBLR_CONSUMER_SECRET='<your_consumer_secret>'
TUMBLR_TOKEN_KEY='<your_token_key>'
TUMBLR_TOKEN_SECRET='<your_token_secret>'
```

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
Tumblr-bot
|
|---venv
|
|---actions(package)
|   |
|   |---__init__.py
|   |
|   |---actions.py
|
|---.env
|---.env.examples
|
|---server.py
|
|---.gitignore
|---requirements.txt
|
|---README.md
|
|---.dockerignore
|---docker-compose.yml
|---Dockerfile

```


## Important Notice
- **Prioritize Login:** Always initiate the login process before accessing other functionalities to ensure authentication and enable full API access.
- **Minimize Function Calls:** Avoid excessive calls to API functions to prevent potential rate limits or other restrictions. Use the functions judiciously and only when necessary.
- **Optimize Login Frequency:** Reduce the frequency of login requests to minimize strain on our servers and maintain a smooth user experience.
- **Stay Informed:** Keep yourself updated with any changes or announcements regarding API usage guidelines to ensure compliance and optimal utilization of our services.
## API Reference


#### ⇒ Home
- Upvoting by url.
```http
GET /home
```

#### ⇒ Like
- Like some random posts
```http
GET /actions/like/{total_actions}
```
| Parameter       | Type  | Description                                           | Required |
|:----------------|:------|:------------------------------------------------------|:---------|
| `total_actions` | `int` | Enter number of how many actions you want to perform. | `YES`    |

- Like some random posts **based on tag**
```http
GET /actions/like/{tag}/{total_actions}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `tag`           | `string` | Enter the tag name.(ex: frog)                         | `YES`    |
| `total_actions` | `int`    | Enter number of how many actions you want to perform. | `YES`    |






#### ⇒ Random Action

- You can perform random action on random post from you home feed.
```http
  GET /actions/{my_blog_name}/{total_actions}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `my_blog_name`  | `string` | Enter your blog name.(ex: bot_blog)                   | `YES`    |
| `total_actions` | `int`    | Enter number of how many actions you want to perform. | `YES`    |

- You can perform random action on random post **based on tag** from you home feed.
```http
  GET /actions/{my_blog_name}/{tag}/{total_actions}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `my_blog_name`  | `string` | Enter your blog name.(ex: bot_blog)                   | `YES`    |
| `tag`           | `string` | Enter the tag name.(ex: frog)                         | `YES`    |
| `total_actions` | `int`    | Enter number of how many actions you want to perform. | `YES`    |




#### ⇒ Reblog

- Reblog random posts.
```http
  GET /actions/reblog/{my_blog_name}/{total_actions}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `my_blog_name`  | `string` | Enter your blog name.(ex: bot_blog)                   | `YES`    |
| `total_actions` | `int`    | Enter number of how many actions you want to perform. | `YES`    |



- Reblog random posts **based on tag**.
```http
  GET /actions/reblog/{my_blog_name}/{tag}/{total_actions}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `my_blog_name`  | `string` | Enter your blog name.(ex: bot_blog)                   | `YES`    |
| `tag`           | `string` | Enter the tag name.(ex: frog)                         | `YES`    |
| `total_actions` | `int`    | Enter number of how many actions you want to perform. | `YES`    |


- Reblog random posts with comment.
```http
  GET /actions/reblog/{my_blog_name}/{total_actions}/{comment}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `my_blog_name`  | `string` | Enter your blog name.(ex: bot_blog)                   | `YES`    |
| `total_actions` | `int`    | Enter number of how many actions you want to perform. | `YES`    |
| `comment`       | `string` | Enter your comment.                                   | `YES`    |



- Reblog random posts **based on tag** with comment.
```http
  GET /actions/reblog/{my_blog_name}/{tag}/{total_actions}/{comment}
```
| Parameter       | Type     | Description                                           | Required |
|:----------------|:---------|:------------------------------------------------------|:---------|
| `my_blog_name`  | `string` | Enter your blog name.(ex: bot_blog)                   | `YES`    |
| `tag`           | `string` | Enter the tag name.(ex: frog)                         | `YES`    |
| `total_actions` | `int`    | Enter number of how many actions you want to perform. | `YES`    |
| `comment`       | `string` | Enter your comment.                                   | `YES`    |















## Conclusion
This Tumblr bot offers a simple yet effective way to automate interactions on the Tumblr platform. With features like liking, sharing posts randomly, it adds a layer of engagement to your Tumblr experience. Whether you're exploring new content or seeking to increase your presence, this bot provides a versatile toolset. Remember to use it responsibly and adhere to Tumblr's API usage policies. Happy automating!