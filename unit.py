# test_chatbot.py

import unittest
from chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_response(self):
        user_input = "Hello, chatbot."
        response = self.chatbot.respond(user_input)
        self.assertEqual(response, "Chatbot Response")

if __name__ == "__main__":
    unittest.main()
