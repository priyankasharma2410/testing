
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # You can use a different browser driver if needed
driver.get("https://khaanvaani.streamlit.app/")  # Replace with the URL of your web application

# Find the chatbot input element
chatbot_input = driver.find_element("your-selector-strategy", "your-selector-value")

# Interact with the chatbot
chatbot_input.send_keys("Hello, how are you?")
chatbot_input.send_keys(Keys.RETURN)  # Press Enter key

# Wait for the chatbot response
time.sleep(2)  # Use WebDriverWait for a more robust solution

# Retrieve and assert the chatbot response
chatbot_response = driver.find_element("your-selector-strategy", "your-selector-value").text
assert "Expected response" in chatbot_response

# Close the browser
driver.quit()
