import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def textblob_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

def vader_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    sentiment = vs['compound']
    return sentiment

def display_sentiment(sentiment):
    if sentiment > 0:
        label = 'Positive'
    elif sentiment < 0:
        label = 'Negative'
    else:
        label = 'Neutral'
    st.write('Sentiment Score:', sentiment)
    st.write('Sentiment Label:', label)

def main():
    st.title('Sentiment Analysis App')
    text = st.text_input('Enter some text:')
    if st.button('Analyze'):
        st.write('Using TextBlob:')
        textblob_result = textblob_sentiment(text)
        display_sentiment(textblob_result)
        st.write('Using VaderSentiment:')
        vader_result = vader_sentiment(text)
        display_sentiment(vader_result)

if __name__ == '__main__':
    main()
