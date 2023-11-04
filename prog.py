from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe"  # Update with the actual path to ChromeDriver

# Initialize the Chrome WebDriver with the specified executable path
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to a search engine (e.g., Google)
driver.get("https://www.google.com")

# Find the search input field by name (for Google, it's "q")
search_input = driver.find_element_by_name("q")

# Type a search query into the input field
search_input.send_keys("Python programming")
search_input.send_keys(Keys.RETURN)  # Press Enter to perform the search

# Wait for the search results to load (you may need to adjust the wait time)
driver.implicitly_wait(5)

# Print the title of the search results page
print("Search results title:", driver.title)

# Close the browser when done
driver.quit()
