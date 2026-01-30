"""
Advanced Word Cloud Generator - Main Streamlit Application
"""
import streamlit as st
import pandas as pd

from config import MIN_WORDS, THEMES, DEFAULT_MAX_WORDS, DEFAULT_MAX_FONT_SIZE
from file_readers import read_uploaded_file
from text_processing import preprocess_text, get_word_frequencies
from wordcloud_generator import create_wordcloud, render_wordcloud, save_wordcloud_to_buffer


# ------------------------
# Page Config
# ------------------------
st.set_page_config(page_title="Advanced Word Cloud", layout="centered")
st.title("☁️ Advanced Word Cloud Generator")


# ------------------------
# Sidebar Controls
# ------------------------
st.sidebar.header("🎛 Controls")

theme = st.sidebar.selectbox("🎨 Theme", list(THEMES.keys()))
use_stopwords = st.sidebar.checkbox("Remove stopwords", value=True)
use_lemmatization = st.sidebar.checkbox("🧠 Enable lemmatization", value=True)

max_words = st.sidebar.slider("📏 Max words", 20, 300, DEFAULT_MAX_WORDS, 10)
font_size = st.sidebar.slider("🔠 Max font size", 20, 200, DEFAULT_MAX_FONT_SIZE, 10)

# Get theme settings
theme_config = THEMES[theme]
background_color = theme_config["background_color"]
colormap = theme_config["colormap"]


# ------------------------
# Input Section
# ------------------------
text_input = st.text_area(
    "✍️ Paste your text",
    height=200,
    placeholder="Enter at least 20 words..."
)

uploaded_file = st.file_uploader(
    "📂 Upload TXT / PDF / DOCX",
    type=["txt", "pdf", "docx"]
)


# ------------------------
# Get Input Text
# ------------------------
text = read_uploaded_file(uploaded_file) if uploaded_file else text_input.strip()


# ------------------------
# Generate Word Cloud
# ------------------------
if st.button("🚀 Generate Word Cloud"):
    if not text.strip():
        st.error("Please provide text or upload a file.")
    elif len(text.split()) < MIN_WORDS:
        st.warning(f"Please enter at least {MIN_WORDS} words.")
    else:
        # Process text
        tokens = preprocess_text(
            text,
            use_stopwords=use_stopwords,
            use_lemmatization=use_lemmatization
        )
        frequencies = get_word_frequencies(tokens)
        
        # Generate word cloud
        wc = create_wordcloud(
            frequencies,
            background_color=background_color,
            max_words=max_words,
            max_font_size=font_size,
            colormap=colormap
        )
        
        # Render and display
        fig, ax = render_wordcloud(wc)
        
        st.success("Word Cloud Generated!")
        st.pyplot(fig)
        
        # ------------------------
        # Download Image
        # ------------------------
        buf = save_wordcloud_to_buffer(fig)
        st.download_button(
            "💾 Download Word Cloud",
            data=buf,
            file_name="wordcloud.png",
            mime="image/png"
        )
        
        # ------------------------
        # Frequency Table
        # ------------------------
        st.subheader("📊 Word Frequency")
        df = (
            pd.DataFrame(frequencies.items(), columns=["Word", "Frequency"])
            .sort_values("Frequency", ascending=False)
            .head(max_words)
            .reset_index(drop=True)
        )
        st.dataframe(df, use_container_width=True)
