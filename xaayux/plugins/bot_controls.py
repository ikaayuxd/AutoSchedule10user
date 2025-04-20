import asyncio
from telethon import events, TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sessions import StringSession
from xaayux.config import ADMIN_ID, BOT_TOKEN, API_ID, API_HASH

bot_session = StringSession()
bot_client = TelegramClient(bot_session, api_id=API_ID, api_hash=API_HASH)

async def start_bot(clients):
    await bot_client.start(bot_token=BOT_TOKEN)
    print("Bot client started")

    @bot_client.on(events.NewMessage(from_users=ADMIN_ID, pattern=r'^/join (.+)'))
    async def join_handler(event):
        channel = event.pattern_match.group(1)
        for i, client in enumerate(clients):
            try:
                await client(JoinChannelRequest(channel))
                print(f"Client {i+1} joined channel {channel}")
            except Exception as e:
                print(f"Client {i+1} failed to join channel {channel}: {e}")
        await event.reply(f"All clients instructed to join {channel}")

    @bot_client.on(events.NewMessage(from_users=ADMIN_ID, pattern=r'^/leave (.+)'))
    async def leave_handler(event):
        channel = event.pattern_match.group(1)
        for i, client in enumerate(clients):
            try:
                await client(LeaveChannelRequest(channel))
                print(f"Client {i+1} left channel {channel}")
            except Exception as e:
                print(f"Client {i+1} failed to leave channel {channel}: {e}")
        await event.reply(f"All clients instructed to leave {channel}")

    await bot_client.run_until_disconnected()
