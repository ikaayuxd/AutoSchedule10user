import asyncio
import random
from telethon import events, functions, types
from xaayux.config import EMOJIS

async def react_to_message(event, client):
    if event.is_channel:
        try:
            emoji = random.choice(EMOJIS)
            await client(functions.messages.SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(emoticon=emoji)]
            ))
            print(f"Client reacted to message from {event.chat.title} with {emoji}")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Client Error: {e}")

def register(client):
    @client.on(events.NewMessage())
    async def handler(event):
        await react_to_message(event, client)

async def setup(clients):
    for i, client in enumerate(clients):
        try:
            register(client)
            print(f"Reaction handler registered for client {i+1}")
        except Exception as e:
            print(f"Failed to register reaction handler for client {i+1}: {e}")
xaayux/plugins/bot_control.py
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
