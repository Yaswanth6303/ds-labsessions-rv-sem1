"""
Word cloud generation utilities.
"""
from typing import Dict
from io import BytesIO

import matplotlib.pyplot as plt
from wordcloud import WordCloud

from config import WORDCLOUD_WIDTH, WORDCLOUD_HEIGHT


def create_wordcloud(
    frequencies: Dict[str, int],
    background_color: str = "white",
    max_words: int = 100,
    max_font_size: int = 120,
    colormap: str = "tab10"
) -> WordCloud:
    """
    Create a WordCloud object from word frequencies.
    
    Args:
        frequencies: Dictionary of word frequencies
        background_color: Background color for the word cloud
        max_words: Maximum number of words to display
        max_font_size: Maximum font size for words
        colormap: Matplotlib colormap name
        
    Returns:
        Generated WordCloud object
    """
    wc = WordCloud(
        width=WORDCLOUD_WIDTH,
        height=WORDCLOUD_HEIGHT,
        background_color=background_color,
        max_words=max_words,
        max_font_size=max_font_size,
        colormap=colormap
    )
    return wc.generate_from_frequencies(frequencies)


def render_wordcloud(wc: WordCloud):
    """
    Render a word cloud as a matplotlib figure.
    
    Args:
        wc: WordCloud object to render
        
    Returns:
        Matplotlib figure and axes
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    return fig, ax


def save_wordcloud_to_buffer(fig) -> BytesIO:
    """
    Save a matplotlib figure to a BytesIO buffer.
    
    Args:
        fig: Matplotlib figure to save
        
    Returns:
        BytesIO buffer containing the PNG image
    """
    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf
