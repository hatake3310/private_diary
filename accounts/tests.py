from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver


# Create your tests here.
class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path='C:/Users/hatake/Python/chromedriver_win32/chromedriver.exe')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('batabata@example.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('himi2himi2')
        self.selenium.find_element_by_class_name('btn').click()

        self.assertEqual('日記一覧|Private Diary', self.selenium.title)
