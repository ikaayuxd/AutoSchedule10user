import re
from .. import client
from telethon import events, types, Button
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
        new_buttons = []
        if event.reply_markup:
            for row in event.reply_markup.rows:
                new_row = []
                for button in row.buttons:
                    if isinstance(button, types.KeyboardButtonUrl):
                        # Change the URL of the button
                        new_button = types.KeyboardButtonUrl(button.text, url='https://t.me/+s7zlIpl9NfZhMWFl')
                        new_row.append(new_button)
                    else:
                        new_row.append(button)
                new_buttons.append(new_row)

            # Create a copy of the original reply markup with updated buttons
            updated_reply_markup = types.ReplyInlineMarkup(new_buttons)

        # Add the URL at the end of the message
        updated_message = f"{event.message.message}\n\n[Click here to visit](https://t.me/+s7zlIpl9NfZhMWFl)"

        await event.client.send_message(event.chat_id, str(updated_message), reply_to=event.reply_to_msg_id,
                                        buttons=updated_reply_markup if event.reply_markup else None)

        await event.delete()
    except Exception as e:
        print(f"An error occurred: {e}")
  
@client.on(events.NewMessage(outgoing=True, pattern='LegendxTricks'))
async def alive(event):
    txt = await event.edit("『𝗟𝗲𝗴𝗲𝗻𝗱 × 𝗧𝗿𝗶𝗰𝗸𝘀』")
    time.sleep(3)
    await event.edit("• ᴅᴀɪʟʏ ɴᴇᴡ ᴍᴇᴛʜᴏᴅꜱ ᴜᴘᴅᴀᴛᴇ")
    time.sleep(3)
    await event.edit("• ʜɪɢʜ Qᴜᴀʟɪᴛʏ ᴍᴇᴛʜᴏᴅꜱ")
    time.sleep(3)
    await event.edit("• ᴘᴀɪᴅ ᴍᴇᴛʜᴏᴅꜱ ꜰᴏʀ ꜰʀᴇᴇ")
    time.sleep(3)
    await event.edit("• ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴꜱ ᴍᴇᴛʜᴏᴅꜱ")
    time.sleep(3)
    await event.edit("• ʙᴀɴ/ᴜɴʙᴀɴ ᴍᴇᴛʜᴏᴅꜱ")
    time.sleep(3)
    await event.edit("• ᴄᴏᴜʀꜱᴇꜱ, ᴍᴏᴅꜱ, ᴠɪʀᴜꜱᴇꜱ")
    time.sleep(3)
    await event.edit("• ʀᴀᴛꜱ /ꜱᴄʀɪᴘᴛꜱ")
    time.sleep(3)
    await event.edit("• ʀᴇғᴜɴᴅɪɴɢ / ʙʏᴘᴀssɪɴɢ")
    time.sleep(3)
    await event.edit("• ꜱᴇᴄʀᴇᴛ ᴛʀɪᴄᴋꜱ")
    time.sleep(3)
    await event.edit("• ꜱᴛᴜᴅʏ ᴍᴀᴛᴇʀɪᴀʟꜱ")
    time.sleep(3)
    await event.edit("• ᴅᴀʀᴋ ᴡᴇʙ ᴅᴇᴇᴘ ᴡᴇʙ")
    time.sleep(3)
    await event.edit("• ʙᴏᴍʙᴇʀ ᴀᴘᴘꜱ ᴀɴᴅ ᴡᴇʙ")
    time.sleep(3)  
    await event.edit("• ᴛɢ ᴜꜱᴇꜰᴜʟ ʙᴏᴛꜱ")
    time.sleep(3)
    await event.edit("• ᴄᴀʀᴅɪɴɢ / ʙɪɴɴɪɴɢ / ʙᴀɴɴɪɴɢ")
    time.sleep(3)
    await event.edit("• ꜱᴄʀᴀᴘᴘɪɴɢ / ᴊᴀᴄᴋɪɴɢ")
    time.sleep(3)
    await event.edit("• ʟᴏɢᴏ ᴍᴀᴋɪɴɢ")
    time.sleep(3)
    await event.edit("• ɪɢ ᴄᴄ")
    time.sleep(3)
    await event.edit("• ᴍᴏʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ")
    time.sleep(3)
    await event.edit("• ᴛᴏᴏʟꜱ / ʙᴜɢ ʜᴜɴᴛɪɴɢ")
    time.sleep(3)
    await event.edit("• ʀᴅᴘ / ᴋᴀʟɪ ʟɪɴᴜx")
    time.sleep(3)
    await event.edit("• ʜᴇʀᴏᴋᴜ ᴄᴄ")
    time.sleep(3)
    await event.edit("• ᴀᴅᴠᴀɴᴄᴇᴅ ʙᴜʀᴘꜱᴜɪᴛᴇ")
    time.sleep(3)
    await event.edit("• ᴇᴅᴜ ᴍᴀɪʟ / ᴏᴛᴘ ʙᴏᴛ")
    time.sleep(3)
    await event.edit("• ᴄᴄ ᴛᴏ ʙᴛᴄ / ᴄᴄ ᴛᴏ ᴜᴘɪ")
    time.sleep(3)
    await event.edit("• ᴡᴇʙ ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ")
    time.sleep(3)
    await event.edit("• ꜱQʟ ɪɴᴊᴇᴄᴛɪᴏɴ / ꜱᴍᴍ ᴘᴀɴᴇʟ")
    time.sleep(3)
    await event.edit(f"✘ 𝐇𝐞𝐫𝐞 𝐖𝐞 𝐇𝐚𝐯𝐞 𝐄𝐯𝐞𝐫𝐲𝐭𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐘𝐨𝐮\n\n𝗣ʀᴇᴍɪᴜᴍ 𝗔ɴᴅ 𝗣ᴀɪᴅ 𝗖ᴏɴᴛᴇɴᴛ 𝗔ʙ𝘀ᴏʟᴜᴛᴇʟʏ 𝗙ʀᴇᴇ")
          
