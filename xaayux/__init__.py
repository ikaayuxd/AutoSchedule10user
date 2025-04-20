import logging 
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from xaayux import config
import xaayux.plugins.reaction as reaction_plugin
import xaayux.plugins.bot_controls as bot_controls_plugin

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

sessions = []
for i in range(1, 11):
    session_var = f'SESSION{i}'
    session_value = getattr(config, session_var, None)
    sessions.append(session_value)

clients = []

for i, session_str in enumerate(sessions):
    if session_str is not None:
        try:
            session = StringSession(str(session_str))
            client = TelegramClient(
                session=session,
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                connection=ConnectionTcpAbridged
            )
            clients.append(client)
            logging.info(f"Client {i+1} created.")
        except Exception as e:
            logging.error(f"Failed to create client {i+1}: {e}")

async def register_plugins():
    await reaction_plugin.setup(clients)

async def run_clients():
    await register_plugins()
    bot_task = asyncio.create_task(bot_control_plugins.start_bot(clients))
    client_tasks = [asyncio.create_task(start_client(client, i+1)) for i, client in enumerate(clients)]
    await asyncio.gather(bot_task, *client_tasks)

async def start_client(client, client_number):
    try:
        await client.start()
        logging.info(f"Client {client_number} started!")
        await client.run_until_disconnected()
    except Exception as e:
        logging.error(f"Client {client_number} encountered an error: {e}")

async def main():
    await run_clients()

if __name__ == "__main__":
    asyncio.run(main())
