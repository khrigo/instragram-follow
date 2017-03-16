"""
    Filters
"""

import os
import io

def check_user(self, user_id):
    user_id = self.convert_to_user_id(user_id)

    if not user_id:
        return False

    if self.whitelist and str(user_id) in self.whitelist:
        return True
    if self.blacklist and user_id in self.blacklist:
        return False

    if self.following == []:
        self.following = self.get_user_following(self.user_id)
    if user_id in self.following:
        return False

    user_info = self.get_user_info(user_id)
    if not user_info:
        return False  # closed acc
    if "is_business" in user_info:
        if user_info["is_business"]:
            return False
    if "is_verified" in user_info:
        if user_info["is_verified"]:
            return False
    if "follower_count" in user_info and "following_count" in user_info:
        if user_info["follower_count"] < self.min_followers_to_follow:
            return False
        if user_info["follower_count"] > self.max_followers_to_follow:
            return False
        if user_info["following_count"] < self.min_following_to_follow:
            return False
        if user_info["following_count"] > self.max_following_to_follow:
            return False
        try:
            if user_info["follower_count"] / user_info["following_count"] \
                    > self.max_followers_to_following_ratio:
                return False
            if user_info["following_count"] / user_info["follower_count"] \
                    > self.max_following_to_followers_ratio:
                return False
        except ZeroDivisionError:
            return False

    if 'media_count' in user_info:
        if user_info["media_count"] < self.min_media_count_to_follow:
            return False  # bot or inactive user

    return True

def check_private(self, user_id):
    if not user_id:
        return True

    user_info = self.get_user_info(user_id)
    if "is_private" in user_info:
        if user_info["is_private"]:
            return True
    return False

def convert_to_user_id(self, smth):
    if type(smth) == str and not smth.isdigit():
        if smth[0] == "@": # cut first @
            smth = smth[1:]
        smth = self.get_userid_from_username(smth)
    # if type is not str than it is int so user_id passed
    return smth
