# AutoSchedule10User - Telegram Multi-Userbot Scheduler

![Made with Python](http://ForTheBadge.com/images/badges/made-with-python.svg)

## Overview

AutoSchedule10User is a Telegram userbot project built with Telethon that allows running up to 10 concurrent userbots (sessions) to schedule and send messages automatically. Each userbot can react to new posts in specified Telegram channels with a heart emoji, enabling multi-account automation with ease.

This project is ideal for users who want to manage multiple Telegram accounts simultaneously for scheduling, reacting, and automating tasks.

---

## Features

- Supports up to 10 concurrent Telegram userbots (sessions).
- Automatically reacts with a heart emoji ❤️ to new posts in specified channels.
- Gracefully handles fewer than 10 sessions without errors.
- Easy configuration of API credentials and session strings.
- Uses Telethon for efficient Telegram client management.
- Modular plugin system for easy extension.
- Runs asynchronously for optimal performance.

---

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Telegram API credentials (API_ID and API_HASH) from [my.telegram.org](https://my.telegram.org)
- Session strings for your Telegram accounts (can be generated using Telethon scripts)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ikaayuxd/AutoSchedule10User.git
cd AutoSchedule10User
Install dependencies:
pip install -r requirements.txt
Configure your credentials and sessions:
Edit xaayux/config.py and set your API_ID, API_HASH, and up to 10 session strings (SESSION1 to SESSION10). Example:

API_ID = 'your_api_id'
API_HASH = 'your_api_hash'
SESSION1 = 'your_session_string_1'
SESSION2 = 'your_session_string_2'
# Set other SESSION variables or None if not used
SESSION3 = None
...
SESSION10 = None
Specify the channels to monitor for reactions in xaayux/plugins/reaction.py by updating the CHANNEL_IDS list with your target channel IDs.
```
## Usage
Run the userbots with:

python3 -m xaayux
This will start all configured userbots concurrently. Each userbot will listen for new messages in the specified channels and react with a heart emoji ❤️ automatically.

## Project Structure
xaayux/config.py: Configuration for API credentials, session strings, and other settings.
xaayux/__init__.py: Initializes Telegram clients, registers plugins, and runs clients concurrently.
xaayux/__main__.py: Entry point to start the application.
xaayux/plugins/reaction.py: Plugin that handles reacting to new messages in specified channels.
requirements.txt: Python dependencies.

## Extending the Project
Add more plugins in the xaayux/plugins/ directory.
Modify or add new event handlers to automate other Telegram interactions.
Scale beyond 10 userbots by extending the session management logic.

## Troubleshooting
Ensure all session strings are valid and correspond to logged-in Telegram accounts.
Verify that the userbots have access to the specified channels.
Check logs for errors related to client connections or event handling.

## Credits
Built with Telethon
Original project by @𝘅𝗔𝗮𝗬𝘂𝘅 and @𝗜𝗲𝗴𝗲𝗻𝗱𝘅𝗧𝗿𝗶𝗰𝗸𝘀

## License
This project is open source and free to use, modify, and distribute.

## For support and updates, join the Telegram Channel: https://t.me/LegendxTricks
