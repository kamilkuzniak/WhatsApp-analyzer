import unittest
import src.chat_analyzer


class TestChat(unittest.TestCase):
    def test_classify_msg(self):
        text = 'some part of chat'
        result = src.chat_analyzer.classify_msg(text)
        self.assertEqual(result, 'some part of chat')

    def test_chat_fix(self):
        text = 'some part of chat'
        result = src.chat_analyzer.chat_fix(text)
        self.assertEqual(result, 'some part of chat')

    def test_remove_nan(self):
        text = 'some part of chat'
        result = src.chat_analyzer.remove_nan(text)
        self.assertEqual(result, 'some part of chat')

    def test_count_words(self):
        text = 'some part of chat'
        result = src.chat_analyzer.count_words(text)
        self.assertEqual(result, 'some part of chat')

# add appropriate parts of the chat file to run the tests
