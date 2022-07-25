"""This program will take a string of words and determine its word sentiment.

Author: Thomas Brickhouse
Version: 4/1/2022
"""


import string
from review import Review


class SentimentAnalyzer:
    """Class for calculating a strings word sentiment.

    Attributes:
        review_counts (dict): A dictionary for mapping from individual words
                              to a count of the total number of reviews that
                              contain those words.
        word_rating_totals (dict): A dictionary for  mapping from individual
                                   words to the sum of the ratings of all
                                   reviews that contain that word.
        reviews (list): A list with all the Review objects called in
                        the add_review or load_review method.

    """

    def __init__(self):
        """Intialize the dictionaries and a list needed to record data."""
        self.review_counts = {}
        self.word_rating_totals = {}
        self.reviews = []

    def add_review(self, a_review):
        """Update the constroctors using the info provided.

        This method takes a review and adds to the the reviews list
        as well as updates review_counts and word_rating_totals with
        the info provided in a_review.

        Args:
            a_review (Review): A line from a file that will be added to various
                               dictionaries and lists

        """
        self.reviews.append(a_review)
        for word in a_review.words:
            if word in self.review_counts.keys():
                self.review_counts[word] = self.review_counts.get(word) + 1
            else:
                self.review_counts[word] = 1
        review_rating = a_review.rating
        for word in a_review.words:
            if word in self.word_rating_totals:
                self.word_rating_totals[word] = (
                    (self.word_rating_totals.get(word) + review_rating))

            else:
                self.word_rating_totals[word] = review_rating

    def load_reviews(self, file_name):
        """Read all the reviews from the given file.

        Args:
            file_name (str): The file name to load reviews from.

        """
        infile = open(file_name, "r")
        movie_lines = infile.readlines()
        for line in movie_lines:
            self.add_review(Review(line))
        infile.close()

    def save_reviews(self, file_name):
        """Save the reviews in the reviews list to the given file name.

        Args:
            file_name (str): The file name to save the reviews to.

        """
        out_file = open(file_name, "w")
        for line in self.reviews:
            out_file.write(str(line))
        out_file.close()

    def word_sentiment(self, word):
        """Return the word sentiment for the provided word.

        Args:
            word (str): A word.

        Returns:
            float: The word sentiment score. Will return 2.0 if the word does
                   not have a score.

        """
        if word in self.word_rating_totals:
            return (self.word_rating_totals.get(word) /
                    self.review_counts.get(word))
        else:
            return(2.0)

    def analyze(self, sentance):
        """Take a string and return the average sentiment value including repeats.

        Args:
            sentance (str): An arbitrary sting of text.

        Returns:
            float: The average sentiment score.

        """
        score_list = []
        if len(sentance) != 0:
            words_lowercase = sentance.lower()
            punc_sentance = (words_lowercase.translate
                             (str.maketrans('', '', string.punctuation)))
            for word in punc_sentance.split():
                score = self.word_sentiment(word)
                score_list.append(score)
            return sum(score_list) / len(score_list)
