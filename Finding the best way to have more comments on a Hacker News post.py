#!/usr/bin/env python
# coding: utf-8

# # Finding the best way to have more comments on a Hacker News post
# ## In this project, we'll work with a data set of submissions to popular technology site Hacker News.
# ## We're specifically interested in posts whose titles begin with either Ask HN or Show HN. 
# ## Users submit Ask HN posts to ask the Hacker News community a specific question.
# ## Likewise, users submit Show HN posts to show the Hacker News community a project, product, or just generally something interesting.
# 
# ## We'll specifically compare these two types of posts to determine the following:
# 
# ## Do Ask HN or Show HN receive more comments on average?
# 
# ## Do posts created at a certain time receive more comments on average?

# # Importing the data

# In[1]:


# Exploring the dataset
from csv import reader
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)
hn[:5]


# # Removing headers from a list of list 

# In[2]:


# Removing the headers
headers = hn[0]
hn = hn[1:]
print(headers)
hn[:5]


# # Extracting Ask HN and Show HN posts

# In[3]:


# Identify posts that begin with either `Ask HN` or `Show HN` 
# and separate the data into different lists.

ask_posts = []
show_posts = []
other_posts = []

for post in hn:
    title = post[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(post)
    elif title.lower().startswith('show hn'):
        show_posts.append(post)
    else:
        other_posts.append(post)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))
             


# In[4]:


# Calculate the average number of comments `Ask HN` posts receive.
total_ask_comments = 0

for post in ask_posts:
    total_ask_comments += int(post[4])
    
avg_ask_comments = total_ask_comments / len(ask_posts)
print(avg_ask_comments)    


# In[5]:


total_show_comments = 0

for post in show_posts:
    total_show_comments += int(post[4])
    
avg_show_comments = total_show_comments / len(show_posts)
print(avg_show_comments)


# # Finding the amount of ask posts and         comments by hour created

# In[6]:


# Calculate the amount of ask posts created during each hour of day and the number of comments received.
import datetime as dt

result_list = []

for post in ask_posts:
    result_list.append(
        [post[6], int(post[4])]
    )

comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour


# # Calculating the Average Number of Comments for Ask HN Posts by Hour

# In[7]:


avg_by_hour = []

for hour in comments_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])

avg_by_hour


# # Sorting and Printing Values from a List of Lists

# In[8]:


swap_avg_by_hour = []
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap


# # Sorting and Printing Values from a List of Lists

# In[9]:


# Sort the values and print the the 5 hours with the highest average comments.
print('Top 5 Hours for Ask Pots Comments')

for average, hour in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hour, "%H").strftime("%H:%M"),average
        )
    )


# ### To conclude, based on our analysis, to maximize the amount of comments a post receives, we'd recommend the post be categorized as 'ask post' and created between 15:00 and 16:00.
# 
