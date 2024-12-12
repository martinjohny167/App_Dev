from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure ChromeDriver is in your PATH

try:
    # 1. Open the application
    driver.get("http://127.0.0.1:8000/")  # Replace with your app URL
    driver.maximize_window()

    # Test 1: Check if the login form loads and works
    print("Testing Login Form...")
    login_url = "http://127.0.0.1:8000/login/"  # Adjust this if necessary
    driver.get(login_url)

    # Find the username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # Enter login details
    username_field.send_keys("testuser")
    password_field.send_keys("testpassword")
    password_field.send_keys(Keys.RETURN)

    # Validate successful login by checking the redirected page or user menu
    time.sleep(2)
    assert "Dashboard" in driver.page_source, "Login failed or Dashboard not found!"

    # Test 2: Navigation Test
    print("Testing Navigation...")
    nav_link = driver.find_element(By.LINK_TEXT, "Employee")  # Adjust link text as needed
    nav_link.click()
    time.sleep(2)
    assert "Employee List" in driver.title, "Navigation to Employee page failed!"

    # Test 3: Form Submission
    print("Testing Form Submission...")
    add_employee_url = "http://127.0.0.1:8000/employee/add/"  # Adjust this if necessary
    driver.get(add_employee_url)

    # Fill out the form
    name_field = driver.find_element(By.NAME, "name")
    role_field = driver.find_element(By.NAME, "role")
    name_field.send_keys("John Doe")
    role_field.send_keys("Manager")
    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()

    # Validate successful submission
    time.sleep(2)
    assert "Employee added successfully" in driver.page_source, "Form submission failed!"

finally:
    # Close the WebDriver
    driver.quit()
