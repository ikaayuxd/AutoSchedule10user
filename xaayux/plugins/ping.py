

from .. import client
from telethon import events
import logging 
import asyncio
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -- Constants -- #
HELP = """𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀
`!start` - **Start Auto Scheduler **
`!cancel` - **Stop Auto Scheduler** 
`!alive` - **Check If Bot Is Alive**
`!about` - **About The Bot **
`!help` - **Help Message**
"""

ABOUT_TXT = """
᪥ **Name:** 𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗕𝘆 @xAaYux • @LegendxTricks
᪥ **Library: [Telethon](https://docs.telethon.dev/)**
᪥ **Language: [Python 3](https://www.python.org)**
᪥ **Dev:** [⏤‌ＫＡＲＴＩＫ𓆩♡𓆪™|🇮🇳](https://t.me/xAaYux)
"""

@client.on(events.NewMessage(outgoing=True, pattern='!about'))
async def about(event):
    await event.edit(ABOUT_TXT, link_preview=False)


@client.on(events.NewMessage(outgoing=True, pattern='!help'))
async def help_me(event):
    await event.edit(HELP)


@client.on(events.NewMessage(outgoing=True, pattern='!alive'))
async def alive(event):
    txt = await event.edit("▢▢▢▢▢▢")
          await event.edit("▣▢▢▢▢▢")
          await event.edit("▣▣▢▢▢▢")
          await event.edit("▣▣▣▢▢▢")
          await event.edit("▣▣▣▣▢▢")
          await event.edit("▣▣▣▣▣▢")
          await event.edit("▣▣▣▣▣▣")
          await event.edit("𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗜𝘀 𝗔𝗰𝘁𝗶𝘃𝗲 𝗔𝗻𝗱 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗦𝗲𝗻𝗱𝗶𝗻𝗴 𝗔𝗻𝗱 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗶𝗻𝗴 𝗗𝗲𝗮𝗹𝘆 𝗜𝘀 𝗦𝗲𝘁 𝗧𝗼 {DELAY}(𝗦𝗲𝗰𝗼𝗻𝗱)")
