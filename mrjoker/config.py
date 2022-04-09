# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID= 6235351 # integer value, dont use ""
    API_HASH= "f68fde1378da8f85a243f2ae57f2fcf9"
    TOKEN = "5139344076:AAGe8KZzAxgWr8PHVN6tGfK3nrMAiTytHkg"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1601406864   # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Your_ddy"
    SUPPORT_CHAT = "Mr_Jokr_support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001235511467
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001235511467
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://ncfjrkbfwqsqqy:0eebbc75d1e7e70a55622a129b49dafafa906eeff5e0ab59feee9f01126f1edf@ec2-3-230-122-20.compute-1.amazonaws.com:5432/d98horqj63h7ai"  
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "yfJmdR0rNj1MclUWjiTblobi3QRynjNBqQEjNn~nb3kQY6hvmQbgoH4O0encL1QA"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1601406864"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1601406864"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1601406864"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1601406864"
    WOLVES = "1601406864"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "Y0L02LBR4WLNIK5W"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "6DEOJMP7M03L"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "xyz"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "xyz"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    YOUTUBE_API_KEY=""
    INFOPIC =""
    TEMP_DOWNLOAD_DIRECTORY = "./"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

