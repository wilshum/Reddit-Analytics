##! python3

from credentials import reddit
import praw
from praw.models import MoreComments
import pandas as pd
import datetime as dt

print(reddit.read_only)  # confirmation


def scrap_func(sname):

    subreddit = reddit.subreddit(sname)

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


def top_submission(sname):

    subreddit = reddit.subreddit(sname)
    
    top_submissions = subreddit.top(limit=5)

    # for submission in top_posts:
    #     print(submission.title)

    topics_dict = {
        "submissions": [], \
        "upvotes": []}

    for submission in top_submissions:
        topics_dict["submissions"].append(submission.title)
        topics_dict["upvotes"].append(submission.score)


    for submission in top_submissions:
        top_level_comments = list(submission.comments)

        # for comment in top_level_comments:
        #     print(comment)
        
        # for i in range(0,min(len(top_level_comments), 5)):
        #     if isinstance(top_level_comments[i], MoreComments):
        #         continue
        #     topics_dict["popular"].append(top_level_comments[i].body)
        #     topics_dict["likes"].append(top_level_comments[i].score)


    return topics_dict