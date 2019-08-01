# loading the packages
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import pandas as pd

#opening the csv with the list of the cities
with open('muni_try2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

#opening the Web Driver
    driver = webdriver.Chrome()
    driver.get("https://adressverzeichnis.ekd.de/einfachesuche/")

# defining the input elemnt
    elem = driver.find_element_by_id('inputOrt')

#defining variables
    street_adress = ''
    street_chain = []
    number = ''
    number_chain = []
    the_name = ''
    name_chain = []
    first_zip = ''
    zip1_chain = []
    second_zip = ''
    zip2_chain = []
    the_telefon = ''
    telefon_chain = []
    the_fax = ''
    fax_chain =[]
    the_email = ''
    email_chain= []
    the_web = ''
    web_chain = []
    the_konfe = ''
    konfe_chain = []

# the loop which search each city in the site
    for line in csv_reader:
# for each city: reser the search line ,put the city in the search line
# and press search
        goback = driver.find_element_by_id('reset').click()
        elem = driver.find_element_by_id('inputOrt')
        elem.clear()
        elem.click()
        elem.send_keys(line)
        elem = driver.find_element_by_id('readData')
        elem.click()
        driver.implicitly_wait(3)
        try:
# cheak if there are results
            street = driver.find_elements_by_css_selector("span[data-bind='text: Strasse'")
            housenummer = driver.find_elements_by_css_selector("span[data-bind='text: Hausnummer'")
            name = driver.find_elements_by_css_selector("span[data-bind='text: Bezeichnung'")
            zip_code1 = driver.find_elements_by_css_selector("span[data-bind='text: Postleitzahl'")
            zip_code2 = driver.find_elements_by_css_selector("span[data-bind='text: Ort'")
            telefon = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[3]/span")
            fax = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[5]/span")
            email = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[7]/a")
            web = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[9]/a")
            konfe = driver.find_elements_by_css_selector("span[data-bind='text: Konfessionen' ")
        except NoSuchElementException:
# if there are no results, go back
            goback = driver.find_element_by_id('reset').click()
        else:
# if there are reults, save them in a list
                for a in street:
                    street_adress = a.get_attribute("innerHTML")
                    street_chain += [street_adress]
                for b in housenummer:
                    number = b.get_attribute("innerHTML")
                    number_chain += [number]
                for c in name:
                    the_name = c.get_attribute("innerHTML")
                    name_chain += [the_name]
                for d in zip_code1:
                    first_zip = d.get_attribute("innerHTML")
                    zip1_chain += [first_zip]
                for e in zip_code2:
                    second_zip = e.get_attribute("innerHTML")
                    zip2_chain += [second_zip]
                for f in telefon:
                    the_telefon = f.get_attribute("innerHTML")
                    telefon_chain += [the_telefon]
                for g in fax:
                    the_fax = g.get_attribute("innerHTML")
                    fax_chain += [the_fax]
                for h in email:
                    the_email = h.get_attribute("href")
                    email_chain += [the_email]
                for i in web:
                    the_web = i.get_attribute("href")
                    web_chain += [the_web]
                for j in konfe:
                    the_konfe = j.get_attribute("innerHTML")
                    konfe_chain += [the_konfe]
                    
                goback = driver.find_element_by_id('reset')
                goback.click()

# creat dictionary
    dicti ={'title': name_chain,'Street': street_chain,
                       'House_number': number_chain, 'zip code 1': zip1_chain,
                       'zip code 2': zip2_chain, 'telefon': telefon_chain,
                       'fax': fax_chain, 'Email': email_chain,
                       'web':web_chain, 'konfession': konfe_chain }
# save as csv
    df = pd.DataFrame.from_dict(dicti, orient='index').transpose()

    export_csv = df.to_csv(r'C:\Users\user\Desktop\לימודים\מינכן\research_assis\first_task\export_dataframe.csv',index=False)
    



