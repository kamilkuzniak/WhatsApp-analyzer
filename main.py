from person import Person
import datetime
import pandas as pd



def gettime(time):
    time_split = time.split(':')

    hour = int(time_split[0])
    minute = int(time_split[1])

    return datetime.time(hour, minute)


def getdate(date):
    date_split = date.split('/')

    year = int('20' + date_split[2])
    month = int(date_split[1])
    day = int(date_split[0])

    return datetime.date(year, month, day).ctime()

with open('WhatsApp Chat with Sara.txt', 'r') as chat:
    #maybe more complex reading with some if statements
    messages = chat.readlines()
    #messages = []
    #for line in chat.readlines():
        #messages.append(line)

    names = []
    dates = []
    #This loop finds the names of all the people in the chat
    #100 put there for now, until I figure out the issue with file reading
    for line in messages[1:100]:
        if '-' in line:
            name = line.split('-')[1].split()[0].replace(':', '')
            dates.append(line.split('-')[0])
            if name not in names:
                names.append(name)
    #there are messages in which a person used enter which created a new line, that screws up the name search and message and word count
    people = []

    #This loop creates a person object for each person participating in the chat
    for name in names:
        people.append(Person(name))

    for person in people:
        for line in messages:
            if person.name in line:
                person.msg_count += 1
                person.word_count += len(line.split(':')[-1].split())
        person.calculate_average()
        print(person)

    #print('Kamil sent ' + str(round((1 - kamil_msg/sara_msg)*100)) + '% less messages than Sara')
    #print('Kamil sent ' + str(round((1 - kamil_words / sara_words) * 100)) + '% less words than Sara')

#if __name__ == '__main__':
