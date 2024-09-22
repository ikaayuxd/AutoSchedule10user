import logging 
from os import environ
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from xaayux.config import API_ID, API_HASH, SESSION, SESSION2, channel_ids, DELAY

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

# Session 1
if SESSION is not None:
    session1 = StringSession(str(SESSION))
else:
    session1 = "pyrobot"

# Session 2
if SESSION2 is not None:
    session2 = StringSession(str(SESSION2))
else:
    session2 = "pyrobot2"

try:
    # Create both clients
    client = TelegramClient(
        session=session1,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged
    )

    client2 = TelegramClient(
        session=session2,
        api_id=API_ID,
        api_hash=API_HASH,
        connection=ConnectionTcpAbridged
    )

    # Define an asynchronous function to run the clients
    async def run_clients():
        async with client, client2:
            await client.start()
            print("Client 1 started!")
            await client2.start()
            print("Client 2 started!")
            # ... rest of your bot logic ...

    # Run the asynchronous function with the event loop
    asyncio.run(run_clients())

except Exception as e:
    print(e)
