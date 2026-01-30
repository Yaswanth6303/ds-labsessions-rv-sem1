"""
Text preprocessing and NLP utilities.
"""
import string
from collections import Counter
from typing import List, Dict

from wordcloud import STOPWORDS
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()


def preprocess_text(
    text: str,
    use_stopwords: bool = True,
    use_lemmatization: bool = True
) -> List[str]:
    """
    Preprocess text by tokenizing, removing punctuation, 
    optionally removing stopwords and lemmatizing.
    
    Args:
        text: Input text to process
        use_stopwords: Whether to remove stopwords
        use_lemmatization: Whether to apply lemmatization
        
    Returns:
        List of processed tokens
    """
    tokens = word_tokenize(text.lower())
    
    # Remove non-alphabetic tokens and punctuation
    tokens = [
        t for t in tokens
        if t.isalpha() and t not in string.punctuation
    ]
    
    # Optionally remove stopwords
    if use_stopwords:
        tokens = [t for t in tokens if t not in STOPWORDS]
    
    # Optionally apply lemmatization
    if use_lemmatization:
        tokens = [lemmatizer.lemmatize(t) for t in tokens]
    
    return tokens


def get_word_frequencies(tokens: List[str]) -> Dict[str, int]:
    """
    Calculate word frequencies from a list of tokens.
    
    Args:
        tokens: List of word tokens
        
    Returns:
        Dictionary mapping words to their frequencies
    """
    return dict(Counter(tokens))
