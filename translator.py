import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip
import pyttsx3

st.set_page_config(page_title="Language Translator")

st.title("🌍 Language Translation Tool")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

text = st.text_area("Enter Text to Translate")

source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        translated_text = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translated Text")

        st.text_area(
            "Output",
            translated_text,
            height=150
        )

        if st.button("Copy Result"):
            pyperclip.copy(translated_text)
            st.success("Copied Successfully!")

        if st.button("Speak Translation"):
            engine = pyttsx3.init()
            engine.say(translated_text)
            engine.runAndWait()