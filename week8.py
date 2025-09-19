# ========================
# Part 1: Data Loading and Basic Exploration
# ========================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

# Load dataset
df = pd.read_csv("metadata.csv")

# Basic exploration
print("Shape of dataset:", df.shape)
print("\nData Info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum().head(15))  # check first 15 cols
print("\nSummary statistics:")
print(df.describe())
print("\nFirst few rows:")
print(df.head())

# ========================
# Part 2: Data Cleaning and Preparation
# ========================

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year for analysis
df['year'] = df['publish_time'].dt.year

# Handle missing values
# Example: drop rows with missing title or publish_time
df_clean = df.dropna(subset=['title', 'publish_time'])

# Create a new feature: abstract word count
df_clean['abstract_word_count'] = df_clean['abstract'].fillna("").apply(lambda x: len(x.split()))

print("Cleaned dataset shape:", df_clean.shape)

# ========================
# Part 3: Data Analysis and Visualization
# ========================

# Count publications per year
year_counts = df_clean['year'].value_counts().sort_index()

# Top journals
top_journals = df_clean['journal'].value_counts().head(10)

# Word frequency in titles
from collections import Counter
import re

def clean_text(text):
    text = re.sub(r"[^a-zA-Z ]", "", str(text))
    return text.lower().split()

title_words = df_clean['title'].dropna().apply(clean_text)
all_words = [word for words in title_words for word in words]
common_words = Counter(all_words).most_common(20)

# ---- Visualizations ----

# Publications per year
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Top journals
plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.tight_layout()
plt.show()

# Word cloud of titles
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(all_words))
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.show()

# ========================
# Part 4: Streamlit Application
# ========================

def run_app():
    st.title("CORD-19 Data Explorer")
    st.write("Simple exploration of COVID-19 research papers")

    # Sidebar filter
    year_range = st.slider("Select year range", int(df_clean['year'].min()), int(df_clean['year'].max()), (2020, 2021))
    
    # Filter data
    filtered = df_clean[(df_clean['year'] >= year_range[0]) & (df_clean['year'] <= year_range[1])]
    
    st.write(f"Number of papers: {filtered.shape[0]}")
    st.dataframe(filtered[['title','journal','publish_time']].head(10))

    # Plot: Publications per year
    year_counts = filtered['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
    ax.set_title("Publications by Year")
    st.pyplot(fig)

    # Plot: Top journals
    top_journals = filtered['journal'].value_counts().head(10)
    fig2, ax2 = plt.subplots()
    sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax2)
    ax2.set_title("Top 10 Journals")
    st.pyplot(fig2)

    # Word cloud
    all_words = " ".join(filtered['title'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_words)
    fig3, ax3 = plt.subplots()
    ax3.imshow(wordcloud, interpolation="bilinear")
    ax3.axis("off")
    ax3.set_title("Word Cloud of Titles")
    st.pyplot(fig3)

# Uncomment this when running with Streamlit
# if __name__ == "__main__":
#     run_app()

# ========================
# Part 5: Documentation and Reflection
# ========================
# - Document insights in a separate report or Jupyter notebook
# - Add comments explaining code
# - Reflect on challenges faced (large dataset size, missing data, etc.)
