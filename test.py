
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe"  # Update with the actual path to ChromeDriver

# Initialize the Chrome WebDriver with the specified executable path
driver = webdriver.Chrome(executable_path=chrome_driver_path)



# Navigate to a website
webpage_url = "https://khaanvaani.streamlit.app/"
driver.get(webpage_url)

# Find the first <input> element on the page by tag name
chat_input = driver.find_element(By.TAG_NAME, "input")

# Perform actions on the input element
chat_input.send_keys("Your message")  # You can send text to the input element

# You can also submit the form, if applicable
chat_input.submit()

# Close the browser when done
driver.quit()
