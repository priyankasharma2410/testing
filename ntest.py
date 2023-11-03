from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = "C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver-win64"


# Open the chatbot webpage
base_url ="https://khaanvaani.streamlit.app//"  # Replace with the URL of the chatbot

# Find the chat input field by tag name (input)
chat_input = driver.find_element_by_tag_name("input")

# Start a conversation
chat_input.send_keys("How can I assist you?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response (you may need to adjust the wait time)
driver.implicitly_wait(5)

# Capture the chatbot's response by finding a message element
response = driver.find_element_by_id("st-dc")
print("Chatbot: " + response.text)

# Continue the conversation
chat_input.clear()
chat_input.send_keys("I had an accident in a mining site. What should I do?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response (adjust the wait time)
driver.implicitly_wait(5)

# Capture the chatbot's response
response = driver.find_element_by_id("st-dc")
print("Chatbot: " + response.text)

# You can continue the conversation by repeating the steps above
# ...

# Close the browser when done
driver.quit()
