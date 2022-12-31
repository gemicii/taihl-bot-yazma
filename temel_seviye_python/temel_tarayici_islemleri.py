# tarayıcı nesnemizi import edelim
from moduller.tarayici import Tarayici
from time import sleep

tarayici_nesnesi = Tarayici()
tarayici = tarayici_nesnesi.al()

# tarayıcıda gezinme
tarayici.get("https://teknolojiaihl.meb.k12.tr/")
print(tarayici.current_url)
sleep(2)

# yeni adrese gidelim
tarayici.get("https://teknolojiaihl.meb.k12.tr/34/40/766892/okulumuz_hakkinda.html")
sleep(2)

# geri gönelim
tarayici.back()
print(tarayici.title)
sleep(2)

# ileri gidelim
tarayici.forward()
print(tarayici.title)
sleep(2)

# pencere boyutunu yazdıralım
print(tarayici.get_window_size())

# pencere boyutunu ayarlayalım
tarayici.set_window_size(100,100)

# pencerenin pozisyonunu yazdıralım
print(tarayici.get_window_position())

# pencerenin pozisyonunu ayarlayalım
tarayici.set_window_position(100, 100)
sleep(2)

# penceremizi tam ekran yapalım
tarayici.maximize_window()
sleep(2)

# pencereyi simge durumuna küçültelim
tarayici.minimize_window()
sleep(2)

# pencereyi tam ekran yapalım
tarayici.fullscreen_window()
sleep(2)

# ekran görüntüsü alalım
tarayici.save_screenshot("./gorseller/bot-yazma.png")
