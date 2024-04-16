# Instagram Bot
## Description
**Instagram Bot** is an Instagram automation tool that helps you engage with your target audience effectively. With Instagram Bot, you can automatically like, comment, and follow users who are posting content relevant to your interests or niche.
## Tech Stack

- Python >= 3.9
- Instagrapi


## Features

- **Hashtag Targeting:** Specify hashtags related to your niche, and Instagram Bot will interact with posts that use those hashtags. This allows you to engage with users who are interested in similar topics.

- **User Interaction:** Interact with users by liking their posts, leaving comments, and following them, helping to increase engagement and attract new followers.

- **Auto-Liking:** Instagram Bot can automatically like posts that match your specified hashtags. Liking posts can help increase your visibility and attract new followers.

- **Auto-Commenting:** Leave meaningful comments that you have set on relevant posts to engage with users and start conversations. Bot can automatically comment on posts that match your selected hashtags.

- **Auto-Following:** Follow users who are posting content related to your niche. By following relevant users, you can increase your chances of building a targeted audience.

- **Photo Upload with Tagging:** Instagram Bot supports uploading photos to your Instagram account and tagging multiple people in the photos. This feature allows you to share content with your audience and engage with specific individuals by tagging them directly in your posts.

- **Story Upload:** Instagram Bot supports uploading stories to your Instagram account. Share engaging content with your audience through stories, keeping them informed and entertained.
## Installation and set up the project

### Clone this project from

```bash
  git clone https://github.com/MojoDevAgentNine/Instagram-Bot.git
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
INSTAGRAM_USERNAME="your_instagram_username"
INSTAGRAM_PASSWORD="your_instagram_password"
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
instagram-bot-api
|
|---venv
|
|---actions(package)
|       |
|       |---__init__.py
|       |
|       |---action_test.py
|
|---.env
|       
|---.env.examples
|
|---server.py
|
|---.gitignore
|
|---requirements.txt
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
```http
POST /actions/like/{hashtag}/{total_action}
```
| Parameter      | Type     | Description                                                             | Required |
|:---------------|:---------|:------------------------------------------------------------------------|:---------|
| `hashtag`      | `string` | Define hashtag relevant to your interests or niche. (ex: drilling_rigs) | `YES`    |
| `total_action` | `int`    | Enter how many like you want to do. (ex: 5)                             | `YES`    |


#### ⇒ Comments
- Comments on those post where owner has more than 2k followers on relevant niche.
```http
  POST /actions/comment/on_conditions/{hashtag}/{text}
```
| Parameter | Type     | Description                                                             | Required |
|:----------|:---------|:------------------------------------------------------------------------|:---------|
| `hashtag` | `string` | Define hashtag relevant to your interests or niche. (ex: drilling_rigs) | `YES`    |
| `text`    | `string` | Enter your comment text. (ex: interesting!)                             | `YES`    |


- Comments on relevant niche

```http
  POST /actions/comment/{hashtag}/{total_action}/{text}
```
| Parameter      | Type     | Description                                                             | Required |
|:---------------|:---------|:------------------------------------------------------------------------|:---------|
| `hashtag`      | `string` | Define hashtag relevant to your interests or niche. (ex: drilling_rigs) | `YES`    |
| `total_action` | `int`    | Enter how many actions you want to do. (ex: 5)                          | `YES`    |
| `text`         | `string` | Enter your comment text. (ex: interesting!)                             | `YES`    |


#### ⇒ Follow/Unfollow
- Follow those people who have more than 2k followers on relevant niche.
```http
POST /actions/follow/relevant/{hashtag}
```

| Parameter | Type     | Description                                                             | Required |
|:----------|:---------|:------------------------------------------------------------------------|:---------|
| `hashtag` | `string` | Define hashtag relevant to your interests or niche. (ex: drilling_rigs) | `YES`    |

- Follow people on relevant niche.
```bash
POST /actions/follow/{hashtag}/{total_action}
```
| Parameter      | Type     | Description                                                             | Required |
|:---------------|:---------|:------------------------------------------------------------------------|:---------|
| `hashtag`      | `string` | Define hashtag relevant to your interests or niche. (ex: drilling_rigs) | `YES`    |
| `total_action` | `int`    | Enter how many actions you want to do. (ex: 5)                          | `YES`    |

- Unfollow people who did not follow back.
```bash
PUT /actions/unfollow_non_followers
```


#### ⇒ Perform all actions (Like, Comments, Follow)

```http
  POST /actions/{hashtag}/{total_action}/{text}
```
| Parameter      | Type     | Description                                                             | Required |
|:---------------|:---------|:------------------------------------------------------------------------|:---------|
| `hashtag`      | `string` | Define hashtag relevant to your interests or niche. (ex: drilling_rigs) | `YES`    |
| `total_action` | `int`    | Enter how many actions you want to do. (ex: 5)                          | `YES`    |
| `text`         | `string` | Enter your comment text. (ex: interesting!)                             | `YES`    |



#### ⇒ Media
- Photo Upload
```http
POST /actions/upload_photo/{media_path}/{caption}
```
| Parameter           | Type     | Description                                           | Required |
|:--------------------|:---------|:------------------------------------------------------|:---------|
| `media_path`        | `string` | Enter path of your photos.(ex: /home/jp/my_photo.jpg) | `YES`    |
| `caption`           | `string` | Enter your caption.(ex: Universal Need)               | `YES`    |
| `hashtag`           | `string` | Enter your hashtag.(ex: drilling_rigs, oil_rigs)      | `NO`     |
| `tagged_user_names` | `string` | Enter usernames.(ex: usernames1, usernames2)          | `NO`     |

- Story Photo Upload
```http
POST /actions/upload_story/{media_path}
```
| Parameter    | Type     | Description                                  | Required |
|:-------------|:---------|:---------------------------------------------|:---------|
| `media_path` | `string` | Enter path of your photos.(ex: my_photo.jpg) | `YES`    |


## Conclusion
Thank you for exploring our API documentation. Our API offers a range of powerful features to enhance your Instagram presence, including automated interactions like likes, comments, and follows, as well as targeted hashtag engagement. By leveraging our API, you can boost your visibility, attract new followers, and share engaging content seamlessly through photo and story uploads. We hope this overview helps you understand how our API can support your Instagram goals effectively. If you have any questions or need assistance, please reach out to us.