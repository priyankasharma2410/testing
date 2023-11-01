from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (Make sure you have the WebDriver installed and configured)
driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox

# Navigate to the chatbot page
driver.get("https://example.com/chatbot")  # Replace with the URL of your chatbot

# Find the chat input element
chat_input = driver.find_element_by_id("chat-input")  # Replace with the appropriate selector

# Simulate a conversation with the chatbot
chat_input.send_keys("Hello, chatbot. How can you help me today?" + Keys.RETURN)

# Wait for the chatbot to respond (you may need to adjust the waiting time)
driver.implicitly_wait(5)  # Wait for 5 seconds

# Validate the chatbot's response
chatbot_response = driver.find_element_by_id("chatbot-response")  # Replace with the actual selector
expected_response = "I can help you with financial and health questions."
assert expected_response in chatbot_response.text, "Chatbot response doesn't match expected response."

# Continue the conversation
chat_input.send_keys("Tell me about health insurance" + Keys.RETURN)

# Wait for the chatbot to respond
driver.implicitly_wait(5)

# Validate the chatbot's response
chatbot_response = driver.find_element_by_id("chatbot-response")
expected_response = "Health insurance provides coverage for medical expenses."
assert expected_response in chatbot_response.text, "Chatbot response doesn't match expected response."

# Close the browser
driver.quit()

