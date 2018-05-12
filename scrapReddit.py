##! python3

from credential import reddit
import praw
import pandas as pd
import datetime as dt

print(reddit.user.me())  # confirmation

subreddit = reddit.subreddit('leagueoflegends')
print(subreddit.display_name)

top_subreddit = subreddit.new(limit = 5)
print(top_subreddit)

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = timestamp)

topics_data.to_csv('result.csv', index = False)
