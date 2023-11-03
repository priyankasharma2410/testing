from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set the path to the ChromeDriver executable
chrome_driver_path = 'C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe'

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open the chatbot webpage
base_url = "https://khaanvaani.streamlit.app/"  # Replace with the URL of the chatbot

# Navigate to the chatbot's webpage
driver.get(base_url)

# Find the chat input field by class name
chat_input = driver.find_element_by_class_name('st-c0')

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
