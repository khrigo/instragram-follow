"""
    Filters
"""

import os
import io

def check_user(self, user_id):
    """
        Decide should you interract with that user_id or not.
    """
    if not user_id:
        return True

    user_info = self.get_user_info(user_id)
    if not user_info:
        return True # closed acc
    if "is_business" in user_info:
        if user_info["is_business"]:
            return False
    if "is_verified" in user_info:
        if user_info["is_verified"]:
            return False
    if "follower_count" in user_info and "following_count" in user_info:
        if user_info["follower_count"] < 100:
            return True # not famous user
        if user_info["following_count"] < 10:
            return False
        if user_info["follower_count"] / user_info["following_count"] > 10:
            return False # too many
        if user_info["following_count"] / user_info["follower_count"] > 2:
            return True # too many
    if 'media_count' in user_info:
        if user_info["media_count"] < 3:
            return False # bot or inactive user
    return True

def convert_to_user_id(self, smth):
    if type(smth) == str and not smth.isdigit():
        if smth[0] == "@": # cut first @
            smth = smth[1:]
        smth = self.get_userid_from_username(smth)
    # if type is not str than it is int so user_id passed
    return smth
