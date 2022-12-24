# selenium ve diğerleri paketler içeri aktarlım
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

tarayici = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# tarayıcıda gezinme
tarayici.get("https://teknolojiaihl.meb.k12.tr/")
print(tarayici.current_url)
sleep(1)

# yeni adrese gidelim
tarayici.get("https://teknolojiaihl.meb.k12.tr/34/40/766892/okulumuz_hakkinda.html")
sleep(1)

# geri gönelim
tarayici.back()
print(tarayici.title)
sleep(1)

# ileri gidelim
tarayici.forward()
print(tarayici.title)
sleep(1)

# pencere boyutunu yazdıralım
print(tarayici.get_window_size())

# pencere boyutunu ayarlayalım
tarayici.set_window_size(500,300)

# pencerenin pozisyonunu yazdıralım
print(tarayici.get_window_position())

# pencerenin pozisyonunu ayarlayalım
tarayici.get_window_position(100,500)
sleep(2)