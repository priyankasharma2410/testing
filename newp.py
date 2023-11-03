import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Get the ChromeDriver executable path
#driver_path = ChromeDriverManager().install()

# Initialize a ChromeDriver instance with the obtained path
#driver = webdriver.Chrome(executable_path=driver_path)

# Your Selenium tests go here

# Close the driver when you're done


class ChatbotTest(unittest.TestCase):
    def setUp(self):
        # Initialize the Selenium WebDriver (you may need to specify the driver executable path)
        driver = webdriver.Chrome(executable_path=r"C:\Users\91881\Desktop\sih\product development\chromedriver-win64\chromedriver-win64")
      
        self.driver.get("https://khaanvaani.streamlit.app/")

    def test_chatbot_interaction(self):
        # Locate the chatbot input element
        input_element = self.driver.find_element_by_id("chatbot-input")

        # Simulate a conversation with the chatbot
        input_element.send_keys("Hello, chatbot")
        input_element.send_keys(Keys.RETURN)

        # You can add assertions to check the chatbot's responses or other elements on the page
        chatbot_response = self.driver.find_element_by_id("chatbot-response").text
        self.assertIn("Hello! How can I assist you?", chatbot_response)

    def tearDown(self):
        # Clean up and close the WebDriver
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
