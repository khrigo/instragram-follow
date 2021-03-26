import sys
import os

sys.path.append(os.path.join(sys.path[0],'../'))

from followbot import Bot

bot = Bot(backlist="backlist.txt")
bot.login()
bot.follow_followers(username)
