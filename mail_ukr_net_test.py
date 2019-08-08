import re
import string
import unittest
from itertools import islice, imap, repeat
from os import urandom
from telnetlib import EC

import configparser
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import Login_page
from pages.create_page import Create_mail
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



class Test(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)

    def test_first(self):
        global action
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
        wdriver.implicitly_wait(10)
        user_mail = wdriver.find_element_by_xpath(Login_page.user_mail)
        print(user_mail.text)
        assert user_mail.text == Create_mail.expected_name

        # Create e-mail
        a = [rand_string(10) for x in range(0, 5)]
        b = [rand_string(10) for x in range(0, 5)]
        #b = [Random_data.rand_string(10) for x in range(0, 15)]
        for i in range(len(a)):
            theme = a[i]
            text = b[i]

            wdriver.find_element_by_xpath(Create_mail.create_button).click()
            wdriver.find_element_by_xpath(Create_mail.fild_input).send_keys(Create_mail.expected_name)
            wdriver.find_element_by_xpath(Create_mail.fild_subject).send_keys(theme)

            action = ActionChains(wdriver).send_keys(Keys.TAB).send_keys(text).perform()

            wdriver.find_element_by_xpath(Create_mail.submit_button).click()
            wdriver.find_element_by_xpath("//a[@id='0']/span[4]").click()
            #wdriver.find_element_by_xpath("//input[@name='subject']").click()
            #wdriver.implicitly_wait(10)
            id = "msglist_rows"
            re.findall()

            regex = "(msg | [0 - 9]{20})"
            d = [re.findall(regex, text)]


        # Find e-mail
        #c = [wdriver.find_element_by_css_selector("a.msglist__row_href") for x in range(0, 15)]
        for i in range(len(a)):
            theme = a[i]
            WebDriverWait(self.driver, 900).until(
                EC.text_to_be_present_in_element((By.XPATH, "//span[contains(text(),theme)]"),
                                                 "No data to display"))

            #wait = WebDriverWait(self)
            #wait.until(expected_conditions.title_contains(("Sign up")))
            #elements = wdriver.find_elements_by_xpath("//*[text()=theme]")
            #print(elem.text)
            #assert elements.text == id111111

    def tear_down(self):
        self.driver.quit()

def rand_string(self):
        chars = set(string.ascii_uppercase + string.digits)
        char_gen = (c for c in imap(urandom, repeat(1)) if c in chars)
        return ''.join(islice(char_gen, 10))
        pass


if __name__ == "__main__":
        unittest.main()

        #, id = "ID_109"