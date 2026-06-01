import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_csv("X_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df.dropna(inplace=True)

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = text.strip()
    return text

df['Processed_Text'] = df['clean_text'].apply(clean_text)

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['Processed_Text'].apply(get_sentiment)

print("\nSentiment Counts:")
print(df['Sentiment'].value_counts())

plt.figure(figsize=(8,5))
sns.countplot(x='Sentiment', data=df)
plt.title("Sentiment Distribution of X Posts")
plt.xlabel("Sentiment")
plt.ylabel("Number of Posts")
plt.show()

sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct='%1.1f%%'
)
plt.title("Sentiment Percentage Distribution")
plt.show()

print("\nSample Sentiment Results:")
print(df[['clean_text', 'Sentiment']].head(10))

df.to_csv("sentiment_analysis_results.csv", index=False)

print("\nSentiment Analysis Completed Successfully!")
print("Results saved as 'sentiment_analysis_results.csv'")
