import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the ChromeDriver executable
driver = webdriver.Chrome()

# Set window size (optional)
driver.set_window_size(1400, driver.get_window_rect()['height'])

# Open the website
driver.get('https://free-proxy-list.net/#')
time.sleep(1)
try:
    # Wait for the div element to be present
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="text-center"]'))
    )

    # Click on the anchor element
    raw_list_link = div_element.find_element(By.XPATH, './/a[@title="Get raw list"]')
    raw_list_link.click()

    # Switch to the modal dialog
    modal_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="modal-body"]'))
    )

    # Find the textarea element within the modal body
    textarea = modal_body.find_element(By.XPATH, './/textarea[@class="form-control"]')

    # Get the text from the textarea
    textarea_text = textarea.get_attribute('value')

    # Specify the file path where you want to save the text
    file_path = 'proxy_data.txt'

    # Save the text to a text file
    with open(file_path, 'w') as file:
        file.write(textarea_text)

    # Switch back to the default content
    driver.switch_to.default_content()

except Exception as e:
    # Handle any exceptions here or simply ignore them
    print("An error occurred:", e)

# Close the browser
driver.quit()
