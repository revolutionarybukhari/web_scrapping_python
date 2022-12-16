#!/usr/bin/env python
# coding: utf-8

# In[51]:


import snscrape.modules.twitter as sntwitter
import pandas as pd

tweets_list1 = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:ImranKhanPTI').get_items()): 
    if i>1000:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) 
    
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])


# In[54]:


tweets=tweets_df1["Text"]


# In[1]:


import snscrape.modules.twitter as sntwitter
import pandas as pd


# In[ ]:


sntwitter.


# In[10]:


maxTweets = 8000

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:ImranKhanPTI').get_items()):
    if i>maxTweets:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])


# In[11]:


# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
tweets_df1.head()


# In[7]:


# Export dataframe into a CSV
tweets_df1.to_csv('ImranKhan-tweets.csv', sep=',', index=False)


# In[3]:


import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools


# In[6]:


df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"#FloodsInPakistan"').get_items(),1000))


# In[7]:


df


# In[9]:


df.to_csv('FloodsInPakistan-tweets.csv', sep=',', index=False)


# In[10]:


df2 = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"#FloodsInPakistan2022"').get_items(),1000))


# In[11]:


df2


# In[12]:


df2.to_csv('FloodsInPakistan2022-tweets.csv', sep=',', index=False)


# In[13]:


df3 = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper('"#PakistanFloodsAppeal"').get_items(),1000))


# In[14]:


df3


# In[15]:


df3.to_csv('PakistanFloodsAppeal-tweets.csv', sep=',', index=False)


# In[ ]:




