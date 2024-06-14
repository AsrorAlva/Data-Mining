from playwright.sync_api import sync_playwright
import time

def analisis() :
    with sync_playwright() as p :
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page_url = ''
        page.goto(page_url)
        
        time.sleep(10)
        
        datas = page.get_by_alt_text("")
        
        for data in datas :
            analisa = data.locator("").inner_text()
            print(analisa)