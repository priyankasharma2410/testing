from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
chrome_driver_path = 'C:\\Users\\91881\\Desktop\\sih\\product development\\chromedriver-win64\\chromedriver.exe'
# Initialize the Chrome WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Define the base URL
base_url = "https://www.dominos.co.in"

# Open the website
driver.get(base_url)

# Find and click on an element using its XPath
driver.find_element(By.XPATH, "//*[@id='ymPluginDivContainerInitial']//img").click()

# Create a WebDriverWait instance
wait = WebDriverWait(driver, 60)

# Wait for the presence of an element
wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(),'Stores near me')]")))

# Find and click on the element
driver.find_element(By.XPATH, "//strong[contains(text(),'Stores near me')]").click()

print("Found the button, clicked on that...")

# Close the browser
driver.close()

# Exit the script
driver.quit()
