"""File containing a review class to format a review.

Author: Thomas Brickhouse
Version: 4/21/22
"""
import string


class Review:
    """A review class to format movie reviews."""

    def __init__(self, *args):
        """Intialize the instance vairables rating and text.

        Intializes the variables rating and text based on how many
        arguments are passed through. If 2 arguments are passed through,
        it seperates the first position to be an interger value rating and
        the second position to be a string. If 1 argument is passed through,
        it takes the first position in the string and sets its value to be an
        integer, and the rest to a string. Then no matter how many arguments are
        passed through, it takes the string and creates a set and sets that equal
        to the instance variable words.

        Args:
            args (str): Somthing

        """
        if len(args) == 2:
            self.rating = args[0]
            self.text = args[1]
            words_lowercase = self.text.lower()
            words_punc = (words_lowercase.translate
                          (str.maketrans('', '', string.punctuation)))
            self.words = words_punc.split()
            self.words = set(self.words)

        elif len(args) == 1:
            self.text = args[0]
            self.rating = int(self.text[0])
            self.text = self.text[2:]
            words_lowercase = self.text.lower()
            words_punc = (words_lowercase.translate
                          (str.maketrans('', '', string.punctuation)))
            self.words = words_punc.split()
            self.words = set(self.words)

    def __str__(self):
        """Format the text to appear in a readable mannor.

        Takes the rating and text and format it into a readable
        string. If the string is over 70 characters it cuts it off
        at 67 characters and adds an ellipses. If the string is
        shorter than 70, it only returns the string itself.

        Returns:
            str: A formatted string with the rating and text.

        """
        sentance = (f'{self.rating} {self.text}')
        if len(sentance) > 70:
            sentance = sentance[0:67]
            return (f'{sentance}...')
        else:
            return sentance

    def __eq__(self, other):
        """Determine if the reviews have the same rating and text.

        Args:
            other (str): The other case to compare the rating and
                         texct to.

        Returns:
            bool: Returns a value if the method is true or false.

        """
        return (isinstance(other, Review) and
                (self.text == other.text and self.rating == other.rating))
