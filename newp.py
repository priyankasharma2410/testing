import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ChatbotTest(unittest.TestCase):
    def setUp(self):
        # Initialize the Selenium WebDriver
        
        self.driver='C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe'

     #   self.driver = webdriver.Chrome(executable_path=r"C:\Users\91881\Desktop\sih\product development\chromedriver-win64\chromedriver.exe")
        base_url = "https://khaanvaani.streamlit.app/" 
        
        self.driver.get('base_url')

    def test_chatbot_interaction(self):
        input_element.send_keys("Hello, chatbot")
        input_element.send_keys(Keys.RETURN)

        # You can add assertions to check the chatbot's responses or other elements on the page
        chatbot_response = self.driver.find_element_by_id("chatbot-response").text
        self.assertIn("Hello! How can I assist you?", chatbot_response)

    def tearDown(self):
        # Clean up and close the WebDriver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
