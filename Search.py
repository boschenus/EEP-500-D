
import streamlit as st

import spacy
import numpy as np
from PIL import Image

st.title('Image Search')
st.header('Pass in an input word or even a sentence (e.g. jasmine or mount adams)')
# Load the pre-trained word vectors model (en_core_web_md)
nlp = spacy.load("en_core_web_md")

word_image_mapping = {
    'Flower': 'https://cdn.firstcry.com/education/2022/12/12101916/Flower-Names-In-English-For-Kids.jpg',
    'Vehicle': 'data:image/png;base64,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',
    'Tree': 'data:image/jpeg;base64,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',
    'Mountain': 'data:image/jpeg;base64,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',
    'Building': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsGL4hs8cPjF8OSyC-xNCFuDq1OaAdh2epAIYs9xlCX23AGcNNjtbAMzn6dUn2ZqcLAVg&usqp=CAU'
}
# List of words
word_list = ['Flower', 'Vehicle', 'Tree', 'Mountain', 'Building']

# Function to find the nearest words
def find_nearest_words(input_word, word_list, nlp, top_n=3):

    input_vector = nlp(input_word).vector

    # Calculate cosine similarities
    similarities = [(word, np.dot(input_vector, nlp(word).vector) / (np.linalg.norm(input_vector) * np.linalg.norm(nlp(word).vector)))
                    for word in word_list]

    # Sort words by similarity in descending order
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Get the top N nearest words
    nearest_words = [word for word, similarity in similarities[:top_n]]

    return nearest_words


input_word = st.text_input('Input here')
nearest_words = find_nearest_words(input_word, word_list, nlp)

st.image(Image.open(word_image_mapping[nearest_words[0]]), caption=f"Nearest image to '{input_word}': {nearest_words[0]}")
st.write(f"The nearest words is: {nearest_words[0]}")
