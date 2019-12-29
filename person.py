class Person:
    def __init__(self, name):
        self.name = name
        self.msg_count = 0
        self.word_count = 0
        self.word_avg = 0

    def calculate_average(self,):
        self.word_avg = round(self.word_count / self.msg_count)

    def __str__(self):
        return self.name + ' sent: ' + str(self.msg_count) + ' messages and ' + str(self.word_count) +\
        ' words in total\n' + 'Average message length for ' + self.name + ' is: ' + str(self.word_avg) + '\n'

