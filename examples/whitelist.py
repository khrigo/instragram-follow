import sys
import os

sys.path.append(os.path.join(sys.path[0],'../'))

from followbot import Bot

bot = Bot(whitelist="whitelist.txt")
bot.login()
bot.unfollow_everyone()
