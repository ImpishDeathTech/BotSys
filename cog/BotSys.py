"""
# BotSys.py
# 
# Copyright (C) 2021 Christopher Stephen Rafuse <ImpishDeathTech@protonmail.ch> 
# BSD-3-Clause
#
"""


import discord, sys, subprocess, time, logging, os, json

from discord.ext import commands
from data.Token import Token

class BotSysConfig:
    MODERATOR_ROLE = ""
    TIME_STR = ""
    ACTIVITY = ""
    BOT_SCRIPT = ""
    
    LOG_STR = []
    
    CTX_STR = []
    
    def __init__(self):
        with open("./data/botsys-config.json", 'r') as f:
            data = json.load(f)
            
            self.MODERATOR_ROLE = data["MODERATOR ROLE"]
            self.TIME_STR = data["TIME STR"]
            self.ACTIVITY = data["ACTIVITY"]
            self.BOT_SCRIPT = data["BOT SCRIPT"]
            
            for n in range(len(data["LOG STR"])-1):
                self.LOG_STR.append(data["LOG STR"][n])
            
            for n in range(len(data["CTX STR"])-1):
                self.CTX_STR.append(data["CTX STR"][n])
            
            f.close()

C = BotSysConfig()


class BotSys(commands.Cog):
    """Cog containing basic methods for running and developing a bot"""
    
    def __init__(self, bot):
        self.Bot = bot
    
    
    ###########
    # helpers #
    ###########
    
    # returns the localtime of the server your bot is 
    # running on
    
    @classmethod
    async def get_localtime(self):
        return time.strftime(C.TIME_STR, time.localtime(time.time()))
    
    
    # load_extensions() - command function for loading all 
    # of the extensions in a directory to a bot. 
    # To be used in the startup script
    #
    # @param "bot" - the bot to load extensions to
    # @param "directory" - the directory from which to
    # load the extensions
    
    @classmethod
    def load_extensions(self, bot, directory):
        for f in os.listdir(directory):
            if f.endswith('.py'):
                bot.load_extension(f"{directory}.{f[:-3]}")
    
    ##########
    # events #
    ##########
    
    @commands.Cog.listener()
    async def on_ready(self):
        Bot = self.Bot
        
        logging.info(C.LOG_STR[0].format(Bot.user, str(Bot.user.id), await self.get_localtime()))
        logging.info(C.LOG_STR[1].format(Bot.command, await self.get_localtime()))
        
        await Bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=C.ACTIVITY))
        
        logging.info(C.LOG_STR[2].format(Bot.user.name, Bot.user, Bot.user.id, await self.get_localtime()))
    
    ############
    # commands #
    ############
    
    @commands.command()
    async def lt(self, ctx:commands.Context):
        """bot command to ask for the local time"""
        
        await ctx.send(f"```css\n Server.localtime({await self.get_localtime()});```")
    
    
    @commands.command()
    @commands.has_role(C.MODERATOR_ROLE)
    async def ping(self, ctx:commands.Context):
        """Tests the bot's latency'"""
        
        Bot = self.Bot
        
        logging.info(C.LOG_STR[3].format(Bot.user.name, Bot.latency, await self.get_localtime()))
        await ctx.send(C.CTX_STR[0].format(Bot.user.name, Bot.latency))
    
    
    @commands.command()
    @commands.has_role(C.MODERATOR_ROLE)
    async def shutdown(self, ctx:commands.Context):
        """Shuts down the bot"""
        
        Bot = self.Bot
        
        logging.info(C.LOG_STR[4].format(Bot.user.name, Bot.user, str(Bot.user.id), await self.get_localtime()))
        await ctx.send(C.CTX_STR[1])
        
        await ctx.bot.close()
        logging.info(C.LOG_STR[5].format(await self.get_localtime()))
    
    
    @commands.command()
    @commands.has_role(C.MODERATOR_ROLE)
    async def reset(self, ctx:commands.Context):
        """Resets the bot (disfunctional, needs update)"""
        
        Bot = self.Bot
        
        logging.info(C.LOG_STR[6].format(Bot.user.name, Bot.user, Bot.user.id, await self.get_localtime()))
        
        await ctx.send(C.CTX_STR[2])
        await ctx.bot.close()
        
        logging.info(C.LOG_STR[7].format(Bot.user, await self.get_local_time()))
        subprocess.call([sys.executable, BOT_SCRIPT])
    
    
    @commands.command(name="load")
    @commands.has_role(C.MODERATOR_ROLE)
    async def load_cog(self, ctx:commands.Context, cog):
        """Load an extension to the bot"""
        
        usr = ctx.user
        Bot = self.Bot
        
        Bot.load_extension(extension)
        logging.warning(C.LOG_STR[8].format(Bot.user.name, usr, usr.id, cog, await self.get_localtime()))
        await ctx.send(C.CTX_STR[3].format(cog))
    
    
    @commands.command(name="unload")
    @commands.has_role(C.MODERATOR_ROLE)
    async def unload_cog(self, ctx:commands.Context, cog):
        """Unload an extension from the bot"""
        
        usr = ctx.user
        Bot = self.Bot
        
        Bot.unload_extension(extension)
        logging.warning(C.LOG_STR[9].format(Bot.user.name, usr, usr.id, cog, await self.get_local_time()))
        await ctx.send(C.CTX_STR[4].format(Bot.user, cog))
    
    
    @commands.command(name="reload")
    @commands.has_role(C.MODERATOR_ROLE)
    async def reload_cog(self, ctx:commands.Context, cog):
        await self.unload_cog(ctx,cog)
        await self.load_cog(ctx,cog)

def setup(bot):
    bot.add_cog(BotSys(bot))

