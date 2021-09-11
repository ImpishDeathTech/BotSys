## A basic startup script I'd write using BotSys would look something like this

```py
#! /usr/bin/python3

import discord, logging, sys

from discord.ext import commands
from cog.BotSys import BotSys

# bot client
Bot = commands.Bot(command_prefix='test.', case_insensitive=True, description="A basic bot ready for development")

if __name__ == "__main__":
    # configure the logger
    logging.basicConfig(filename="./log/test.log", level=logging.INFO)
    logging.info("Test.py -> started")
    
    # load any extensions in a given directory
    BotSys.load_extensions(bot=Bot,directory="cog")
    
    # run the bot and exit with the returned code
    sys.exit(BotSys.run(bot=Bot, token_idx=2))
```

#### BotSys has a few nifty functions, you can look through the code to see how they work and tweak them to your liking they're all pretty simple, and you might wanna change shit cause you don't like the way I do things for whatever reason 
#### If you get any good ideas you wanna add to this or change in this, let me know, I'm all for it :3

##### For now what I have for commands is:

`bot.ping` - your typical latency check

`bot.lt` - localtime of the bot's running server

`bot.shutdown` - shuts it down

`bot.reset` - does't work yet

`bot.load <dir.MyCog>` - loads a cog dynamically to the bot during runtime

`bot.unload <dir.MyCog>` - same as above, but for unloading

`bot.reload <dir.MyCog>` - preforms the two above functions in succession

##### And for classmethods, I have:
````py
# the classmethod behind bot.lt
await BotSys.localtime()

# A classmethod for loading all of the extensions
# contained within an indicated directory
tm = BotSys.load_extensions(bot=BotClient,directory="./extension/directory")

# classmethods for loading and unloading json data
data = await BotSys.json_get(file_path="path/to/file.json")
data["time"] = tm
await BotSys.json_set(data=data,file_path="path/to/file.json", indent=3)

# classmethod to run the bot using a secret token list
# returns -2 if login fails
exit_code = BotSys.run(bot=BotClient,token_idx=idx)
sys.exit(exit_code)
