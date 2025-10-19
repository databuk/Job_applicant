from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from config import EDGE_DRIVER_PATH
import undetected_chromedriver as uc

def get_driver(): 
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    return driver

def get_jobs(url="www.nairaland.com/jobs", limit=5):
    driver = get_driver()
    driver.get(f"https://www.nairaland.com/jobs")
    jobs = []
    for i in range(limit):
        results = driver.find_elements(By.XPATH, "//tr/td[contains(@id, 'top')]")
        row = results[i]

        headline = row.find_element(By.XPATH, ".//b/a[1]").text.strip()
        job_link = row.find_element(By.XPATH, ".//b/a[1]").get_attribute("href")
        driver.get(job_link)
        time.sleep(2)
        try:
            job_details = driver.find_element(By.XPATH, "/html/body/div/table[2]/tbody/tr[2]/td/div[1]").text
        except Exception:
            job_details = "Job details not found."

        jobs.append(
            {"headline": headline, 
             "job_link": job_link,
             "job_details": job_details})
        driver.back()
        time.sleep(2)
    driver.quit()
    return jobs