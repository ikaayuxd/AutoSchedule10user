import re
from .. import client
from telethon import events
from telethon.tl import types 
import logging 
import asyncio
import time
from telethon.tl.functions.messages import EditMessageRequest
from xaayux.config import DELAY, channel_ids 
import asyncio
from telethon import TelegramClient, events, types
from telethon.tl.functions.messages import SendReactionRequest

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -- Constants -- #
@client.on(events.NewMessage)
async def reaction_handler(event):
    chat = await event.get_chat()
    message_id = event.id
    await client(SendReactionRequest(
        peer=chat,
        msg_id=message_id,
        reaction=[types.ReactionEmoji(
            emoticon='❤️'
        )]
    ))
