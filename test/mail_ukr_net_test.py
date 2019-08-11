import re
import time
import unittest
import configparser
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.login_page import Login_page
from src.pages.create_page import Create_mail
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.utils.random_data import Random_data

class Test(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_first(self):
        global action, theme, text, create_email
        wdriver = self.driver
        parser = configparser.ConfigParser()
        parser.read('simple_config.ini')
        url = parser.get('data', 'url')
        user_name = parser.get('data', 'username')
        password = parser.get('data', 'password')

        # Login to mailbox form
        wdriver.get(url)
        login_field = wdriver.find_element_by_xpath(Login_page.login_field)
        login_field.send_keys(user_name)
        password_field = wdriver.find_element_by_xpath(Login_page.password_field)
        password_field.send_keys(password)
        button_login = wdriver.find_element_by_xpath(Login_page.button_login)
        button_login.click()
        try:
            elem = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, Login_page.user_mail)))
        except TimeoutException:
            print "No found element"
        user_mail = wdriver.find_element_by_xpath(Login_page.user_mail)
        print(user_mail.text)
        assert user_mail.text == Create_mail.expected_name

        # Create e-mail
        for i in range(len(Random_data.randoms_a)):
            theme = Random_data.randoms_a[i]
            text = Random_data.randoms_b[i]

            wdriver.find_element_by_xpath(Create_mail.create_button).click()
            wdriver.find_element_by_xpath(Create_mail.fild_input).send_keys(Create_mail.expected_name)
            wdriver.find_element_by_xpath(Create_mail.fild_subject).send_keys(theme)
            action = ActionChains(wdriver).send_keys(Keys.TAB).send_keys(text).perform()
            wdriver.find_element_by_xpath(Create_mail.submit_button).click()
            try:
                elem = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, Create_mail.default_button)))
                print "Page is ready!"
            except TimeoutException:
                print "Mail not create!"
            action = ActionChains(wdriver).send_keys(Keys.TAB).send_keys(Keys.TAB).perform()
            action = ActionChains(wdriver).send_keys(Keys.ENTER).perform()

        # Collect E-mail
        wdriver.find_element_by_xpath(Create_mail.in_mail_box).click()
        dicts = {}
        dicts.clear()
        content = wdriver.find_elements(By.XPATH, Create_mail.content_fild)

        for i in range(len(content)):
            regex1 = r"^\w{1,10}"
            regex2 = r"\s\w{1,10}"

            key = re.search(regex1, content[i].text)
            value = re.search(regex2, content[i].text)

            d = {key.group(0): value.group(0)}
            dicts.update(d)
        print ("Full dict:")
        print (dicts)

        # Create final e-mail
        email_text = ""
        for i in range(len(Random_data.randoms_a)):
            messege_theme = Random_data.randoms_a[i]
            messege_text = dicts.setdefault(messege_theme)
            line_output = messege_theme + str(messege_text)
            regex3 = r"[A-Za-z]"
            regex4 = r"[0-9]"
            letters = re.findall(regex3, line_output)
            numbers = re.findall(regex4, line_output)
            n_letters = len(letters)
            n_numbers = len(numbers)
            string1 = "Received mail on theme " + str(messege_theme) + " with message" + str(messege_text) + "."
            string2 = "It contains " + str(n_letters) + " letters and " + str(n_numbers) + " numbers"
            string = string1 + "\n" + string2
            email_text = email_text + '\n' + string

        wdriver.find_element_by_xpath(Create_mail.create_button).click()
        wdriver.find_element_by_xpath(Create_mail.fild_input).send_keys(Create_mail.expected_name)
        wdriver.find_element_by_xpath(Create_mail.fild_subject).send_keys("mail")
        action = ActionChains(wdriver).send_keys(Keys.TAB).send_keys(email_text).perform()
        wdriver.find_element_by_xpath(Create_mail.submit_button).click()
        try:
            elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Create_mail.default_button)))
            print "Page is ready!"
        except TimeoutException:
            print "Mail not create!"
        wdriver.find_element_by_xpath(Create_mail.action_button).click()

        # Delete mails
        for i in range(15):
            row_checks = wdriver.find_elements_by_xpath(Create_mail.row_check)
            row_checks[i+1].click()
        delete_button = wdriver.find_element_by_xpath(Create_mail.delete_button)
        delete_button.click()

    def tear_down(self):
        self.driver.quit()

if __name__ == "__main__":
        unittest.main()
