import yfinance as yf
import newsapi
import praw
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries


key = 'A8JZ69J154CEQR2W'
ts = TimeSeries(key, output_format='pandas')
#newsAPi = newsApiClient(api_key='539ff4120e9c4cc7b15030408deb9ab4')

plt.style.use('default')


reddit = praw.Reddit(client_id="tDk4i02L9gIk8w",
                     client_secret="E1rtw8mlCleaaBOeuvkQZLgnWyGT1g",
                     username="nano1999",
                     password="Pingapinga1",
                     user_agent="deeeepValuee")

subreddit = reddit.subreddit('wallstreetbets')
top_subreddit = subreddit.rising(limit=100)
words = []


for submission in top_subreddit:
    title = submission.title
    title_words = title.split()
    words.append(title_words)

maybeStonks = []
notStonks = ["UPVOTE", "SUPPORT", "YOLO", "CLASS", "ACTION", "AGAINST", "ROBBINHOOD", "GAIN", "LOSS", "PORN",
             "I'M", "ALL", "IN", "WSB", "WSB.", "I", "STILL", "DIDN'T", " HEAR", "NO", "BELL", "YOLO.",
             "**ALREADY**", "YOLO!", "LOVE", "UPDATE", "GO!!", "THE", "REST", "LIKE"]

for title in words:
    for word in title:
        if word.isupper() and word not in notStonks:
            maybeStonks.append(word)
stonks = []
indexes = []
for stonk in maybeStonks:
    index = 0
    for i in range(len(maybeStonks)):
        if(stonk == maybeStonks[i]):
            index = i
    if(index not in indexes):
        indexes.append(index)
        stonks.append(stonk)
        print(stonk + ": " + str(maybeStonks.count(maybeStonks[index])))

sign = input(
    "which of these stocks intrests you? \n type quit to exit the program ")

while(sign != 'quit'):
    try:
        data, meta = ts.get_intraday(sign, interval='1min', outputsize='full')
        # print(data.info())
        plt.plot(data['4. close'])
        plt.ylabel('price')
        plt.xlabel('date')
        plt.title("Stock price of $"+sign + " over the past 10 days.")
        plt.show()
    except:
        print("\nan error has ocurred. Please reenter the stock sign\n")
    sign = input(
        "which of these stocks intrests you? \ntype quit to exit the program ")
print("Thanks for coming!")
