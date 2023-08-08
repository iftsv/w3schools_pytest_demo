import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    @pytest.fixture(params=["chrome"], scope='class')
    def init_driver(self, request):
        if request.param == "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--log-level=3")
            # web_driver = webdriver.Chrome(options=chrome_options)
            web_driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=chrome_options
            )
        # if request.param == "firefox":
        #    web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver = web_driver
        web_driver.implicitly_wait(10)
        yield
        web_driver.close()
