"""
    Like user followers.
"""

import sys
import os
import time
import random
from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0],'../'))
from followbot import Bot

if len(sys.argv) < 2:
    print ("USAGE: Pass username.")
    print ("Example: python %s khrigo" % sys.argv[0])
    exit()

bot = Bot()
bot.login()
for username in sys.argv[1:]:
    bot.like_followers(username)
