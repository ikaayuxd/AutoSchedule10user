import glob
from pathlib import Path
from .utils import load_plugins
import asyncio
import logging
from . import client, client2 # Assuming client2 is defined in your '.init.py'

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Load plugins (after initializing clients)
path = "xaayux/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

async def run_clients():
    async with client:
        await client.start()
        print("Client 1 started!")
        await client.run_until_disconnected()

    async with client2:
        await client2.start()
        print("Client 2 started!")
        await client2.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(run_clients())
