from telethon import TelegramClient, events
from asyncio import sleep
import random

from telethon.errors.rpcerrorlist import MsgIdInvalidError

with open('acc.json') as user_file:
    file_contents = user_file.read()
    data = eval(file_contents)


api_id = data['api_id']
api_hash = data['api_hash']
session_name = data['name']

proxy = {
    'proxy_type': 'SOCKS5', # (mandatory) protocol to use (see above)
    'addr': '68.183.25.31',      # (mandatory) proxy IP address
    'port': 59166,           # (mandatory) proxy port number
}

client = TelegramClient(session_name, api_id, api_hash)
client.start()

random_greeting = lambda: f"{random.choice(['Обычная ситуация','Жесть','Как обычно','Круто'])} "

parse_chats = []

res = client.iter_dialogs()
for e in res:
    if len(str(e.id)) > 8:
        parse_chats.append(e.id)


print('Скрипт запущен ожидает новых постов.')

@client.on(events.NewMessage(chats=parse_chats))
async def my_event_handler(event):
    try:
        if event.grouped_id == None:
            if event.message:
                print(f'New post')
                await sleep(random.randint(7, 15))
                print(f'CHash Bydet')
                await event.respond(random_greeting(), comment_to=event.id)


    except MsgIdInvalidError:
        print(MsgIdInvalidError)

    except Exception as s:
        print("[!] Error:", s)



@client.on(events.Album(chats=parse_chats))
async def handler(event):
    try:
        if event.message:
            print(f'New post')
            await sleep(random.randint(7, 15))
            print(f'CHash Bydet')
            await event.respond(random_greeting(), comment_to=event.id)


    except MsgIdInvalidError:
        print(MsgIdInvalidError)

    except Exception as s:
        print("[!] Error:", s)


client.run_until_disconnected()

