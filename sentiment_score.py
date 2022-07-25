"""Program fro prompting the user to enter text for sentiment analysis.

Author: Thomas Brickhouse
Version: 5/1/2022
"""


from sentiment_analyzer import SentimentAnalyzer
import sys


if __name__ == "__main__":
    sentiment_analyzer = SentimentAnalyzer()
    sentiment_analyzer.load_reviews("movie_reviews.txt")
    repeat = True
    while repeat:
        sentance = input("Enter your text (blank to exit): ")
        result = sentiment_analyzer.analyze(sentance)
        if result:
            print(f'The sentiment score for this text is: {result:.2f}')
            if result < 1.95:
                print("This text is NEGATIVE.\n")
            if 1.95 <= result < 2.05:
                print("This text is NEUTRAL.\n")
            if result >= 2.05:
                print("This text is POSITIVE.\n")
        else:
            repeat = False
