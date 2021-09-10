"""
# Token.py
# 
# Copyright (C) 2021 Christopher Stephen Rafuse <ImpishDeathTech@protonmail.ch>
# All rights reserved
#
# BSD-3-Clause
#
"""

import json

# Token is a class that loads a token from a known set contained in a json file
# it contains one function "get()" in witch @param token_idx is set to 0 by default 
# You should only keep one in there at a time, unless this is for a devbot

class Token:
    
    @classmethod
    def get(self, token_idx=0):
        data = {}
        
        with open("data/Token.json", 'r') as f:
            data = json.load(f)
            f.close
        
        token = data["BOT TOKENS"][token_idx]
        
        if not token == None:
            return token
