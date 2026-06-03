import streamlit as st
from textblob import TextBlob

st.title("Text Analyser")

user_text=st.text_area("Enter your text here")

if st.button("Analyser Sentiment"):
    blob=TextBlob(user_text)
    polarity=blob.sentiment.polarity
    subjectivity=blob.sentiment.subjectivity

    if polarity > 0:
        st.success("Text is positive")
    elif polarity < 0:
        st.error("Text is negative")
    elif polarity == 0:
        st.warning("Text is neutral")


    if subjectivity == 0:
        st.success("It's a Fact")
    else:
        st.warning("It's a opinion")

        # /Users/sanjeev/Downloads/New.py