from selenium import webdriver
import time as tm
from selenium.webdriver.common.keys import Keys
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
tm.sleep(2)
driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
tm.sleep(2)

tm.sleep(4)
driver.execute_script("window.scrollTo(0, 2000)")                        #bu kısım yüklenmemiş resme basılamayacağı için onun yüklenmesini sağlıyordu
tm.sleep(4)
driver.execute_script("window.scrollTo(0, 2000)")
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[4]/div[2]/a/div").click()


tm.sleep(5)
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li/div/button/span").click()
tm.sleep(5)  

liste = []
süreler = [4,5,7,8,4,5,4,6,4,5,5,6,4,5,5,4,4,8,8,5,4,7,5]
for a in range(5,24):
    liste.append(driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[{}]/div/li/div/div[1]/div[2]/span/a".format(a)).text)

print(liste)
for i in range(0,23):
    yorum_butonu = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()                      #xpath de sonda buttun olmayan kısımları clicklediğinde çalışmıyo, ayrıca yorum kısmına send_keys yapabilmek için önce yorum butonuna basılması gerekiyo
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(liste[i])
    paylas_butonu = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
    tm.sleep(süreler[i])

"""tm.sleep(3)    
driver.execute_script("window.scrollTo(0, 500)")
tm.sleep(3)    
c = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
#c.click()
c.send_keys(liste[1])
tm.sleep(3)                 
#driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(Keys.ENTER)
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]").click()"""
                            

"""tm.sleep(3)
for i in range(0,23):
    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea").send_keys(liste[i])
    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]").click()
    tm.sleep(3)"""
    
    
    
#driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[1]/div/svg").click()


















"""#driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[5]/div[3]/a/div").click()
#last_height = driver.execute_script("return document.body.scrollHeight")
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[5]/div[3]/a/div/div[1]/img
#print(last_height)
yazıkon= "askidanevar"
yazııııı= driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div/div[1]").text
print("*************************************"+yazııııı+"**************************************")
#yazıkontrol = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text
tm.sleep(3)
#print(yazıkontrol)
#print("KONTROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO8OOOOOOOOOOOOOOOOOOOOOOOOL")
while yazıkon != yazıkontrol :
    driver.execute_script("window.scrollTo(0, 250)")
    #driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[5]/div[3]/a/div/div[1]").click()
    print("KONTROOOOL")
    yazıkontrol = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").text

driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a").click()
#//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[5]/div[3]/a/div/div[1]
yazılar = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span").text

print(yazılar)
#print(yazı)"""