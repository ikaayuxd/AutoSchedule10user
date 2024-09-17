import glob
from pathlib import Path
from .utils import load_plugins
import logging
from . import client, client2 # Assuming client2 is defined in your '.__init__.py'

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "xaayux/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")

if name == "main":
    client.run_until_disconnected() # Run client1
    client2.run_until_disconnected() # Run client2
