import pandas as pd
import matplotlib.pyplot as plt

def autopct_format(values): # A function for displaying percentages on a pie chart
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{:.1f}%\n({v:d})'.format(pct, v=val)
    return my_format

df = pd.read_csv("fifa_world_cup_2022_tweets.csv")

# Question 1: What is the prevailing sentiment of the tweets?
neutral = len(df.loc[df["Sentiment"] == "neutral"])
negative = len(df.loc[df["Sentiment"] == "negative"])
positive = len(df.loc[df["Sentiment"] == "positive"])
plt.bar("Neutral", neutral, color = "lightblue", label = neutral)
plt.bar ("Negative", negative, color = "red", label = negative)
plt.bar ("Positive", positive, color = "green", label = positive)
plt.xlabel("Sentiment")
plt.ylabel("Number of tweets")
plt.legend()
plt.show()

# Question 2: What are the sources of the most tweets?
tw_web_app = len(df.loc[df["Source of Tweet"] == "Twitter Web App"])
tw_for_ip = len(df.loc[df["Source of Tweet"] == "Twitter for iPhone"])
tw_for_an = len(df.loc[df["Source of Tweet"] == "Twitter for Android"])
tw_for_mac = len(df.loc[df["Source of Tweet"] == "Twitter for Mac"])
labels = ["Twitter Web App", 
          "Twitter for iPhone", 
          "Twitter for Android", 
          "Twitter for Mac"]
results = [tw_web_app, tw_for_ip, tw_for_an, tw_for_mac]
plt.pie(results, labels = labels, autopct=autopct_format(results))
plt.show()

# Question 3: What are the three most popular tweets?
most_pop_tweets = df.sort_values(["Number of Likes"], ascending=False)[0:3].reset_index()
print(most_pop_tweets)

# Question 4: What time was usually the most active?
df["Date Created"] = pd.to_datetime(df["Date Created"])
df["Hour"] = df["Date Created"].dt.hour
df["Count"] = 1
hours = [hour for hour, df in df.groupby("Hour")]
results = df.groupby(["Hour"]).count()
plt.plot(hours, results, color="g", marker="o")
plt.xticks(hours)
plt.xlabel("Hour")
plt.ylabel("Number of Tweets")
plt.grid()
plt.show()