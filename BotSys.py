import discord, sys, subprocess, time, logging, os

from discord.ext import commands

MODERATOR_ROLE = "Banging-On-Keys-Writing-Python"
TIME_STR = '%a.%b(%Y, %d)[%H:%M:%S]'
ACTIVITY = "you play with your fucking anus"
BOT_SCRIPT = "Test.py"
LOG_STR = [
    "BotSys - Logged In - {0} | {1} - {2}",
    "BotSys - Loading Command - {0} - {1}",
    "{0} - Bot Initialized - {1} | {2} open for business! ^,..,^ - {3}",
    "{0} - Pong! ^,..,^ - Latency : {1} - {2}",
    "{0} - Shudown Initiated - Logging out of {0} | {1} and shutting down now... - {2}",
    "BotSys - Shutdown Completed - see you again next time ^,..,^ - {}",
    "{0} - Reset Initiated - Logging out of {1} | {2} and shutting down now... - {3}",
    "BotSys - Restarting Bot - Flipping {0} ove in it's grave - {1}'"
    "{0} - USER = {1}, ID = {2}, ACTION = Loading_Extension - {3} - {4}"
]


class BotSys(commands.Cog):
    """Cog containing basic methods for running and developing a bot"""
    
    def __init__(self, bot):
        self.Bot = bot
    
    
    # helpers
    @classmethod
    async def get_localtime(self):
        """returns the localtime of the bot's server"""
        
        return time.strftime(TIME_STR, time.localtime(time.time()))
    
    
    @classmethod
    def load_extensions(self, bot, directory):
        for f in os.listdir(directory):
            if not f == "BotToken" and f.endswith('.py'):
                bot.load_extension(directory+f[:-3])
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        """Bot's on_ready event'"""
        
        Bot = self.Bot
        
        logging.info(LOG_STR[0].format(Bot.user, str(Bot.user.id), await self.get_localtime()))
        logging.info(LOG_STR[1].format(Bot.command, await self.get_localtime()))
        
        await Bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=ACTIVITY))
        
        logging.info(LOG_STR[2].format(Bot.user.name, Bot.user, Bot.user.id, await self.get_localtime()))
    
    
    @commands.command("lt")
    async def lt(self, ctx:commands.Context):
        """bot function to ask for the local time"""
        
        await ctx.send(self.get_localtime)
    
    
    @commands.command()
    @commands.has_role(MODERATOR_ROLE)
    async def ping(self, ctx:commands.Context):
        """Tests the bot's latency'"""
        
        Bot = self.Bot
        
        logging.info(LOG_STR[3].format(Bot.user.name, Bot.latency, await self.get_loacaltime()))
        await ctx.send(f"```css\nPong! ^,..,^\nLatency : {Bot.latency}```")
    
    
    @commands.command()
    @commands.has_role(MODERATOR_ROLE)
    async def shutdown(self, ctx:commands.Context):
        """Shuts down the bot"""
        
        Bot = self.Bot
        
        logging.info(LOG_STR[4].format(Bot.user.name, Bot.user, str(Bot.user.id), await self.get_localtime()))
        await ctx.send("```css\nShutdown initiatied!\nLogging out and shutting down, now...```")
        
        await ctx.bot.close()
        logging.info(LOG_STR[5].format(await self.get_localtime()))
    
    
    @commands.command()
    @commands.has_role(MODERATOR_ROLE)
    async def reset(self, ctx:commands.Context):
        """Resets the bot"""
        
        Bot = self.Bot
        
        logging.info(LOG_STR[6].format(Bot.user.name, Bot.user, Bot.user.id, await self.get_local_time()))
        await ctx.send("```css\nReset initiatied!\nLogging out and shutting down, now...```")
        
        await ctx.bot.close()
        logging.info(LOG_STR[7].format(Bot.user, await self.get_local_time()))
        subprocess.call([sys.executable, BOT_SCRIPT])
    
    
    @commands.command(name="load")
    @commands.has_role(MODERATOR_ROLE)
    async def load_cog(self, ctx:commands.Context, cog):
        """Load an extension to the bot"""
        
        usr = ctx.user
        
        Bot = self.Bot
        
        Bot.load_extension(extension)
        
        logging.warning(LOG_STR[8].format(Bot.user.name, usr, usr.id, cog, await self.get_local_time()))
        await ctx.send(f"```css\nLoading Extension {cog}```")
    
    
    @commands.command(name="unload")
    @commands.has_role(MODERATOR_ROLE)
    async def unload_cog(self, ctx:commands.Context, cog):
        """Unload an extension from the bot"""
        
        usr = ctx.user
        
        self.bot.unload_extension(extension)
        
        print(f"{self.bot.user.name} - USER = {usr}, ID = {usr.id}, ACTION = Unloading_Extension - {cog} - {await self.get_local_time}")
        await ctx.send(f"```css\nUnloading Extension {cog}```")
    
    
    @commands.command(name="reload")
    @commands.has_role(MODERATOR_ROLE)
    async def reload_cog(self, ctx:commands.Context, cog):
        await self.unload_cog(ctx,cog)
        await self.load_cog(ctx,cog)


def setup(bot):
    bot.add_cog(BotSys(bot))
