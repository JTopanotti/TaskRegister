from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from datetime import datetime


class RedmineDriver():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self, username, password):
        #load login screen
        self.driver.get("http://apps.substractum.com.br/redmine")
        self.driver.find_element_by_link_text("Sign in").click()
        # first_result = wait.until(presence_of_element_located((By.ID, "login-form")))

        #insert login creds
        #TODO pass creds to .env file
        self.driver.find_element_by_id("username").send_keys(username.strip())
        self.driver.find_element_by_id("password").send_keys(password.strip())
        self.driver.find_element_by_id("login-submit").click()

    def register_task(self, time, comment, task, date):
        wait = WebDriverWait(self.driver, 10)

        #find task
        self.driver.find_element_by_class_name("projects").click()
        self.driver.find_element_by_id("q").send_keys(task.strip() + Keys.ENTER)
        ele = wait.until(presence_of_element_located((By.LINK_TEXT, "Tempo de trabalho")))
        ele.click()

        #insert task info and save
        date_element = self.driver.find_element_by_id("time_entry_spent_on")
        date_str = datetime.strptime(date, "%Y-%m-%d").strftime("%m%d%Y")
        ActionChains(self.driver).move_to_element(date_element).click().send_keys(date_str).perform()
        self.driver.find_element_by_id("time_entry_hours").send_keys(time.strip())
        self.driver.find_element_by_id("time_entry_comments").send_keys(comment.strip())
        self.driver.find_element_by_name("commit").click()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    driver = RedmineDriver()
    driver.login()
    driver.register_task("00:50", "Modificação EncerraSalaChat", "14464", datetime.fromisoformat('2021-01-19'))