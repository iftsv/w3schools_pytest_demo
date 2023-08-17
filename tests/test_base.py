import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.chrome.options import Options as FirefoxOptions


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    web_driver = None

    @pytest.fixture(params=["chrome"], scope='class')
    def init_driver(self, request):
        if request.param == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--log-level=3")
            # self.web_driver = webdriver.Chrome(options=chrome_options)
            self.web_driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=chrome_options
            )

        # if request.param == "firefox":
        #     firefox_options = FirefoxOptions()
        #     # firefox_options.add_argument("--headless")
        #     self.web_driver = webdriver.Remote(
        #         command_executor='http://localhost:4445/wd/hub',
        #         options=firefox_options
        #     )

        request.cls.driver = self.web_driver
        self.web_driver.implicitly_wait(10)
        yield
        self.web_driver.close()
