from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity (-1 for negative, 1 for positive, 0 for neutral)
    sentiment_polarity = blob.sentiment.polarity
    
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    print("Simple Sentiment Analysis Program")
    print("---------------------------------")
    
    while True:
        user_input = input("Enter some text (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        sentiment = analyze_sentiment(user_input)
        print(f"Sentiment: {sentiment}")
        print()

if __name__ == "__main__":
    main()
