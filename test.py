from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

# Navigate to the chatbot page
driver.get("https://khaanvaani.streamlit.app/")

# Find the input field and send a message
input_field = driver.find_element("id", "chat-input")
input_field.send_keys("Hello, chatbot!")
input_field.send_keys(Keys.RETURN)

# Wait for the response
time.sleep(2)  # Use a better way to wait for the response

# Assert that the response is as expected
response = driver.find_element("id", "chat-response").text
assert response == "Hi there! How can I help you?"

# Close the browser
driver.quit()
