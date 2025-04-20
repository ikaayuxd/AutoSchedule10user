import asyncio
from telethon import events, TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from xaayux.config import ADMIN_ID, BOT_TOKEN

bot_client = TelegramClient('bot_session', api_id=0, api_hash='', bot_token=BOT_TOKEN)

async def join_channel_all(clients, channel):
    for i, client in enumerate(clients):
        try:
            await client(JoinChannelRequest(channel))
            print(f"Client {i+1} joined channel {channel}")
        except Exception as e:
            print(f"Client {i+1} failed to join channel {channel}: {e}")

async def leave_channel_all(clients, channel):
    for i, client in enumerate(clients):
        try:
            await client(LeaveChannelRequest(channel))
            print(f"Client {i+1} left channel {channel}")
        except Exception as e:
            print(f"Client {i+1} failed to leave channel {channel}: {e}")

def register_bot_commands(clients):
    @bot_client.on(events.NewMessage(from_users=ADMIN_ID, pattern=r'^/join (.+)'))
    async def join_handler(event):
        channel = event.pattern_match.group(1)
        await join_channel_all(clients, channel)
        await event.reply(f"All clients instructed to join {channel}")

    @bot_client.on(events.NewMessage(from_users=ADMIN_ID, pattern=r'^/leave (.+)'))
    async def leave_handler(event):
        channel = event.pattern_match.group(1)
        await leave_channel_all(clients, channel)
        await event.reply(f"All clients instructed to leave {channel}")

async def start_bot(clients):
    register_bot_commands(clients)
    await bot_client.start()
    print("Bot client started")
    await bot_client.run_until_disconnected()
