from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome web driver
driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe")

# Open the chatbot web page
driver.get("https://your-chatbot-website.com")

# Wait for the chatbot to load
time.sleep(3)

# Find the chat input field and send a message
chat_input = driver.find_element_by_css_selector("your-chat-input-css-selector")
chat_input.send_keys("Hello, chatbot!")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot to respond
time.sleep(3)

# Find the chatbot response element
chatbot_response = driver.find_element_by_css_selector("your-chatbot-response-css-selector")

# Validate the chatbot's response
expected_response = "Hi there! How can I assist you today?"
if expected_response in chatbot_response.text:
    print("Test Passed: Chatbot response is as expected")
else:
    print(f"Test Failed: Expected '{expected_response}', but got '{chatbot_response.text}'")

# Close the browser
driver.quit()
