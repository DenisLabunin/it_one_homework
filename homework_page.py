import time
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TodoPage(BasePage):

    DOJOLINK = (By.XPATH, '//span[text()="Dojo"]')
    NEW_TODO = (By.XPATH, '//input[@class="new-todo"]')
    TODO = (By.XPATH, '//ul[@class ="todo-list"]//li//label')

    def follow_the_link(self):
        self.wait.until(EC.visibility_of_element_located(self.DOJOLINK)).click()

    def create_new_todo(self, todo_name: str):
        todo = self.wait.until(EC.visibility_of_element_located(self.NEW_TODO))
        todo.send_keys(todo_name)
        todo.send_keys(Keys.ENTER)

    def change_todo(self, new_todo_name: str):
        todo = self.wait.until(EC.visibility_of_element_located(self.TODO))
        length_todo = len(todo.text)
        action = ActionChains(self.browser)
        action.double_click(todo).perform()
        todo = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//ul[@class ="todo-list"]//li//input[@class="edit"]')))
        action.send_keys_to_element(todo, Keys.BACKSPACE * length_todo).send_keys_to_element(
            todo, new_todo_name).perform()
        todo.send_keys(Keys.ENTER)

    def delete_todo(self):
        delete_button = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//ul[@class ="todo-list"]//li//button')))
        delete_button.click()
