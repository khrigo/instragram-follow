# Instagram follow
Instagram scripts for promotion and API wrapper. Written in Python.
___
As you may know, Instagram closed it's API in summer 2016. This Python module can do the same thing without any effort. Also it has lots of example scripts to start with.

## How to install and update

Install latest stable version or update current from pip

``` python
sudo pip install -r requirements.txt
```

## Sample usage

Following user followers
```python
python follow_user_followers.py khrigo
```

Like user followers
```python
python like_user_followers.py khrigo
```

Unfollowing everyone users
```python
python unfollow_everyone.py
```

Use whitelist
```python
bot = Bot(whitelist="whitelist.txt")
```
