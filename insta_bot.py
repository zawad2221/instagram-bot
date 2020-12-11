from instapy import InstaPy
from os import environ

USERNAME = environ['USERNAME']
PASSWORD = environ['PASSWORD']
session = InstaPy(username=USERNAME, password=PASSWORD)

session.login()
session.like_by_feed(amount=100, randomize=True, unfollow=False,interact=False)
session.end()
