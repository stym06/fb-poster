"""

Author: Satyam Raj
"""
import facebook
import requests
import datetime

# Configuration

################################

# Insert your access token here.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'your access toke here'
# Fetch contents of your own wall by setting user to me
user = 'me'
# Set your birthday here in the same format:
birthday = '2017-06-06'

################################


def parse_date(post):
    """
    Parse date from Facebook's format to Python's datetime format.
    """
    post_date = datetime.datetime.strptime(
        post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    return post_date.date()


def like_and_comment(post):
    """
    This function likes and comments on posts sent to it.
    """
    message = "Thank you so much! :)"

    graph.put_like(post['id'])
    graph.put_comment(post['id'], message)

# convert birthday to datetime
bday = datetime.datetime.strptime(birthday, '%Y-%m-%d')

# Fetch graph, own profile and posts.
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'feed')

# Get all posts made on your birthday from your wall.
# This code assumes they're all 'happy birthday' type posts.
birthday_posts = [
    post for post in posts['data'] if parse_date(post) == bday.date()]


# Now like and comment on all birthday posts
for idx, post in enumerate(birthday_posts):
    like_and_comment(post)
    print('Post %d successfully processed.' % idx)
