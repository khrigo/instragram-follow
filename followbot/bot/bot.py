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

from .bot_like import like
from .bot_like import like_medias
from .bot_like import like_user_id
from .bot_like import like_users
from .bot_like import like_followers

class Bot(API):
    def __init__(self,
                 max_follows_per_day=350,
                 follow_delay=30,
                 max_unfollows_per_day=2000,
                 unfollow_delay=7,
                 max_likes_per_day=1000,
                 like_delay=5):
        super(self.__class__, self).__init__()

        self.total_followed = 0
        self.total_unfollowed = 0
        self.total_liked = 0
        self.start_time = datetime.datetime.now()

        # limits
        self.max_likes_per_day = max_likes_per_day
        self.max_follows_per_day = max_follows_per_day
        self.max_unfollows_per_day = max_unfollows_per_day

        # delays
        self.like_delay = like_delay
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
        if self.total_liked:
            self.logger.info("  Total liked: %d" % self.total_liked)

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

# like

    def like(self, media_id):
        return like(self, media_id)

    def like_medias(self, media_ids):
        return like_medias(self, media_ids)

    def like_user_id(self, user_id, amount=None):
        return like_user_id(self, user_id, amount)

    def like_users(self, user_ids, nlikes=None):
        return like_users(self, user_ids, nlikes)

    def like_followers(self, user_id, nlikes=None):
        return like_followers(self, user_id, nlikes)

# filter

    def check_user(self, user):
        return check_user(self, user)

    def convert_to_user_id(self, usernames):
        return convert_to_user_id(self, usernames)
