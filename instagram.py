from selenium import webdriver
import time as tm
from selenium.webdriver.common.keys import Keys
#import emoji
driver = webdriver.Chrome(r"C:\Users\User\OneDrive\Masaüstü\chromedriver.exe")

driver.get("https://www.instagram.com")
tm.sleep(3)

driver.maximize_window()

giris1 = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
sifre1 = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
giris1.send_keys("mahmutizel@hotmail.com")
sifre1.send_keys("3610619Baris")
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
tm.sleep(5)
driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys("askidanevar")
tm.sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
tm.sleep(3)

tm.sleep(5)
driver.execute_script("window.scrollTo(0, 2000)")                                                                                                     #bu kısım yüklenmemiş resme basılamayacağı için onun yüklenmesini sağlıyordu
"""tm.sleep(5)
driver.execute_script("window.scrollTo(0, 2000)")"""
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a").click()


tm.sleep(5)
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li/div/button/span").click()                                     #yorumlardaki + tuşuna basıyor
tm.sleep(5)  

liste = []
süreler = [4,5,7,8,4,5,4,6,4,5,5,6,4,5,5,4,4,8,8,5,4,7,5]
for a in range(1,24):
    liste.append(driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[{}]/div/li/div/div[1]/div[2]/span".format(a)).text)


print(liste)
tm.sleep(2)
t=0
for i in range(0,20):
    yorum_butonu = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()  
    tm.sleep(2)                                                                                                                     #xpath de sonda button olmayan kısımları clicklediğinde çalışmıyo, ayrıca yorum kısmına send_keys yapabilmek için önce yorum butonuna basılması gerekiyo
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(liste[i])
    tm.sleep(2)
    paylas_butonu = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
    tm.sleep(süreler[i])
    t = t + 1
    if t%2 == 0:
        driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
        tm.sleep(2)
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a").click()
        tm.sleep(3)


