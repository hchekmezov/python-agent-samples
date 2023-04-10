import os

import pytest
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    zebrunner_selenium_grid = os.getenv("ZEBRUNNER_SELENIUM_GRID", "http://127.0.0.1:4444")

    ############################################################################################
    options = webdriver.FirefoxOptions()
    # options = webdriver.ChromeOptions()
    options.platform_name = "linux"
    options.browser_version = "109.0"
    options.set_capability("enableVideo", "true")
    ############################################################################################

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Remote(
        command_executor=zebrunner_selenium_grid,
        options=options
    )

    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver

    driver.quit()
