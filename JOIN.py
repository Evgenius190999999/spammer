from telethon.sync import TelegramClient
from asyncio import sleep
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest


with open('acc.json') as user_file:
    file_contents = user_file.read()
    data = eval(file_contents)


api_id = data['api_id']
api_hash = data['api_hash']
session_name = data['name']
phone = '+6285654079208'


proxy = {
    'proxy_type': 'SOCKS5',
    'addr': '68.183.25.31',
    'port': 59166,
}

client = TelegramClient(session_name, api_id, api_hash)
client.start()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

async def changeProfil():
    print('Сейчас будет изменен профиль.')
    await client(UpdateProfileRequest(
        first_name='ТВОЯ ЗАЙКА',
        about='Я тут: https://t.me/+IaXxsYgtHRA3NmVi'
    ))
    await sleep(10)

    # print('Сейчас будет изменена фотография профиля.')
    # await client(UploadProfilePhotoRequest(
    #     await client.upload_file(file='1.jpg')
    # ))

parse_chats = ['https://t.me/chrtnv', 'https://t.me/igmtv', 'https://t.me/syriantube', 'https://t.me/football_nik', 'IeY034H9tp45N2Ey', 'MuW9WJePRF5lMzYy']

async def main():
    await changeProfil()
    for i in parse_chats:
        if 't.me/' in i:
            entity = await client.get_entity(i)
            await client(JoinChannelRequest(channel=entity.id))
            print(f'Подписался на {entity.title}')
            await sleep(10)
        else:
            await client(ImportChatInviteRequest(i))



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
