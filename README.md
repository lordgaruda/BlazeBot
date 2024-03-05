# BlazeBot Guide

## Setup
1. Clone repo

```
git clone -b ptb https://github.com/ProjectBlaze/BlazeBot
```
2. Move to BlazeBot directory and setup virtual environment.

```
cd BlazeBot
sudo apt install python3-pip
pip install virtualenv
virtualenv venv
```

3. Start screen session

```
screen -S bot
```

3. To activate virtual environment

```
source venv/bin/activate
```
4. Install all required packages

```
pip install -r requirements.txt
```

5. Start bot

```
python blazebot.py
```

Now once bot has been started, use CTRL+A+D to leave screen session without stopping bot.

## Restart/Update
Update bot on your local machine then push the changes.
Considering you are outside screen session, 

1. Open screen session we created earlier

```
screen -Dr bot
```

2. Stop bot using CTRL+C

3. Pull the changes from github
```
git pull origin ptb
```

4. Start bot again
```
python blazebot.py
```

5. Detach from screen session using CTRL+A+D

## Secrets
This bot uses secrets.txt file saved in your user home directory, i.e. ```~/secrets.txt```.
Save your credentials in this file in following format.

WARNING : NEVER SHARE THIS FILE WITH ANYONE UNLESS YOU TRUST THEM.

```
BOT_TOKEN
SOURCE_FORGE_PASSWORD
CHAT_ID
```

Bot Token can be brought from Bot Father on Telegram.

Source forge password is required only if you want to use Upload feature of bot, only supported from GDrive to SourceForge. Write "None" if not required.

CHAT_ID helps you to restrict bot usage in perticular group. To get CHAT_ID of your group,
1. Add bot your group.
2. Make it admin.
3. Use command ```/chatid```

Then bot will reply with CHAT_ID.

## Contact me
You can contact me using following ways
- Email : ganesh314159@gmail.com
- Telegram : ganesh314159
- Instagram : ganesh314159
- Discord : Hououin-kyouma#1395

## THANK YOU