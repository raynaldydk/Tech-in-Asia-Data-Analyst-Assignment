# Tech in Asia - Data Analyst Assignment: 
## Overview
* Create a script to collect data from REST API
* Create a script to collect data automatically
* Understanding the data & removing unecessary features
* Perform an EDA in Tableau (https://public.tableau.com/app/profile/raynaldy.dwi.k/viz/TIAArticles/TIAArticlesAnalysis)
* Create a WordCloud and some more EDA in pandas
* Create a dashboard & stories using Tableau
* Preprocessing the data for NLP techniques
* Perform Sentiment Analysis using TextBlob
* Perform Topic Modelling using LDA

## EDA Highlights
![articles_distribution](https://user-images.githubusercontent.com/96482347/158934603-b7233a94-700f-4a6d-a1cd-874e76245adc.png)
![avg_comment_by_cat](https://user-images.githubusercontent.com/96482347/158934614-ad90bcd7-1694-474c-8437-d080396109dd.png)
![avg_comment_day_hour](https://user-images.githubusercontent.com/96482347/158934624-872c9a35-cdff-43ff-ac6a-5dad98762f74.png)
![article_vs_comments](https://user-images.githubusercontent.com/96482347/158943017-9504103a-31b1-42e2-95bc-eca17d8ad9ff.png)
![wordcloud](https://user-images.githubusercontent.com/96482347/158934633-e9900322-a372-416f-8b84-843295cbc2f5.png)

## Sentiment Analysis
![sentiment_textblob](https://user-images.githubusercontent.com/96482347/158934764-ec3a662b-6bd9-430c-a6d7-ca9f2663cf98.png)
![sentiment_author](https://user-images.githubusercontent.com/96482347/158934775-16095dae-a4d7-4a3f-9522-0395584df7b5.png)

## Topic Modelling
* Create topic modelling using all text
* Create topic modelling using only nouns
* Create topic modelling using nouns + adjective

## Findings
1) Blockchain, Analysis, Fintech have the highest average read time but low average comments. Articles about them are not effective? I'm not sure why but we need more metrics to confirm that.
2) Distributions of Articles by category are very good, only missing articles about TIA Jobs & Recruitment.
3) Saturday are the days that have higher average comments, we only posts a few articles in Saturday, maybe we can automate more articles in Saturday.
4) There are some unusual behavior that people tends to comment more on Monday night.
5) 6/10 of our top 10 authors are heavily Indian based articles, we need to get more articles about other Asia countries too.
6) In the sentiment analysis we can see that TIA bots have the highest positive value and the most opiniated author.
7) In the other hand Roehl are the most negative but most of them are facts.
8) LDA model doesn't really capture the topics, the topics generated are quite similar. Maybe I will get a better result using different techniques.
