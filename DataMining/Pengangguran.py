from playwright.sync_api import sync_playwright
import time

def Keadaann_Ketenagakerjaan():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page_url = 'https://www.bps.go.id/id/pressrelease/2023/11/06/2002/tingkat-pengangguran-terbuka--tpt--sebesar-5-32-persen-dan-rata-rata-upah-buruh-sebesar-3-18-juta-rupiah-per-bulan.html'
        page.goto(page_url)
        
        time.sleep(10)
        
        datas = page.locator("div.mt-4").nth(0).all()
        
        for data in datas :
            judul = data.locator("h1").inner_text()
            print("Judul : ", judul)
            
            subJudulA = data.locator("b").nth(1).inner_text()
            print(subJudulA)
            
            isi = data.locator("li").nth(0).inner_text()
            print("-",isi)
            
            isi2 = data.locator("li").nth(1).inner_text()
            print("-",isi2) 
            
            isi3 = data.locator("li").nth(2).inner_text()
            print("-",isi3)
            
            isi4 = data.locator("li").nth(3).inner_text()
            print("-",isi4)
            
            isi5 = data.locator("li").nth(4).inner_text()
            print("-",isi5)
            
            isi6 = data.locator("li").nth(5).inner_text()
            print("-",isi6)
            
            subJudulB = data.locator("b").nth(2).inner_text()
            print(subJudulB)
            
            isi7 = data.locator("li").nth(6).inner_text()
            print("-",isi7)
            
            isi8 = data.locator("li").nth(7).inner_text()
            print("-",isi8)
            
            isi9 = data.locator("li").nth(8).inner_text()
            print("-",isi9)
            
            isi10 = data.locator("li").nth(9).inner_text()
            print("-",isi10)
            
            isi11 = data.locator("li").nth(10).inner_text()
            print("-",isi11)
            
            isi12 = data.locator("li").nth(11).inner_text()
            print("-",isi12)
            
            
        browser.close()