import yfinance as yf
import newsapi
import praw
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries



plt.style.use('default')


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
stonks = set(maybeStonks)
indexes = []
for i in range(len(stonks)):
       print(stonks[i], "seen", str(maybeStonks.count(maybeStonks[index], "times in WSB"))

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
