
# WhatsApp Bot API
## Description
The WhatsApp Bot is a Python script designed to automate interactions with WhatsApp's web interface using Selenium WebDriver. This bot provides functionality for various tasks such as retrieving the number of participants in a group, obtaining contact information of group members and joining groups via invitation links.
## Tech Stack

- Python 3.10
- Selenium WebDriver
- Browser WebDriver (e.g., Chrome WebDriver)
- Other libraries as specified in the requirements.txt file



## Features

- **Number of Participants:** Retrieve the number of participants in a WhatsApp group.
- **Group Members Information:** Obtain contact information (e.g., phone numbers) of members in a WhatsApp group.
- **Join Group by Link:** Automatically join a WhatsApp group by clicking on an invitation link.
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

#### ⇒ Home
**You can see all actions from here**
```http
GET /home
```

<br />


#### ⇒ Group
- You can join a group by groups invitation link.
```http
GET /action/join/group/{link}
```
| Parameter | Type     | Description                                                           | Required |
|:----------|:---------|:----------------------------------------------------------------------|:---------|
| `link`    | `string` | Enter the link.(ex: https://chat.whatsapp.com/4fy62abhcGb9tmmVP3AQtI) | `YES`    |


<br />

- You can find the total number of group members.
```http
GET /actions/group/number_of_members/{group_name}
```
| Parameter    | Type     | Description                                 | Required |
|:-------------|:---------|:--------------------------------------------|:---------|
| `group_name` | `string` | Enter the name of group.(ex: My Test Group) | `YES`    |

**Output data will be saved on `Collected_data/number_of_group_members/group_members.csv`.**

<br />

- You can find the total number of group members.
```http
GET /actions/group/contact/number_of_members/{group_name}
```
| Parameter    | Type     | Description                                 | Required |
|:-------------|:---------|:--------------------------------------------|:---------|
| `group_name` | `string` | Enter the name of group.(ex: My Test Group) | `YES`    |

**Output data will be saved on `Collected_data/contact_info_data/` in a csv file.**


## Conclusion
The WhatsApp Bot simplifies WhatsApp interactions through automation, offering features like retrieving the number of participants in a group, obtaining contact information of group members, joining groups via invitation links. Use it responsibly and in compliance with WhatsApp's terms. Enhance productivity and enjoy a smoother WhatsApp experience with this versatile tool.

**Thank you**.