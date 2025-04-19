import asyncio
from telethon import events, functions, types
from xaayux.config import CHANNEL_IDS

async def react_to_message(event, client):
    if event.is_channel:
        try:
            await client(functions.messages.SendReactionRequest(
                peer=event.chat_id,
                msg_id=event.id,
                big=True,
                add_to_recent=True,
                reaction=[types.ReactionEmoji(emoticon='❤️')]
            ))
            print(f"Client reacted to message from {event.chat.title} with ❤️")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Client Error: {e}")

def register(client):
    @client.on(events.NewMessage(chats=CHANNEL_IDS))
    async def handler(event):
        await react_to_message(event, client)

async def setup(clients):
    for i, client in enumerate(clients):
        try:
            register(client)
            print(f"Reaction handler registered for client {i+1}")
        except Exception as e:
            print(f"Failed to register reaction handler for client {i+1}: {e}")
