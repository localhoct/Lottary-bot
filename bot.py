# -*- coding: utf-8 -*-

import requests
import random
import validators
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from instabot import Bot


api_id = 123456789 #int of api id get from my.telegram.org
api_hash = " Your Api Hash Here " #str of api hash get from my.telegram.org
token = ' Your Bot Token here ' #str of token get from BotFather
app = Client("Downlaoder", api_id, api_hash, token)


@app.on_message(filters.command('start', '/') & filters.private)
async def start(c, m):
    await m.reply_text('[اینجا بزن](tg://user?id=1404201443))

# Group Member
@app.on_message(filters.command('lt', '/') & filters.group)
async def get_member(c, m):
    chat_title = m.chat.title
    # Get All Chat Member and Save to File
    with open(chat_title+'.txt', 'w', encoding='UTF-8') as f:
        async for member in m.chat.iter_members():
            writes = f'{member.user.first_name},{member.user.id}\n'
            f.write(writes)
    # Read Chat Member File
    with open(chat_title+'.txt', 'r', encoding='UTF-8') as f:
        list_of_member = f.readlines()  # Read lines
        select_member = random.choice(list_of_member)  # Select random member
        chatid_fname = select_member.replace('\n', '')
        fname, chat_id = chatid_fname.split(',')
        await m.reply_text(f'Winner:\n[{fname}](tg://user?id={chat_id})', parse_mode='markdown')

# Instagram Comments
def get_comments(link):
    bot = Bot()
    # bot.login(username='Usr', password='pasw')
    media_id = bot.get_media_id_from_link(link)
    comments = bot.get_media_comments_all(media_id)
    for i in range(0, len(comments)):
        with open('comments.txt', 'w', encoding='UTF-8') as f:
            username = (comments[i]["user"]['username'])
            text = (comments[i]['text'])
            line = f"{username},{text}\n"
            f.write(line)
    with open('comments.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    return lines


@app.on_message(filters.command('cmts', '/') & filters.group)
async def comments(c, m):
    link = m.text.replace('/cmts ', '')
    if validators.url(link):
        msg = await m.reply_text('Leech Comments...')
        lines = get_comments(link)
        await msg.edit_text('Reading users :) ')
        select_member = random.choice(lines)  # Select random member
        chatid_fname = select_member.replace('\n', '')
        fname, chat_id = chatid_fname.split(',')
        asyncio.sleep(4)
        await msg.edit_text(f'Maybe This User? [{fname}](https://instagram.com/{fname})\n NOOOOOO You Wrong :))')
        select_member = random.choice(lines)  # Select random member
        asyncio.sleep(4)
        await msg.edit_text('I selected what do you think? :) ')
        select_member = random.choice(lines)  # Select random member
        asyncio.sleep(4)
        chatid_fname = select_member.replace('\n', '')
        fname, chat_id = chatid_fname.split(',')
        await msg.edit_text(f'**Winner** : [{fname}](https://instagram.com/{fname})\n**text of comment** : {chat_id}', parse_mode='markdown')
    else:
        await m.reply_text("Please Send valid Link :)")


app.run()
