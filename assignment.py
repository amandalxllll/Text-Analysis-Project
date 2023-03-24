# This code is designed for Assignment 2 (Text Mining Analysis)
import random
import string
import sys
from unicodedata import category
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from sklearn.metrics import SCORERS

nltk.download("vader_lexicon")
from thefuzz import fuzz
import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt


# Part 1: Cleaning the File
def process_file(filename, skip_header=False):
    """
    This process is adapted from session15
    Regenerate book that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    book = {}
    fp = open(filename, encoding="UTF8")

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith("*** END OF THIS PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(
            chr(8212), " "
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            book[word] = book.get(word, 0) + 1

    return book


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith("*** START OF THIS PROJECT"):
            break


# Part2 : Analyzing the Text
stopwords = process_file("stopwords.txt", False)

stopwords = list(stopwords.keys())
# print(stopwords)

# Step1: Computing Summary Statistics
# Includes 3 parts: Counting the total number of words; Counting most common words (excluding the stopwords)
# Counting the most frequent 10 words


# a. Count the Total words
def total_words(book):
    """Returns the total of the frequencies in a book."""
    return sum(book.values())


# b. count the most common words
def most_common(book, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    book: map from word to frequency
    returns: list of (frequency, word) pairs
    """

    res = []
    for word in book:
        if excluding_stopwords:
            if word in stopwords:
                continue
        freq = book[word]

        res.append((freq, word))

    res.sort(reverse=True)

    return res


# c. count the most 10 frequent word in books
def top_10_words(book):
    """
    This sort the dictionary in desceding order and return the top 10 most appeared words in the book.
    """
    t = most_common(book, excluding_stopwords=True)
    result = {}
    for freq, word in t[:10]:
        result[word] = freq
    return result


def top_overlappingwords(book_1, book_2):
    """
    This returnd the overlapping words appeared in top_10 words from two books.
    """
    b1 = top_10_words(book_1)
    b2 = top_10_words(book_2)
    lt = []
    for key in b1:
        if key in b2.keys():
            lt.append(key)
    for key in b2:
        if key in b1.keys():
            lt.append(key)
    list_overlapping = []
    for i in lt:
        if i not in list_overlapping:
            list_overlapping.append(i)
    return list_overlapping


def top_nonoverlappingwords(book_1, book_2):
    """
    This returnd the nonoverlapping words appeared in top_10 words from two books.
    """
    b1 = top_10_words(book_1)
    b2 = top_10_words(book_2)
    lt = []
    for key in b1:
        if key not in b2.keys():
            lt.append(key)
    for key in b2:
        if key not in b1.keys():
            lt.append(key)
    list_nonoverlapping = []
    for i in lt:
        if i not in list_nonoverlapping:
            list_nonoverlapping.append(i)
    return list_nonoverlapping


def count_marr_words(book):
    """
    This returnd the words contaning words with marr: married. marry. marriage. marrying from two books.
    """
    marr_count = 0
    book_string = str(book)
    final_book = book_string.lower()
    for word in final_book.split():
        if "marr" in word:
            marr_count += 1
        elif "mar" in word and len(word) > 4:
            # Check for variations like "marriage", "married", etc.
            marr_count += 1
    return marr_count


# Part 3: Natural Language Processing
def sentiment(book):
    score = SentimentIntensityAnalyzer().polarity_scores(book)
    return score


# Part 4: Text Similarity


def text_similarity(book1, book2):
    result = fuzz.ratio(book1, book2)
    return result


def main():
    je = process_file("janeeyre.txt", skip_header=False)
    lw = process_file("littlewomen.txt", skip_header=False)
    je_nltk = open("janeeyre.txt", "r", encoding="utf-8").read()
    lw_nltk = open("littlewomen.txt", "r", encoding="utf-8").read()

    print(f"The total words in Jane Eyre are {total_words(je)}")
    print(f"The total words in Little Women are {total_words(lw)}")
    print(f"The top 10 words in Jane Eyre are:{top_10_words(je)}")
    print(f"The top 10 words in Little Women are:{top_10_words(lw)}")
    print(
        f"The non-overlapping words in the top 10 common words in two books are:{top_nonoverlappingwords(je, lw)}"
    )
    print(
        f"The overlapping words in the top 10 common words in two books are:{top_overlappingwords(je, lw)}"
    )
    print(
        f"The occurence of words related to marriage in Jane Eyre are {count_marr_words(je)}"
    )
    print(
        f"The occurence of words related to marriage in the Little Women are {count_marr_words(lw)}"
    )
    print(f"The sentiment analysis result of Jane Eyre is{sentiment(je_nltk)}")
    print(f"The sentiment analysis result of the Little Women is{sentiment(lw_nltk)}")
    print(f"The text similarity based in the fuzz ratio is {text_similarity(je,lw)}%")


if __name__ == "__main__":
    main()
