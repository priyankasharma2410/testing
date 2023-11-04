from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (e.g., Chrome WebDriver)
driver = "C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe"

# Navigate to a website
webpage_url = "https://khaanvaani.streamlit.app/"

# Find the first <input> element on the page by tag name
chat_input  = "C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe"

# Perform actions on the input element
chat_input.send_keys("Your message")  # You can send text to the input element

# You can also submit the form, if applicable
chat_input.submit()

# Close the browser when done
driver.quit()
