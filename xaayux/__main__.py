import glob
import asyncio
from pathlib import Path
from .utils import load_plugins
import asyncio
import logging
from . import client, client2 

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

if name == "main":
    async def main():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # Start both clients within the event loop
        await client.start()
        await client2.start()
        await client.run_until_disconnected() 
        await client2.run_until_disconnected()
        loop.close() # Close the loop after finishing

    asyncio.run(main())
