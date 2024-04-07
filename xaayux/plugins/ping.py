import re
from .. import client
from telethon import events, types
import logging 
import asyncio
import time
from telethon.tl.functions.messages import EditMessageRequest
from xaayux.config import DELAY, channel_ids 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -- Constants -- #
HELP = """
𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀
!start - Start Auto Scheduler 
!cancel - Stop Auto Scheduler 
!alive - Check If Bot Is Alive
!about - About The Bot 
!help - Help Message
"""

ABOUT = """
᪥ Name: 𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗕𝘆 @xAaYux • @LegendxTricks
᪥ Library: [Telethon](https://docs.telethon.dev/)
᪥ Language: Python 3 
᪥ Dev: [⏤‌ＫＡＲＴＩＫ𓆩♡𓆪™|🇮🇳](https://t.me/xAaYux)
"""

  
@client.on(events.NewMessage(outgoing=True, pattern='!about'))
async def about(event):
    await event.edit(ABOUT, link_preview=False)
  

@client.on(events.NewMessage(outgoing=True, pattern='!hii'))
async def get_group_id(event):
        # Get the group ID
        group_id = event.chat_id
        # Save the group ID to saved messages
        await client.send_message('me', f'Saved Group ID:`{group_id}`')

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
    
    await event.edit(f"𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗜𝘀 𝗔𝗰𝘁𝗶𝘃𝗲.\n\n𝗗𝗲𝗮𝗹𝘆 𝗜𝘀 𝗦𝗲𝘁 𝗧𝗼 {DELAY}(𝗦𝗲𝗰𝗼𝗻𝗱𝘀). \n\n @LegendxTricks")



@client.on(events.NewMessage(chats=channel_ids))
async def fwdrmv(event):
    try:
        if event.media and not (event.video_note or event.sticker):
            new_buttons = []
            for row in event.reply_markup.rows:
                new_row = []
                for button in row.buttons:
                    if isinstance(button, types.KeyboardButtonUrl):
                        new_button = types.KeyboardButtonUrl(button.text, url='https://t.me/+s7zlIpl9NfZhMWFl')
                        new_row.append(new_button)
                    else:
                        new_row.append(button)
                new_buttons.append(new_row)

            await event.client.send_message(event.chat_id, event.message, reply_to=event.reply_to_msg_id,
                                            buttons=new_buttons)
            await event.delete()
        else:
            await event.client.send_message(event.chat_id, event.message)
            await event.delete()
    except Exception as e:
        print(f"An error occurred: {e}")


@client.on(events.NewMessage(pattern='/LegendxTricks'))
async def start(event):
    # Send the initial message with the animation
    await event.respond('🥀 𝐖𝐞𝐥𝐜𝐨𝐦𝐞,\n[✘] 𝐇𝐞𝐫𝐞 𝐖𝐞 𝐇𝐚𝐯𝐞 𝐄𝐯𝐞𝐫𝐲𝐭𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐘𝐨𝐮')
    
    # Define your animation frames using emojis, text, and symbols
    frames = [
        "『𝗟𝗲𝗴𝗲𝗻𝗱 × 𝗧𝗿𝗶𝗰𝗸𝘀』",
"×ꜱᴘᴇᴄɪᴀʟ sᴛᴜғғs ɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ×",
"• ᴅᴀɪʟʏ ɴᴇᴡ ᴍᴇᴛʜᴏᴅꜱ ᴜᴘᴅᴀᴛᴇ,",
"• ʜɪɢʜ Qᴜᴀʟɪᴛʏ ᴍᴇᴛʜᴏᴅꜱ,",
"• ᴘᴀɪᴅ ᴍᴇᴛʜᴏᴅꜱ ꜰᴏʀ ꜰʀᴇᴇ,",
"• ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴꜱ ᴍᴇᴛʜᴏᴅꜱ,",
"• ʙᴀɴ/ᴜɴʙᴀɴ ᴍᴇᴛʜᴏᴅꜱ,",
"• ᴄᴏᴜʀꜱᴇꜱ, ᴍᴏᴅꜱ, ᴠɪʀᴜꜱᴇꜱ,",
"• ʀᴀᴛꜱ /ꜱᴄʀɪᴘᴛꜱ,",
"• ʀᴇғᴜɴᴅɪɴɢ / ʙʏᴘᴀssɪɴɢ,",
"• ꜱᴇᴄʀᴇᴛ ᴛʀɪᴄᴋꜱ,",
"• ꜱᴛᴜᴅʏ ᴍᴀᴛᴇʀɪᴀʟꜱ,",
"• ᴅᴀʀᴋ ᴡᴇʙ ᴅᴇᴇᴘ ᴡᴇʙ,",
"• ʙᴏᴍʙᴇʀ ᴀᴘᴘꜱ ᴀɴᴅ ᴡᴇʙ,",
"• ᴛɢ ᴜꜱᴇꜰᴜʟ ʙᴏᴛꜱ,",
"• ᴄᴀʀᴅɪɴɢ / ʙɪɴɴɪɴɢ / ʙᴀɴɴɪɴɢ ,",
"• ꜱᴄʀᴀᴘᴘɪɴɢ / ᴊᴀᴄᴋɪɴɢ,",
"• ʟᴏɢᴏ ᴍᴀᴋɪɴɢ,",
"• ɪɢ ᴄᴄ,",
"• ᴍᴏʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ,",
"• ᴛᴏᴏʟꜱ / ʙᴜɢ ʜᴜɴᴛɪɴɢ ,",
"• ʀᴅᴘ / ᴋᴀʟɪ ʟɪɴᴜx ,",
"• ʜᴇʀᴏᴋᴜ ᴄᴄ ,",
"• ᴀᴅᴠᴀɴᴄᴇᴅ ʙᴜʀᴘꜱᴜɪᴛᴇ ,",
"• ᴇᴅᴜ ᴍᴀɪʟ / ᴏᴛᴘ ʙᴏᴛ ,",
"• ᴄᴄ ᴛᴏ ʙᴛᴄ / ᴄᴄ ᴛᴏ ᴜᴘɪ ,",
"• ᴡᴇʙ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ ,",
"• ꜱQʟ ɪɴᴊᴇᴄᴛɪᴏɴ / ꜱᴍᴍ ᴘᴀɴᴇʟ"
    ]
    
    while True:
        for frame in frames:
            # Edit the message with the current frame of the animation
            await event.respond(frame)
            
            # Sleep for a short duration to control the speed of the animation
            await asyncio.sleep(0.1)
