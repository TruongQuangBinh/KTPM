import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://shopee.vn/buyer/login?next=https%3A%2F%2Fshopee.vn%2F")
        self.assertIn('Đăng nhập tài khoản - Mua sắm Online | Shopee Việt Nam', driver.title)
        username = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div/div/form/div/div[2]/div[2]/div[1]/input")
        username.send_keys("quangbinh1245@gmail.com")
        password = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div/div/form/div/div[2]/div[3]/div[1]/input")
        password.send_keys("016970605644")
        btn = driver.find_element(By.XPATH, "//*[@id=\"main\"]/div/div[2]/div/div/form/div/div[2]/button")
        btn.click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
