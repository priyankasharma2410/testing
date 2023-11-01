from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the Selenium WebDriver
driver = webdriver.Chrome(executable_path="path_to_chromedriver.exe")  # Change this to your chromedriver path

# Open the chatbot webpage
driver.get("https://example.com/chatbot")  # Replace with the URL of the chatbot

# Find the chat input element
chat_input = driver.find_element_by_id("chat-input")  # Replace "chat-input" with the actual chat input field ID

# Start a conversation
chat_input.send_keys("Hello, chatbot!")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("chatbot-response")  # Replace with the actual class name of chatbot responses
print("Chatbot: " + response.text)

# Continue the conversation
chat_input.clear()
chat_input.send_keys("How can I use your service?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("chatbot-response")
print("Chatbot: " + response.text)

# You can continue the conversation by repeating the steps above
# ...

# Close the browser when done
driver.quit()
