import unittest
import src.person.person


class TestPerson(unittest.TestCase):
    def test_count_messages(self):
        text = 'some part of chat'
        result = src.person.person.count_messages(text)
        self.assertEqual(result, 'some part of chat')

    def test_calculate_average(self):
        text = 'some part of chat'
        result = src.person.person.calculate_average(text)
        self.assertEqual(result, 'some part of chat')

    def test_count_total_words(self):
        text = 'some part of chat'
        result = src.person.person.count_total_words(text)
        self.assertEqual(result, 'some part of chat')

    def test_count_words_by_month_day_hour(self):
        text = 'some part of chat'
        result = src.person.person.count_words_by_month_day_hour(text)
        self.assertEqual(result, 'some part of chat')

    def test_most_common_words(self):
        text = 'some part of chat'
        result = src.person.person.most_common_words(text)
        self.assertEqual(result, 'some part of chat')

    def test_count_media(self):
        text = 'some part of chat'
        result = src.person.person.count_media(text)
        self.assertEqual(result, 'some part of chat')

# add appropriate parts of the chat file to run the tests