from .. import client, DELAY
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import InputPeerChannel
from telethon import events, types
import logging 
import asyncio
import random
from xaayux.config import channel_ids, messages, DELAY, group_ids

message_text = ("𝗣𝗥𝗜𝗠𝗘 𝗩𝗜𝗗𝗘𝗢 6𝗠𝗢𝗡𝗧𝗛 𝗠𝗘𝗧𝗛𝗢𝗗 𝗙𝗢𝗥 𝗦𝗔𝗜𝗘\n\𝗜𝗡𝗗𝗜𝗔𝗡 𝗜𝗣 𝗔𝗡𝗗 𝗨𝗦 𝗜𝗣 𝗕𝗢𝗧𝗛 𝗠𝗘𝗧𝗛𝗢𝗗 𝗔𝗩𝗔𝗜𝗜𝗔𝗕𝗜𝗘 𝗔𝗡𝗗 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 ,\n\n𝗣𝗥𝗜𝗖𝗘 100𝗥𝗦 \n\n𝗗𝗠 @xAaYux")
async def send_messages():
    while True:
        for chat in chats:
        if isinstance(chat.entity, InputPeerChannel):
            try:
                # Send the message to the group
                client(SendMessageRequest(chat, message_text))
                print(f"Message sent to {chat.title}")
            except Exception as e:
                print(f"Failed to send message to {chat.title}: {e}")
                
@client.on(events.NewMessage(outgoing=True, pattern='!cancel'))
async def handle_cancel(event):
    await event.respond('Cancelling Auto Message Forwarding...')
    global send_task
    send_task.cancel()

@client.on(events.NewMessage(outgoing=True, pattern='!start'))
async def handle_start(event):
    await event.respond("Starting Auto Message Forwarding...")
    global send_task
    send_task = asyncio.create_task(send_messages())

logging.basicConfig(level=logging.WARNING)

with client:
    client.run_until_disconnected()
