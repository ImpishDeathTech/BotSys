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

import discord, logging, sys

from discord.ext import commands
from cog.BotSys import BotSys

# bot client
Bot = commands.Bot(command_prefix='dg.', case_insensitive=True, description="Penis")

if __name__ == "__main__":
    # configure the logger
    logging.basicConfig(filename="./log/death-grid.log", level=logging.INFO)
    logging.info("DeathGrid.py -> started")
    
    # load any extensions in a given directory
    BotSys.load_extensions(bot=Bot,directory="cog")
    
    # run the bot and exit with the returned code
    sys.exit(BotSys.run(bot=Bot, token_idx=2))
