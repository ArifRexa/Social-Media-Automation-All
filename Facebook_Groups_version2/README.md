
# Facebook Groups API
## Description
This repository contains a collection of programs designed to interact with Facebook groups through the Facebook Graph API. These programs offer various functionalities for discovering, accessing, and analyzing Facebook groups based on specific criteria such as keywords, country names, and group IDs.
## Tech Stack

- Python >= 3.10
- Selenium



## Features

- **Search by Keyword:** Find Facebook groups related to specific keywords.
- **Search by Country:** Discover groups based on both keyword and country name.
- **Retrieve Group Data:** Fetch essential information about groups including total members, new post count, and group URL.
- **User Authentication:** Check if a user is logged in and provide a logout API for session management.
- **Code Refactoring:** Code has been refactored for improved readability, efficiency, and testability.
- **Separation of ID:** Implemented functionality to extract IDs from group data, facilitating easier group identification.
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

### Now run in you terminal 
```bash
  uvicorn server:app --port 44777 --reload
```




## Usage/Examples
Go to 
```http
 http://127.0.0.1:44777
```
Other details and instructions are describe there
## Important Notice
- **Prioritize Login:** Always initiate the login process before accessing other functionalities to ensure authentication and enable full API access.
- **Minimize Function Calls:** Avoid excessive calls to API functions to prevent potential rate limits or other restrictions. Use the functions judiciously and only when necessary.
- **Optimize Login Frequency:** Reduce the frequency of login requests to minimize strain on our servers and maintain a smooth user experience.
- **Stay Informed:** Keep yourself updated with any changes or announcements regarding API usage guidelines to ensure compliance and optimal utilization of our services.
## API Reference

#### ⇒ All Actions
**You can see all actions from here**
```http
GET /actions/options
```
<br /><br />
#### ⇒ Authentication
- Check is logged in or not
```http
GET /check/authentication
```
<br />

- Login
```http
GET /action/login/{email}/{password}
```

| Parameter  | Type     | Description                   | Required |
|:-----------|:---------|:------------------------------|:---------|
| `email`    | `string` | Enter your facebook email.    | `YES`    |
| `password` | `string` | Enter your facebook password. | `YES`    |
 
<br />

- Logout
```http
GET /actions/logout
```
<br /><br />
#### ⇒ Group
- Find related groups by keyword.
```http
GET /actions/group/by/groups_name/{group_names}
```

| Parameter     | Type     | Description                                               | Required |
|:--------------|:---------|:----------------------------------------------------------|:---------|
| `group_names` | `string` | Enter groups name separated by comma. (ex, Food, Cricket) | `YES`    |

**Output will save on `data` directory and the output structure is: \
`group_id` | `group_name` | `Total_members` | `New_post_count` | `URL`**

<br /><br />

- Find related groups based on keyword and country.
```http
GET /actions/group/by/country/{group_names}/{country_names}
```

| Parameter       | Type     | Description                                                | Required |
|:----------------|:---------|:-----------------------------------------------------------|:---------|
| `group_names`   | `string` | Enter groups name separated by comma. (ex, Food, Cricket)  | `YES`    |
| `country_names` | `string` | Enter country name separated by comma. (ex, Canada, Nepal) | `YES`    |

**Output will save on `data` directory and the output structure is: \
`group_id` | `group_name` | `Total_members` | `New_post_count` | `URL`**


<br /><br />
- Separate the ID's (**⇒ Grab ID**)
```http
GET /actions/split/data/{file_name}
```
| Parameter   | Type     | Description                                                   | Required |
|:------------|:---------|:--------------------------------------------------------------|:---------|
| `file_name` | `string` | Enter file_name.(ex: groups_by_names_2024-02-14.15.42.54.txt) | `YES`    |

**Output will save on `data/split.txt` directory and the output example: \
`1892276491076222`\
`1708547722804840`\
`256618691596255`\
`336737143172000`**

<br /><br />
- Find group by group id.
**From collected groups data you should copy past the ID in `input.txt`. There should be more than 1 group ID in the file.**
```http
GET /actions/group/by/id
```
<br /><br />
- Perform action on group.
**You can like comment share on groups post. This is performing on `input.txt` file.**
```http
GET /actions/perform/action
```




## Conclusion
The Facebook Group Programs offer efficient tools for discovering and interacting with Facebook groups. With features for searching by keyword, country, and group ID, these programs streamline the process of accessing group data. Contributions are welcomed to enhance functionality further.\
**Thank you**.