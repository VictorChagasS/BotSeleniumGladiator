from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

#from PyQt5 import uic, QtWidgets




def login():
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    url = 'https://lobby.gladiatus.gameforge.com/pt_PT/'
    browser.get(url)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]"))).click()
    yourusername = "paulotatanka.pt@gmail.com"  # INTERFACE
    yourpassword = "thmpv77d6f"  # INTERFACE
    username_input = browser.find_element_by_css_selector("input[type='email']")
    password_input = browser.find_element_by_css_selector("input[type='password']")

    username_input.send_keys(yourusername)
    password_input.send_keys(yourpassword)

    login_button = browser.find_element_by_css_selector("button[type='submit']")
    login_button.click()
    time.sleep(3)
    WebDriverWait(browser, 13).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/button"))).click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])

    time.sleep(1)
    time.sleep(1)


def lance():
    lance_menu = '//div[1]/div[1]/div/div[2]/a[15]'
    browser.find_element_by_xpath(lance_menu).click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr[3]/td[2]/select/option[9]"))).click()
    browser.find_element_by_xpath("//table/tbody/tr[5]/td/input").click()
    time.sleep(1)

    #table = "/html/body/div[2]/div/div[6]/div/div[2]/div[2]/table/tbody"
    table_row = browser.find_elements_by_xpath("//table/tbody/tr")
    #table_columns = browser.find_elements_by_xpath("/html/body/div[2]/div/div[6]/div/div[2]/div[2]/table/tbody/tr/td")
    count_row = 0
    my_gold = browser.find_element_by_id("sstat_gold_val").text
    my_gold = my_gold.replace(".", "")

    valor_configurado_lance = 2000 #INTERFACE

    try:
        for row in table_row:
            count_row+=1
            count_col = 0
            for colum in range(2):
                my_gold = browser.find_element_by_id("sstat_gold_val").text
                my_gold = my_gold.replace(".", "")

                count_col += 1
                #ruby = browser.find_element_by_xpath("/html/body/div[2]/div/div[6]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/form/div[2]").text
                WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr["+str(count_row)+ "]/td[" +str(count_col) +"]/div/form/div[2]")))
                ruby = browser.find_element_by_xpath("//table/tbody/tr["+str(count_row)+ "]/td[" +str(count_col) +"]/div/form/div[2]").text

                ruby_count = ruby[-3] + ruby[-2]
                if ((int(ruby_count)) > 50 and int(my_gold) > 10000):
                        #print(my_gold)
                        Lance_Proposta_amuleto = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr["+str(count_row)+ "]/td[" +str(count_col) +"]/div/form/div[2]/input[2]"))).click()





    except:
        pass

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//table/tbody/tr[3]/td[2]/select/option[8]"))).click()
    browser.find_element_by_xpath("//table/tbody/tr[5]/td/input").click()
    time.sleep(1)
    count_row = 0
    try:

        for row in table_row:
            count_row += 1
            count_col = 0
            for colum in range(2):

                count_col += 1
                # ruby = browser.find_element_by_xpath("/html/body/div[2]/div/div[6]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/form/div[2]").text
                WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr[" + str(count_row) + "]/td[" + str(count_col) + "]/div/form/div[2]")))
                ruby = browser.find_element_by_xpath("//table/tbody/tr[" + str(count_row) + "]/td[" + str(count_col) + "]/div/form/div[2]").text

                ruby_count = ruby[-3] + ruby[-2] #QUANTIA DO RUBY

                if ((int(ruby_count)) > 50  and int(my_gold) > 10000):
                    Lance_Proposta_anel = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//table/tbody/tr[" + str(count_row) + "]/td[" + str(count_col) + "]/div/form/div[2]/input[2]"))).click()

    except:
        pass


def lance_mercenario():
    lance_menu = '//div[1]/div[1]/div/div[2]/a[15]'
    browser.find_element_by_xpath(lance_menu).click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//table/tbody/tr[3]/td[2]/select/option[13]"))).click()
    browser.find_element_by_xpath("//table/tbody/tr[5]/td/input").click()

def cura():

                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/div/div[3]/div/div[1]/div[1]/div/a[1]"))).click()
                target_element = browser.find_element_by_xpath("//table/tbody/tr/td[1]/div[2]/div[2]")
                # teste=browser.find_elements_by_class_name("ui-draggable")


                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td[2]/div[6]/div/div[3]/div")))
                source_elements = browser.find_elements_by_xpath("//table/tbody/tr/td[2]/div[6]/div/div[3]/div")
                




def interface():
    while True:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "sstat_gold_val")))
        my_gold = browser.find_element_by_id("sstat_gold_val").text
        my_gold = my_gold.replace(".", "")

        life = browser.find_element_by_id("header_values_hp_percent").text
        life = life.replace("%", "")

        valor_bot_lance = 4000 #interface
        #if (int(my_gold) > valor_bot_lance):

        if (int(life) < 100):
            cura()

        if (int(my_gold)) > 30000:
            lance()
            lance_mercenario()







login()
interface()

#print(my_gold)



