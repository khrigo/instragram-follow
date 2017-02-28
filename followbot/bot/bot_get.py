"""
    All methods must return media_ids that can be
    passed into e.g. like() or comment() functions.
"""

import random

# getters

def get_userid_from_username(self, username):
    self.searchUsername(username)
    if "user" in self.LastJson:
        return str(self.LastJson["user"]["pk"])
    return None # Not found

def get_user_info(self, user_id):
    user_id = self.convert_to_user_id(user_id)
    self.getUsernameInfo(user_id)
    if 'user' not in self.LastJson:
        return False
    return self.LastJson['user']

def get_user_followers(self, user_id):
    user_id = self.convert_to_user_id(user_id)
    followers = self.getTotalFollowers(user_id)
    return [item['pk'] for item in followers] if followers else False

def get_user_following(self, user_id):
    user_id = self.convert_to_user_id(user_id)
    following = self.getTotalFollowings(user_id)
    return [item['pk'] for item in following] if following else False
