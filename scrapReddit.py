##! python3

from credential import reddit
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt

print(reddit.user.me())  # confirmation

subreddit = reddit.subreddit('leagueoflegends')
# print(subreddit.display_name)
print("scrapped Reddit")

hot_subreddit = subreddit.top(limit=1)

topics_dict = {
    "likes": [], \
    "popular": []}

for submission in hot_subreddit:
    top_level_comments = list(submission.comments)
    for top_level_comment in top_level_comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        topics_dict["popular"].append(top_level_comment.body)
        topics_dict["likes"].append(top_level_comment.score)
    # all_comments = submission.comments.list()
    # for comment in all_comments:
    #     topics_dict["all"].append(comment.body)

topics_data = pd.DataFrame(data=topics_dict)

# def get_date(created):
#     return dt.datetime.fromtimestamp(created)
#
# timestamp = topics_data["created"].apply(get_date)
# topics_data = topics_data.assign(timestamp = timestamp)

topics_data.to_csv('data.csv', index=False)
