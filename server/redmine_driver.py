from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from pymongo import MongoClient
from pprint import pprint


class RedmineDriver():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self, username, password):
        #load login screen
        self.driver.get("http://apps.substractum.com.br/redmine")
        self.driver.find_element_by_link_text("Sign in").click()

        #insert login creds
        self.driver.find_element_by_id("username").send_keys(username.strip())
        self.driver.find_element_by_id("password").send_keys(password.strip())
        self.driver.find_element_by_id("login-submit").click()

    def register_task(self, time, comment, task, date):
        wait = WebDriverWait(self.driver, 10)

        #find task
        self.driver.find_element_by_class_name("projects").click()
        self.driver.find_element_by_id("q").send_keys(task + Keys.ENTER)
        ele = wait.until(presence_of_element_located((By.LINK_TEXT, "Tempo de trabalho")))
        ele.click()

        #insert task info and save
        date_element = self.driver.find_element_by_id("time_entry_spent_on")
        ActionChains(self.driver).move_to_element(date_element).click().send_keys(date.strftime("%m%d%Y")).perform()
        self.driver.find_element_by_id("time_entry_hours").send_keys(time)
        self.driver.find_element_by_id("time_entry_comments").send_keys(comment)
        self.driver.find_element_by_name("commit").click()

    def syncronize_tasks_mongo(self, connection_str, tasks):
        print(connection_str)
        if connection_str is not None:
            client = MongoClient(connection_str)
            collection = client.taskregister.tasks
            results = collection.insert_many(tasks)
            print("Tasks syncronized!")
        

    def close(self):
        self.driver.close()