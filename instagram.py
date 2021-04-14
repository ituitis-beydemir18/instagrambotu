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
tm.sleep(2)
driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
tm.sleep(3)

"""tm.sleep(5)
driver.execute_script("window.scrollTo(0, 2000)")                                                                                                     #bu kısım yüklenmemiş resme basılamayacağı için onun yüklenmesini sağlıyordu
tm.sleep(5)
driver.execute_script("window.scrollTo(0, 2000)")"""
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[2]/div[1]/a").click()      #burasıdır 

"""tm.sleep(5)
for i in range(20):
    try:
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/li/div/button/span").click()                                     #yorumlardaki + tuşuna basıyor
        if i<20:
            tm.sleep(2) 
        tm.sleep(4) 
        print(i)
    except Exception as a:
        print(a)
print("'+' tuşuna basma işlemi bitti")"""
liste = ['@__nazkorkmaz', '@melikeozkannn', '@seymaa_tknn._', '@tekinsizfikret', '@bektaserenakblue', '@ssonmezselin', '@1selvii', '@busra.catili', '@kaancenkk', '@sezer.turkyilmaz', '@engin.alanbay', '@nagehan.cetinkaya', '@ozlmbdr35', '@f__buse', '@kzgrtesraa', '@arkn_yasin007', '@pelinsu.shn', '@duyguukayya', '@beeyzakartal', '@izemerkekk', '@iremmbaserr', '@hemrje daha kritik bir ihtiyaç görmedim?', '@aslihanyasarrr', '@hakan.saygin', '@theamazingworldofgizem bundan bulmamız lazım', '@meteozturrrkk allah peygamber askına bizim olsun bu akdşzüziamsnspğdp HARİKA', '@dcselek', '@aziz.arslanca', '@betulduymazz', '@eeliifsaree bunsuz yaşayamaö artık', '@sudeyildirim01', 'bu ne güzellik be! @joinandblend�', '@velitrkolu çüşş kdndkdndnd', '@gamzzeylmzz', '@ogun.altun', '@kaanaksy', '@onur.bilgen', '@denizdinnc', '@iremcanb', '@dilsat.yigit', '@denizsydmr', '@aydan.aydinsahin', '@betulerikli', '@acelyakaraaslan ❤️', 'Ne alaka ya 😂', '@emirmekiin', '@yaseminkudret', '@begumsimseek', '@senatzlgl', '@zeyozdemirnep', '@sebnemaldemir', '@semiihustundag', '@kardelennsari', '@atakansonkaya_', '@emequee', '@fayzek', '@esra.kxya', '@ozlemakcakavak', '@aysenuurrrr_', '@ibrahimckrs', '@batinerbali', '@burakadii', '@yaren.kap', '@ireemkorkmaz', '@gokcccenn', '@eliff_ozcelikk', '@betultankk', '@haticenurturgut', '@senmmert', '@aysenurrbzkurt', '@cansuucangi', '@yaseminutkueri', '@ferityaksi 🍿', '@oykuzamaan', '@ncerennaktas', '@_1havva.nur film izlerken iyi gider kanks', '@onurfakii', '@nesringumus08', '@fbenguyilmaz', '@busenuragl', '@prreciousmemoriess', '@iremozfistikci', '@enesrdem', '@afraisciler', '@mustafahizall', '@elf.ttnc', '@uralldogukan kampta kullanırızz😬', '@evinbasutt', '@pointchargee', '@ilknurozhann', '@ermanyldrm', '@aligzl', '@haticeceydacanturk', '@dberfindogan', '@yagmuruzunerrr', '@aybuknurr', '@erdemsanli1', '@ozgeblc99', '@hbustundag', '@a.samet_71', '@elifffusta61', '@basaksinemau', '@safacetiner14 😬', '@cansubahadiir patlak mısır ablama büyük boy', '@tomapera', '@gozdeetpl', '@tugben.g', '@bengisu_simsek', '@y_a_r_e_nnn', '@caliskan1mertcan', '@yektanyilmaz', '@mcaglarturkeli', '@slhttndemir', '@slhttndemir', '@ahmetfurkanaluc', '@secilcavusogluu', '@ahmetfurkanaluc', '@senematlihan', '@lydashnn', '@m.farukk', '@ozangeyik99', '@nesegokdereli', '@mertcanekiz gdfgdfg', '@edizbalta çok ihtiyacım var nolur', '@0801kardelen', '@zekikutahya', '@imran.metin', '@zeybeste', '@kingoldholborn film izlerdik', '@shuagenea', '@ranaa_kisakol', '@yucel.unl', '@batu_hodman', '@that_s_ma_lu', '@sdybunal', '@dile.k5021', '@vehbikartal', '@suleymanunal4591', '@suleyman8335', '@_s.elma_1903_', '@dondu_yurt_unal_', '@yit.poppa', '@tezcanmry', '@crndmrkya', '@sude.kdk', '@ezgi.cankayaaa ❤️', '@cagsudecankaya 🔥', '@seleen__t bak gıdalarda şansım yüksek benim ❤️', '@zeypicsdaily', '@er.doa biraz da burdan ilerleyelim omzn dksksnsn🙃', '@aartforart', '@ozkncemre', '@figenaysal', '@sevvaldogruyol', '@_merineitsi', '@nurrincel hepsi senin için', '@krmniclal', '@aleynakdmr', '@mutlupsu', '@lanespielg', '@nazim_akcil', '@gulcannonal', '@flyprivhesap', '@zeybeste', '@perihankekic', '@furkan_uygur', '@gizemnnursen', '@emreozskk 🥳', '@bilge_selek', '@ayse_perk', '@smtalds', '@isikksanem']


"""for a in range(1,240):
    try:
        liste.append(driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/div[1]/ul/ul[{}]/div/li/div/div[1]/div[2]/span".format(a)).text)
        print("bi tane daha hadi bakiiim")
        if a%10 ==0:
            tm.sleep(2)
        print(a)
    except Exception as i:
        print(i)
print("okuma bitti")"""

print(liste)
print("listenin uzunluğu  ",len(liste))
tm.sleep(1)
t=0
k=0 
yorum_butonu = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button')
yorum_kutusu= '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/fo  rm/textarea'
paylas_butonu= driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]')

for i in range(0,200):
    try:
        print("i-k:{}-{}".format(i,k))
        if i>k:
            """driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
            tm.sleep(2)
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[3]/a").click()"""   #burasıdır
            driver.refresh()
            tm.sleep(4)
            yorum_butonu= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button')
            yorum_kutusu= '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'               #değişkene pathi değilde direk driver.find diye atadığımda olmadı
            paylas_butonu= driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')
            k = i
        tm.sleep(2)
        yorum_butonu.click()                  
        tm.sleep(1)                                                                                                  #xpath de sonda button olmayan kısımları clicklediğinde çalışmıyo, ayrıca yorum kısmına send_keys yapabilmek için önce yorum butonuna basılması gerekiyo
        driver.find_element_by_xpath(yorum_kutusu).send_keys(liste[i])
        tm.sleep(1)
        driver.find_element_by_xpath(yorum_kutusu).send_keys(" umarım kazanırım")
        tm.sleep(2)
        paylas_butonu.click()
        tm.sleep(3)
        k = k + 1
        if k%5==0:
            tm.sleep(300)
        """if t%2 == 0:
            driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
            tm.sleep(2)
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[3]/a").click()   #burasıdır
            tm.sleep(3)"""
    except Exception as e:
        print(e) 
       








"""Çalışan sekmenin altında sekmeler olduğunda ve sayısı arttığında daha çok hata almaya başladım. bu yorumların sayısının fazladığında kasıyor gibi gelmişti ama bir döngünün 25 sn ve üstüne çıktığı zamanda
ekran değiştirdiğimde saniyede 5 sn e düştü tekrar süresi.bunu yapmadan önce sleep süresini arttırmıştım orda hata almaya başladığım yer diğerine göre biraz artmıştı. aa bu çözüm değil büyük ihtimalle."""




"""5 yorum 5 dk sleep 170 de 30 hata ile çalıştı"""