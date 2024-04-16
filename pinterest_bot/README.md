
# Pinterest Bot
## Description
**Pinterest Bot** is an Pinterest automation tool that helps you engage with your target audience effectively. With Pinterest Bot, you can automatically like, comment, and follow users.
## Tech Stack

- Python >= 3.5.0
- py3-pinterest


## Features

- AUTHENTICATIONS 
- BOARD's
- FOLLOW
- LIKE
- COMMENT 
- RANDOM ACTIONS
- PIN's
## Installation and setup the project

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
PINTEREST_USERNAME=
PINTEREST_EMAIL=
PINTEREST_PASSWORD=
PINTEREST_APP_ID=
PINTEREST_APP_SECRET=
PINTEREST_REFRESH_ACCESS_TOKEN=
PINTEREST_ACCESS_TOKEN_SANDBOX=(if need otherwise ignore it)
PINTEREST_ACCESS_TOKEN=
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
Pinterest-bot
|
|---venv
|
|---cred_root(it will automatice create when login)
|
|---py3pin
|
|---Examples
|
|---.env
|
|---.env.examples
|
|---server.py
|
|---setup.py
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

#### ⇒ Authentications
- Login
```http
  GET /actions/login/yes
```
- Logout
```http
  GET /actions/logout
```


#### ⇒ Like
- *total_action = how many actions you want to perform.

- react_type = Enter the number for react type {1:"love", 13:"star", 7:"balb", 11:"wow", 5:"haha"}. Default is love.
```http
POST /actions/like/{total_action}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `total_action` | `int` | Enter how many like you want to do. (ex: 5) |YES|
| `react_type` | `int` | Define hashtag relevant to your interests or niche. (ex: drilling_rigs) |NO|


#### ⇒ Comments
- *total_action = how many actions you want to perform.

- *comment_text = write the text what you want to write in a comment.
```http
  GET /actions/comment/randomly/{total_action}/{comment_text}
```
| Parameter | Type     | Description                |Required|
| :-------- | :------- | :------------------------- |:-------|
| `total_action` | `int` | Enter how many comment you want to do. (ex: 5) |YES|
| `comment_text` | `string` | Enter your comment text. (ex: interesting!) |YES|


#### ⇒ Random Action
**You can perform random action on random post from you home feed.**
- *total_action = how many actions you want to perform.

- *comment_text = write the text what you want to write in a comment.
```http
  GET /actions/random_action/{total_action}/{comment_texts}
```
| Parameter | Type     | Description                |Required|
| :-------- | :------- | :------------------------- |:-------|
| `total_action` | `int` | Enter how many comment you want to do. (ex: 5) |YES|
| `comment_text` | `string` | Enter your comment text. (ex: interesting!) |YES|


#### ⇒ Follow/Unfollow
- Get Followings
```http
GET /actions/get/followings
```

| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `username` | `string` | Enter username to get the followings.|YES|

- Get Followers
```http
GET /actions/get/followers
```

| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `username` | `string` | Enter username to get the followers|YES|

- Randomly follow
```http
GET /actions/follow/randomly/{total_action}
```

| Parameter | Type     | Description                |Required|
| :-------- | :------- | :------------------------- |:-------|
| `total_action` | `int` | Enter how many people you want to follow. (ex: 5) |YES|

- Follow user by username

```http
GET /actions/follow_user_by_username/{username}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `username` | `string` | Enter username who you want to follow.|YES|

- Unfollow user by username
```http
GET /actions/unfollow_user_by_username/{username}
```

| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `username` | `string` | Enter username who you want to unfollow.|YES|



#### ⇒ Board

- Get Board ID
```bash
GET /actions/get_board_id/{name}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `name` | `string` | Enter board name to get board id.|YES|


- Create Board
```bash
POST /actions/creating_board/{name}/{description}/{privacy}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `name` | `string` | The name of the new board.|YES|
| `description` | `string` | Description of the new board.|YES|
| `privacy` | `string` | Privacy setting for the board (ex: PUBLIC/SECRET).|YES|


- Update Board
```bash
PATCH /actions/update_board/{board_name}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `board_name` | `string` | The name of the board to be updated.|YES|
| `new_name` | `string` | New name for the board.|NO|
|`description`|`string`|New description for the board.|NO|
| `privacy` | `string` | New privacy setting for the board (ex: PUBLIC/SECRET).|NO|


- Delete Board
```bash
DELETE /actions/delete_board/{name}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `name` | `string` | The name of the board to be deleted.|YES|



#### ⇒ Pin
- Get all pin's
```bash
GET /actions/get_pins_list
```
- Get all pin details
```bash
GET /actions/pins_details
```

- Get all pin's from a specific board
```bash
GET /actions/get_boards_pins/{name}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `name` | `string` | Enter the board name.|YES|


- Get Pin ID by Title
```bash
GET /actions/get_pin_id_by_title/{board_name}/{pin_title}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `board_name` | `string` | The name of the board where the pin is located.|YES|
| `pin_title` | `string` | The title of the pin.|YES|


- Save Pin
```bash
POST /actions/save_pin/{board_name}/{pin_id}
```

| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `board_name` | `string` | Name of the board where the pin will be saved.|YES|
| `pin_id` | `string` | ID of the pin to be saved.|YES|


- Create Pin
```bash
POST /actions/create_pin/{board_name}/{pin_title}/{pin_description}/{img_url}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `board_name` | `string` | Name of the board where the pin will be created.|YES|
| `pin_title` | `string` | Title of the pin.|YES|
|`pin_description`|`string`|Description of the pin.|YES|
|`img_url`|`string`|URL of the image to be attached to the pin.|YES|
| `note` | `string` | Note to attach to the pin.|NO|


- Delete Pin
```bash
DELETE /actions/delete_pin/{board_name}/{pin_title}
```
| Parameter | Type     | Description                       |Required|
| :-------- | :------- | :-------------------------------- |:-------|
| `board_name` | `string` | Enter the board name where the pin is located.|YES|
|`pin_title`|`string`|Enter the pin_title.|YES|


## Conclusion
The Pinterest bot offers a robust set of features for automating interactions on the platform. From managing boards to engaging with users through likes, comments, and follows, it streamlines Pinterest activities efficiently. With auto-liking functionalities, users can expand their reach and attract new followers effortlessly. Simplifying pin management, the bot allows for easy creation, saving, and organization of content. With clear documentation and user-friendly endpoints, integrating the Pinterest bot into your workflow is seamless, enhancing your Pinterest strategy through automation.