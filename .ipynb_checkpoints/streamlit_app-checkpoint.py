import streamlit as st
import time
from bs4 import BeautifulSoup
import logging
import shutil
import time
from pathlib import Path

import undetected_chromedriver as uc


browser_executable_path = shutil.which("chromium")
print(browser_executable_path)

# delete old log file
Path('selenium.log').unlink(missing_ok=True)
time.sleep(1)

options = uc.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")

with uc.Chrome(browser_executable_path=browser_executable_path,
                # debug=False,
                # headless=True,
                options=options,
                use_subprocess=False,
                log_level=logging.DEBUG,
                service_log_path='selenium.log') as driver:
    driver.get(url = 'https://www.laborum.cl/empleos-publicacion-menor-a-7-dias.html')    
    driver.implicitly_wait(10)

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

    st.code(driver.page_source)

