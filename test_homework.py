from homework_page import TodoPage


URL = 'https://todomvc.com'


class TestWebSite:

    def test_create_todo(self, browser):
        self.homework_page = TodoPage(browser)
        self.homework_page.open(URL)
        self.homework_page.follow_the_link()
        self.homework_page.create_new_todo('some task')

    def test_create_and_change_todo(self, browser):
        self.homework_page = TodoPage(browser)
        self.homework_page.open(URL)
        self.homework_page.follow_the_link()
        self.homework_page.create_new_todo('some task')
        self.homework_page.change_todo('new name for the task')

    def test_create_and_change_and_delete_todo(self, browser):
        self.homework_page = TodoPage(browser)
        self.homework_page.open(URL)
        self.homework_page.follow_the_link()
        self.homework_page.create_new_todo('some task')
        self.homework_page.change_todo('new name for the task')
        self.homework_page.delete_todo()
