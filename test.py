import time
import requests

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import ConnectionManager


TOKEN = '1222858951:AAHeVtfjJodsUS_Pg4yybK3fAzRtkRqo_Go'

knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts
userInfo = {'username' : '',
            'request'    : '',
            'location'   : ''}


commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot',
    'help'        : 'Gives you information about the available commands',
    'ask'         : 'Type in your request',
    'pending'     : 'Check all your pending requests'
    # 'done'        : 'See all completed requests'
}


# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.username) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hello, stranger, you look good today")
        bot.send_message(cid, "How can I help you? Please join our main channel for updates!\nhttps://t.me/joinchat/AAAAAFMxZPdTUyqLDH6mGw")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "I already know you, no need for me to know you again!")


# handle the "/done" command
# @bot.message_handler(commands=['done'])
# def command_requests(m):
#     cid = m.chat.id
#     username = "@" + m.chat.username
#     command_pending(m)
#     bot.send_message(cid, output)


# handle the "/pending" command
@bot.message_handler(commands=['pending'])
def command_pending(m):
    cid = m.chat.id
    username = "@" + m.chat.username
    search_arr = ConnectionManager.search(username)

    # print(search_arr)
    output = 'PENDING Requests:\n'

    if len(search_arr) == 0:
        output += "NO MORE PENDING REQUESTS"
    else:
        for array in search_arr:
            msg = ''
            request_id = array[0]
            request = array[2]
            location = array[3]
            status = array[4]
            # msg = "\nRequest Number: " + str(request_id) + "\nRequest: " + str(request) + "\nLocation: " + str(location)
            if not status:
                msg = "\nRequest Number: " + str(request_id) + "\nRequest: " + str(request) + "\nLocation: " + str(location)
                msg += "\nStatus: PENDING\n"
            output += "============================================\n" + msg 

    output += "============================================\n" + "\nTo make a request, /ask and get more /help here"

    bot.send_message(cid, output)


# handle the "/ask" command
@bot.message_handler(commands=['ask'])
def command_ask(m):
    msg = bot.reply_to(m, 'Please enter your request!')
    userInfo['username'] = "@" + str(m.chat.username)
    # cid will later be used to store things
    bot.register_next_step_handler(msg, process_request)


def process_request(m):
    request = m.text
    userInfo['request'] = request
    # cid will later be used to store things
    answer = bot.reply_to(m, "Where is your location?")
    bot.register_next_step_handler(answer, process_location)


def process_location(m):
    cid = m.chat.id
    location = m.text
    userInfo['location'] = location
    msg = "Request ID: " + userInfo['username'] + "\nRequest: " + userInfo['request'] + "\nLocation: " + userInfo['location'] 
    bot.send_message(cid, 'Thank you for your request! Here are the details of your request:\n' + msg 
    + "\nPlease join our main channel for updates!\nhttps://t.me/joinchat/AAAAAFMxZPdTUyqLDH6mGw")
    insert_database(userInfo)
    send_to_channel(userInfo)


def insert_database(userInfo):
    username = userInfo['username']
    request = userInfo['request']
    location = userInfo['location']
    ConnectionManager.create(username, request, location)


def send_to_channel(m):
    username = m['username']
    request = m['request']
    location = m['location']
    msg = 'Username: ' + str(username) + '\nPerson in need looking for kind person to '  + str(request) +'\nLocation: ' + location
    bot.send_message('@CovidReliefchannel', msg, reply_markup=gen_markup())


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton(text="I can help!", url="http://t.me/wxcovidBOT"))
    return markup


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page


# filter on a specific message
@bot.message_handler(func=lambda message: message.text == "hi")
def command_text_hi(m):
    bot.send_message(m.chat.id, "I love you too!")


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help")


bot.polling()