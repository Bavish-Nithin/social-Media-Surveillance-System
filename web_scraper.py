from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create webdriver object
driver = webdriver.Firefox()

# open the login page
driver.get("https://x.com/i/flow/login")

# wait for the input element to be present and send keys
element = WebDriverWait(driver, 10).until(  
    EC.presence_of_element_located((By.CSS_SELECTOR, ".r-30o5oe"))
) #oombu
element.send_keys("8072828653")

# Handle potential popup
try:
    close_popup = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-175oi2r"))  # Replace with actual popup close button's selector
    )
    close_popup.click()
except:
    print("No popup or could not close popup")

# wait for the login button to be clickable and then click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3"))
)

# Ensure the login button is visible
driver.execute_script("arguments[0].scrollIntoView(true);", login_button)

# Attempt to click the login button
try:
    login_button.click()
except ElementClickInterceptedException:
    print("Element click intercepted; attempting to close any overlays.")
    # Try clicking again after handling any possible obstructions
    try:
        close_popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-175oi2r"))  # Update selector if needed
        )
        close_popup.click()
        login_button.click()
    except:
        print("Failed to click login after multiple attempts.")
