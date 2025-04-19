import logging 
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from xaayux import config
import xaayux.plugins.reaction as reaction_plugin

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

# Collect all session strings in a list dynamically
sessions = []
for i in range(1, 11):
    session_var = f'SESSION{i}'
    session_value = getattr(config, session_var, None)
    sessions.append(session_value)

clients = []

# Create TelegramClient instances for each valid session string
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

# Register plugins for all clients
async def register_plugins():
    await reaction_plugin.setup(clients)

# Define an asynchronous function to run all clients concurrently
async def run_clients():
    await register_plugins()
    tasks = []
    for i, client in enumerate(clients):
        tasks.append(asyncio.create_task(start_client(client, i+1)))
    await asyncio.gather(*tasks)

async def start_client(client, client_number):
    try:
        await client.start()
        logging.info(f"Client {client_number} started!")
        await client.run_until_disconnected()
    except Exception as e:
        logging.error(f"Client {client_number} encountered an error: {e}")

# Explicitly create an event loop and run the clients
async def main():
    await run_clients()

if __name__ == "__main__":
    asyncio.run(main())
