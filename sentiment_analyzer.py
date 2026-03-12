from textblob import TextBlob

news = [
    "Apple stock is rising due to strong iPhone sales",
    "Tesla shares fall after disappointing earnings",
    "Microsoft reports strong quarterly growth"
]

for headline in news:
    analysis = TextBlob(headline)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        result = "Positive"
    elif sentiment < 0:
        result = "Negative"
    else:
        result = "Neutral"

    print(headline, "->", result)
