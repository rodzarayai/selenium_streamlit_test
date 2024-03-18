import streamlit as st
import time
from bs4 import BeautifulSoup

"""
## Web scraping on Streamlit Cloud with Selenium

[![Source](https://img.shields.io/badge/View-Source-<COLOR>.svg)](https://github.com/snehankekre/streamlit-selenium-chrome/)

This is a minimal, reproducible example of how to scrape the web with Selenium and Chrome on Streamlit's Community Cloud.

Fork this repo, and edit `/streamlit_app.py` to customize this app to your heart's desire. :heart:
"""

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    driver.get(url = 'https://www.laborum.cl/empleos-publicacion-menor-a-7-dias.html')
    driver.implicitly_wait(10)

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    
    if soup is not None:
        st.write(soup)
    else:
        st.error("Failed to scrape the web page.")

    if driver.page_source is not None:
        st.code(driver.page_source)
    else:
        st.error("Failed to retrieve page source.")
