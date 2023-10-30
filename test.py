from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the Selenium WebDriver
driver = webdriver.Chrome(executable_path="Downloads\chromedriver_win32\chromedriver.exe")  # Change this to your chromedriver path

# Open the chatbot webpage
driver.get("https://khaanvaani.streamlit.app/")  # Replace with the URL of the chatbot

# Find the chat input element
chat_input = driver.find_element_by_id("st-bd st-by st-bz st-c0 st-c1 st-c2 st-c3 st-c4 st-c5 st-c6 st-c7 st-b9 st-c8 st-c9 st-ca st-cb st-cc st-cd st-ce st-cf st-ae st-af st-ag st-cg st-ai st-aj st-bx st-ch st-ci st-cj")  # Replace "chat-input" with the actual chat input field ID

# Start a conversation
chat_input.send_keys("Hello, chatbot!")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("msg")  # Replace with the actual class name of chatbot responses
print("Chatbot: " + response.text)

# Continue the conversation
chat_input.clear("hello,How can I assist you?")
chat_input.send_keys("How can I use your service?")
chat_input.send_keys(Keys.RETURN)

# Wait for the chatbot's response
response = driver.find_element_by_class_name("chatbot-response")
print("Chatbot: " + response.text)

# You can continue the conversation by repeating the steps above
# ...

# Close the browser when done
driver.quit()
