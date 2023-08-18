import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    web_driver = None

    @pytest.fixture(params=["chrome", "edge"], scope='class')
    def init_driver(self, request):

        if request.param == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--log-level=3")
            self.web_driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options
            )

        if request.param == "edge":
            edge_options = EdgeOptions()
            edge_options.add_argument("--headless")
            edge_options.add_argument("--log-level=3")
            self.web_driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=edge_options
            )

        request.cls.driver = self.web_driver
        self.web_driver.implicitly_wait(10)
        yield
        self.web_driver.close()
