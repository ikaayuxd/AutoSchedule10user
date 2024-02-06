from .. import client, TIME
from telethon import events, types
import logging 
import asyncio
import random

channel_ids = [-1002095710352, -1002052982599, -1002048287965, -1001998377282, -1001992984787, -1001624878815, -1001943016652, -1002139659491]  # Replace with your channel IDs

messages = [
    f"𝗛𝗔𝗖𝗞 𝗬𝗢𝗨𝗥 𝗦𝗖𝗛𝗢𝗢𝗜/𝗖𝗢𝗜𝗜𝗘𝗚𝗘 𝗪𝗘𝗕𝗦𝗜𝗧𝗘 ⬇️\n\n𝗜𝗜𝗡𝗞: [@WebHacking56](https://t.me/+hDX1CM9vk5U5MDI9)\n\n𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗙𝗢𝗜𝗗𝗘𝗥 𝗘𝗡𝗧𝗥𝗬 ⬇️\n\n𝗜𝗜𝗡𝗞: [@PaidFolder68](https://t.me/addlist/3pwjeI2RyiMzYWE9)", 
    f"𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗖𝗛𝗔𝗡𝗡𝗘𝗜 𝗘𝗡𝗧𝗥𝗬 ⬇️\n\n𝗜𝗜𝗡𝗞: [@LegendxTricks](https://t.me/+98qlvU9in_xlODZl)\n\n𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗙𝗢𝗜𝗗𝗘𝗥 𝗘𝗡𝗧𝗥𝗬 ⬇️\n\n𝗜𝗜𝗡𝗞: [@PaidFolder68](https://t.me/addlist/3pwjeI2RyiMzYWE9)"
]  # Add your desired message links here

async def send_messages():
    while True:
        for channel_id in channel_ids:
            message = random.choice(messages)
            await client.send_message(channel_id, message)
            await asyncio.sleep(10)  # Send a message every 1 minute

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
