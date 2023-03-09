from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    button_submit = (By.XPATH, "//button[@type='submit']")
    text_login = (By.XPATH, "//h1[text()='Admin area demo']")
    error_message = (By.XPATH, "//div[contains(@class,'message-error')]")
    email_error_message = (By.XPATH, "//span[@id='Email-error']")