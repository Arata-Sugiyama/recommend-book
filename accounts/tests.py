from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium import webdriver


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Safari()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('https://arata2412.pythonanywhere.com/' + str(reverse_lazy('account_login')))

        # ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys('2cbmf6m@macr2.com')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('sample0618')
        self.selenium.find_element_by_class_name('btn').click()

        # ページタイトルの検証
        self.assertEquals('Log In | Recommend Book', self.selenium.title)
