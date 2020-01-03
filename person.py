import pandas as pd

class Person:
    def __init__(self, name):
        self.name = name
        self.msg_count = 0
        self.word_count = 0
        self.word_avg = 0
        self.top_words = []
        self.media_count = 0

    def count_messages(self, chat_data):
        self.msg_count = chat_data['Person'].value_counts().loc[self.name]

    def calculate_average(self,):
        self.word_avg = round(self.word_count / self.msg_count)

    def count_words(self, chat_data):
        self.word_count = sum(chat_data[(chat_data['Person'] == self.name) & (chat_data['Content'] != '<Media omitted>\n')]['Content'].apply(lambda x: len(x.split())))

    def most_common_words(self, chat_data):
        #join connects all the messages from the chat_data into one huge string that is than lower cased and split into a list of all words that is then cast as a pandas series and value_counts is used on it
        self.top_words = pd.Series(' '.join(chat_data[(chat_data['Person'] == self.name) & (chat_data['Content'] != '<Media omitted>\n')]['Content']).lower().split()).value_counts()[:10]

    def count_media(self, chat_data):
        self.media_count = sum((chat_data['Person'] == self.name) & (chat_data['Content'] == '<Media omitted>\n'))

    def __str__(self):
        return self.name + ' sent: ' + str(self.msg_count) + ' messages and ' + str(self.word_count) +\
            ' words in total\n' + 'Average message length for ' + self.name + ' is: ' + str(self.word_avg) +\
            '\n' + 'Media sent by ' + self.name + ': ' + str(self.media_count) + '\n' + 'Most common words used by ' +\
            self.name + ': \n' + str(self.top_words) + '\n'
