import re
from .. import client
from telethon import events
import logging 
import asyncio
import time
from xaayux.config import DELAY
from sympy import symbols, Eq, solve

# Variable to track if the code assistant is active or not
code_assistant_active = False

@client.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    
    global code_assistant_active
    
    # Check if the message is 'helloc'
    if message.text.lower() == 'helloc':
        code_assistant_active = True
        await client.send_message(message.chat_id, "Code assistant started. How can I assist you?")
    
    # Check if the message contains an equation and the code assistant is active
    elif code_assistant_active and any(char.isdigit() for char in message.text) and any(char in '+-×÷' for char in message.text):
        try:
            # Replace '×' with '*' and '÷' with '/'
            equation_text = message.text.replace('×', '*').replace('÷', '/')
            
            # Split the equation into left-hand side and right-hand side
            equation_parts = equation_text.split('=')
            lhs = equation_parts[0].strip()
            rhs = equation_parts[1].strip()

            # Create symbols for variables used in the equation
            variables = set()
            for char in lhs + rhs:
                if char.isalpha():
                    variables.add(char)
            
            # Create symbolic equations using sympy
            sym_eq = Eq(eval(lhs), eval(rhs))
            
            # Solve the equations to find variable values
            solutions = solve(sym_eq, variables)

            result = ""
            
            # Format and send the results
            for var, val in solutions.items():
                result += f"{var} = {val}\n"
            
            await client.send_message(message.chat_id, result)
        
        except Exception as e:
            await client.send_message(message.chat_id, str(e))
    
    # Check if the message is 'hellos'
    elif message.text.lower() == 'hellos':
        code_assistant_active = False
        await client.send_message(message.chat_id, "Code assistant stopped. Goodbye!")

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

ABOUT_TXT = """
᪥ Name: 𝗔𝘂𝘁𝗼 𝗦𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗿 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𝗕𝘆 @xAaYux • @LegendxTricks
᪥ Library: [Telethon](https://docs.telethon.dev/)
᪥ Language: Python 3 
᪥ Dev: [⏤‌ＫＡＲＴＩＫ𓆩♡𓆪™|🇮🇳](https://t.me/xAaYux)
"""



    
    
@client.on(events.NewMessage(pattern='^@LegendxTricks$'))
async def get_group_id(event):
    # Get the group ID
    group_id = event.chat_id
    
    # Save the group ID to saved messages
    await client.send_message('me', f'Saved Group ID:`{group_id}`')
      
@client.on(events.NewMessage(outgoing=True, pattern='!about'))
async def about(event):
    await event.edit(q, link_preview=False)


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
