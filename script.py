# from selenium import webdriver
# from bs4 import  BeautifulSoup
# import time
# from selenium.webdriver.common.keys import Keys
# import csv
# import datetime
#
# errors = 0
# fieldnames = ['name', 'link', 'exp', 'location', 'nationality', 'info', 'extra_info']
# csv_file = open('{0}_Monster_Resumes.csv'.format(datetime.date.today()), 'a')
# writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
# writer.writeheader()
#
# driver = webdriver.Chrome('chromedriver.exe')
# login_url = 'https://recruiter.monsterindia.com/'
# driver.get(login_url)
# abc = input('ok')
# # username, password = driver.find_element_by_xpath('//*[@id="login"]'), driver.find_element_by_xpath('//*[@id="passwd"]')
# # username.send_keys('xdefvcinx02')
# # password.send_keys('Dubai@2020')
# time.sleep(0.5)
# # password.submit()
# time.sleep(1)
# driver.get('http://recruiter.monsterindia.com/v2/resumedatabase/searchresult.html')
# time.sleep(1)
# html = driver.find_element_by_tag_name('html')
# html.send_keys(Keys.END)
# time.sleep(3)
# source = driver.page_source
# soup = BeautifulSoup(source, 'lxml')
# resumes = soup.findAll('div', {'class': 'resumeitem'})
# for resume in resumes:
#     try:
#         name = resume.find('a', {'class': 'skname'}).text.strip()
#     except:
#         name = '-'
#     try:
#         link = resume.find('a', {'class': 'skname'})['href']
#     except:
#         link = '-'
#     try:
#         exp = resume.find('div', {'class': 'skinfo'}).text.strip()
#     except:
#         exp = '-'
#     try:
#         location = resume.find('div', {'class': 'info_loc'}).text.strip()
#     except:
#         location = '-'
#     try:
#         nationality = resume.find('div', {'class': 'nationality'}).text.strip()
#     except:
#         nationality = '-'
#     try:
#         info = resume.find('div', {'class': 'scndinfo'}).text.strip()
#     except:
#         info = '-'
#     try:
#         extra_info = resume.find('div', {'class': 'bottomboxtxt'}).text.strip()
#     except:
#         extra_info = '-'
#     my_dict = {'name': name, 'link': link, 'exp': exp, 'location': location,
#                'nationality': nationality, 'info': info, 'extra_info': extra_info}
#     try:
#         writer.writerow(my_dict)
#         print(my_dict)
#     except:
#         errors += 1
#         print(errors)
# time.sleep(1)
# # driver.close()
# print('Total Errors : ', errors)










from selenium import webdriver
from bs4 import  BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import csv
import datetime

errors = 0
fieldnames = ['name', 'link', 'exp', 'location', 'nationality', 'info', 'extra_info']
csv_file = open('{0}_Monster_Resumes.csv'.format(datetime.date.today()), 'a')
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

driver = webdriver.Chrome('chromedriver.exe')
login_url = 'https://recruiter.monsterindia.com/'
driver.get(login_url)
abc = input('login here : ')
# username, password = driver.find_element_by_xpath('//*[@id="login"]'), driver.find_element_by_xpath('//*[@id="passwd"]')
# username.send_keys('xdefvcinx02')
# password.send_keys('Dubai@2020')
time.sleep(0.5)
# password.submit()
time.sleep(1)
current_page = 1
driver.get('http://recruiter.monsterindia.com/v2/resumedatabase/searchresult.html')
efg = input('160 button')
def get_page():
    global errors
    time.sleep(1)
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(3)
    source = driver.page_source
    soup = BeautifulSoup(source, 'lxml')
    resumes = soup.findAll('div', {'class': 'resumeitem'})
    for resume in resumes:
        try:
            name = resume.find('a', {'class': 'skname'}).text.strip()
        except:
            name = '-'
        try:
            link = resume.find('a', {'class': 'skname'})['href']
        except:
            link = '-'
        try:
            exp = resume.find('div', {'class': 'skinfo'}).text.strip()
        except:
            exp = '-'
        try:
            location = resume.find('div', {'class': 'info_loc'}).text.strip()
        except:
            location = '-'
        try:
            nationality = resume.find('div', {'class': 'nationality'}).text.strip()
        except:
            nationality = '-'
        try:
            info = resume.find('div', {'class': 'scndinfo'}).text.strip()
        except:
            info = '-'
        try:
            extra_info = resume.find('div', {'class': 'bottomboxtxt'}).text.strip()
        except:
            extra_info = '-'
        my_dict = {'name': name, 'link': link, 'exp': exp, 'location': location,
                   'nationality': nationality, 'info': info, 'extra_info': extra_info}
        try:
            writer.writerow(my_dict)
            print(my_dict)
        except:
            errors += 1
            print(errors)
    time.sleep(1)
    input('change page')
    get_page()
    # current_page_button = soup.find('div', {'class': 'sractivenew'})
get_page()
# driver.close()
print('Total Errors : ', errors)