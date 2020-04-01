import pandas as pd
import numpy as np
# used to remove common, useless words and punctuation
from nltk.corpus import stopwords
import string


class Person:
    def __init__(self, name):
        self.name = name
        self.msg_count = 0
        self.word_count = 0
        self.word_avg = 0
        self.top_words = []
        self.media_count = 0
        self.word_count_by_month = []
        self.word_count_by_day = []
        self.word_count_by_hour = []

    def count_messages(self, chat_data):
        """
        Counts the messages of the given person in the chat
        :param chat_data: Dataframe with the messages from the chat
        """
        self.msg_count = chat_data.xs(self.name, level='Person').count()[0]

    def calculate_average(self, ):
        """
        Calculates the average number of words in a message for the given person in the chat
        """
        self.word_avg = round(self.word_count / self.msg_count)

    def count_total_words(self, chat_data):
        """
        Counts the total number of words used by the given person in the chat
        :param chat_data: Dataframe with the messages from the chat
        """
        self.word_count = chat_data.xs(self.name, level='Person')['Word count'].sum()

    # change this because I added the column with the word number in each sentence
    def count_words_by_month_day_hour(self, chat_data):
        """
        Counts the total number of words by month, day and hour used by the given person in the chat
        :param chat_data: Dataframe with the messages from the chat
        """
        self.word_count_by_month = chat_data.loc[2019].xs(self.name, level='Person')['Word count'].groupby(
            'Month').sum()
        self.word_count_by_day = chat_data.loc[2019].xs(self.name, level='Person')['Word count'].groupby('Day').sum()
        self.word_count_by_hour = chat_data.loc[2019].xs(self.name, level='Person')['Word count'].groupby('Hour').sum()

    def most_common_words(self, chat_data):
        """
        Creates a list of 10 most used words used by the given person in the chat
        :param chat_data: Dataframe with the messages from the chat
        """
        # join connects all the messages from the chat_data into one huge string that is than lower cased and split
        # into a list of all words that is then cast as a pandas series and value_counts is used on it
        self.top_words = pd.Series(' '.join(
            chat_data[chat_data['Content'] != '<Media omitted>\n'].xs(self.name, level='Person')[
                'Content']).lower().split())
        # self.top_words = pd.Series(''.join([char for char in self.top_words if char not in string.punctuation]).split())
        self.top_words = self.top_words[np.logical_not(self.top_words.isin(stopwords.words('english')))].value_counts()[
                         :10]

    def count_media(self, chat_data):
        """
        Count all the media sent by the given person in the chat
        :param chat_data: Dataframe with the messages from the chat
        """
        self.media_count = chat_data[chat_data['Content'] == '<Media omitted>\n'].xs(self.name, level='Person').count()[
            0]

    def __str__(self):
        """
        Returns a string of all the information gathered for the given person from the chat
        """
        return self.name + ' sent: ' + str(self.msg_count) + ' messages and ' + str(self.word_count) + \
               ' words in total\n' + 'Average message length for ' + self.name + ' is: ' + str(self.word_avg) + \
               '\n' + 'Media sent by ' + self.name + ': ' + str(
            self.media_count) + '\n' + 'Most common words used by ' + \
               self.name + ': \n' + self.top_words.to_string() + '\n' + '\n'
