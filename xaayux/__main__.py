# In your main bot script
from .. import client, client2
from .utils import load_plugins
import asyncio

# ... your other code ...

# Load plugins (after initializing clients)
path = "xaayux/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

# Start your clients
async with client:
    await client.start()
    print("Client 1 started!")
    await client.run_until_disconnected()

async with client2:
    await client2.start()
    print("Client 2 started!")
    await client2.run_until_disconnected()
