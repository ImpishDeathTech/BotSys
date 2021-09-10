#! /usr/bin/python3

"""
# Test.py
# 
# Copyright (C) 2021 Christopher Stephen Rafuse <ImpishDeathTech@protonmail.ch>
# All rights reserved
#
# BSD-3-Clause
#
"""

import discord, logging, sys, time

from discord.ext import commands
from cog.BotSys import BotSys, C, Token

Bot = commands.Bot(command_prefix='bot.', case_insensitive=True, description="Penis")
t_ = lambda:time.strftime(C.TIME_STR, time.localtime(time.time())) # time

if __name__ == "__main__":
    logging.basicConfig(filename="./log/test.log", level=logging.INFO)
    
    logging.info(f"BotDaemon - Loading Installed Extentions... - {t_()}")
    BotSys.load_extensions(bot=Bot,directory="cog")
    
    logging.info(f"BotDaemon - Running Bot... - {t_()}")
    Bot.run(Token.get(2))
    
    logging.info(f"BotDaemon - Exiting with code(0) - {t_()}")
    sys.exit(0) 
