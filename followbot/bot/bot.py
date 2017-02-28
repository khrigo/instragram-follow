import os
import sys
import datetime
import atexit
import signal
import logging
import io

from tqdm import tqdm

from .. import API
from . import limits

from .bot_get import get_userid_from_username
from .bot_get import get_user_info
from .bot_get import get_user_followers
from .bot_get import get_user_following

from .bot_follow import follow
from .bot_follow import follow_users
from .bot_follow import follow_followers

from .bot_unfollow import unfollow
from .bot_unfollow import unfollow_users
from .bot_unfollow import unfollow_everyone

from .bot_filter import check_user
from .bot_filter import convert_to_user_id

class Bot(API):
    def __init__(self,
                 max_follows_per_day=350,
                 follow_delay=30,
                 max_unfollows_per_day=350,
                 unfollow_delay=10):
        super(self.__class__, self).__init__()

        self.total_followed = 0
        self.total_unfollowed = 0
        self.start_time = datetime.datetime.now()

        # limits
        self.max_follows_per_day = max_follows_per_day
        self.max_unfollows_per_day = max_unfollows_per_day

        # delays
        self.follow_delay = follow_delay
        self.unfollow_delay = unfollow_delay

        # handle logging
        self.logger = logging.getLogger('[Instagram follow]')
        self.logger.setLevel(logging.DEBUG)
        logging.basicConfig(format='%(asctime)s %(message)s', filename='followbot.log', level=logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.info('Bot Started')

        # current following
        self.following = []

        signal.signal(signal.SIGTERM, self.logout)
        atexit.register(self.logout)

    def logout(self):
        super(self.__class__, self).logout()
        self.logger.info("Bot stopped. "
               "Worked: %s" % (datetime.datetime.now() - self.start_time))
        if self.total_followed:
            self.logger.info("  Total followed: %d" % self.total_followed)
        if self.total_unfollowed:
            self.logger.info("  Total unfollowed: %d" % self.total_unfollowed)

# getters

    def get_userid_from_username(self, username):
        return get_userid_from_username(self, username)

    def get_user_info(self, user_id):
        return get_user_info(self, user_id)

    def get_user_followers(self, user_id):
        return get_user_followers(self, user_id)

    def get_user_following(self, user_id):
        return get_user_following(self, user_id)

# follow

    def follow(self, user_id):
        return follow(self, user_id)

    def follow_users(self, user_ids):
        return follow_users(self, user_ids)

    def follow_followers(self, user_id):
        return follow_followers(self, user_id)

# unfollow

    def unfollow(self, user_id):
        return unfollow(self, user_id)

    def unfollow_users(self, user_ids):
        return unfollow_users(self, user_ids)

    def unfollow_everyone(self):
        return unfollow_everyone(self)

# filter

    def check_user(self, user):
        return check_user(self, user)

    def convert_to_user_id(self, usernames):
        return convert_to_user_id(self, usernames)
