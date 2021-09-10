## A basic startup file I'd write using BotSys would look something like this

```py
import discord, logging, sys, time

from discord.ext import commands
from cog.BotSys import BotSys, C, Token

Bot = commands.Bot(command_prefix='bot.', case_insensitive=True, description="Penis")

if __name__ == "__main__":
    logging.basicConfig(filename="./log/test.log", level=logging.INFO)
    
    logging.info(f"BotDaemon - Loading Installed Extentions... - {time.strftime(C.TIME_STR, time.localtime(time.time()))}")
    BotSys.load_extensions(bot=Bot,directory="cog")
    
    logging.info(f"BotDaemon - Running Bot... - {time.strftime(C.TIME_STR, time.localtime(time.time()))}")
    Bot.run(Token.get(2))
    
    logging.info(f"BotDaemon - Exiting with code(0) - {time.strftime(C.TIME_STR, time.localtime(time.time()))}")
    sys.exit(0) 
```

#### BotSys has a few nifty functions, you can look through the code to see them as they're all pretty simple and you might wanna change shit
#### If you get any good ideas you wanna add to this or change in this, let me know, I'm all for it :3

##### For now we have for commands:

`bot.ping` - your typical latency check

`bot.lt` - localtime of the bot's running server

`bot.shutdown` - shuts it down

`bot.reset` - does't work yet

`bot.load <dir.MyCog>` - loads a cog dynamically to the bot during runtime

`bot.unload <dir.MyCog>` - same as above, but for unloading

`bot.reload <dir.MyCog>` - preforms the two above functions in succession

#### And for classmethods, we have:
````py
# the function behind bot.lt
await BotSys.localtime()

# A method for loading all of the extensions
# contained within an indicated directory
BotSys.load_extensions(bot,directory)

# the only function Token has gets your token from the json file in the data directory
Token.get(token_idx)
```
