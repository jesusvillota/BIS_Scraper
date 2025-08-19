from __future__ import annotations
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def bis_link(initial_date, final_date, page, page_length): 
    """Generate a link to the BIS speeches page with the specified parameters.
    
    Args:
        initial_date: Start date in format 'DD/MM/YYYY'
        final_date: End date in format 'DD/MM/YYYY'
        page: Page number to retrieve
        page_length: Number of speeches per page
        
    Returns:
        A formatted URL string to access the BIS speeches
    """
    index_url = (
        f"https://www.bis.org/cbspeeches"
        f"?fromDate={initial_date}"
        f"&tillDate={final_date}"
        f"&cbspeeches_page={page}"
        f"&cbspeeches_page_length={page_length}"
    )
    return index_url


def scrape(config: dict) -> None:
    """Replicates the notebook's scraping behavior with parameters from config.
    - Iterates pages from 1 to MAX_PAGE
    - Opens each review link
    - Looks for a PDF link and downloads it to DOWNLOAD_DIR
    - Uses simple time.sleep waits matching the notebook
    """
    BASE_URL = config["BASE_URL"]
    DOWNLOAD_DIR = config["DOWNLOAD_DIR"]
    INITIAL_DATE = config["INITIAL_DATE"]
    FINAL_DATE = config["FINAL_DATE"]
    PAGE_LENGTH = int(config["PAGE_LENGTH"])
    MAX_PAGE = int(config["MAX_PAGE"])

    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    driver = webdriver.Chrome()

    try:
        for i in range(1, MAX_PAGE + 1):
            index_url = bis_link(INITIAL_DATE, FINAL_DATE, i, PAGE_LENGTH)
            print(f"\n=== Processing page {i} with Selenium ===")
            print(f"🔗 Requesting URL: {index_url}")
            driver.get(index_url)
            time.sleep(5)  # Wait for JS

            try:
                container = driver.find_element(By.ID, "cbspeeches_list")
                review_links = container.find_elements(By.CSS_SELECTOR, "a.dark[href^='/review/']")
                review_hrefs = [link.get_attribute("href") for link in review_links]
                print(f"✅ Found {len(review_hrefs)} review links on page {i}.")
            except Exception as e:
                print(f"❌ Could not find review links on page {i}: {e}")
                continue

            # --- Iterate over each review link ---
            for review_url in review_hrefs:
                if review_url is None:
                    continue
                    
                print(f"🌐 Visiting: {review_url}")
                driver.get(review_url)
                time.sleep(2)  # Wait for detail page JS (adjust if necessary)

                # Look for pdf link on the detail page
                try:
                    pdf_link = driver.find_element(By.CSS_SELECTOR, "a.pdftitle_link[href$='.pdf']")
                    pdf_href = pdf_link.get_attribute("href")
                    if pdf_href and not pdf_href.startswith("http"):
                        pdf_href = BASE_URL + pdf_href
                    
                    if pdf_href:
                        print(f"📄 PDF found: {pdf_href}")

                        # Download the PDF
                        response = requests.get(pdf_href)
                        filename = os.path.basename(pdf_href)
                        save_path = os.path.join(DOWNLOAD_DIR, filename)
                        with open(save_path, "wb") as f:
                            f.write(response.content)
                        print(f"💾 Downloaded PDF to {save_path}")
                except Exception as e:
                    print(f"❌ No PDF found or error: {e}")
    finally:
        driver.quit()
