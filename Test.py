#! /usr/bin/python3

"""
# Test.py
# 
# Copyright (C) 2021 Christopher Stephen Rafuse <ImpishDeathTech@protonmail.ch>
# BSD-3-Clause
#
"""

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
