from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import datetime
import time

errors = 0
count = 0

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://recruiter.monsterindia.com/')
# username, password = driver.find_element_by_xpath('//*[@id="login"]'), driver.find_element_by_xpath('//*[@id="passwd"]')
# username.send_keys('xdefvcinx02')
# password.send_keys('Dubai@2020')
# time.sleep(0.5)
# password.submit()
time.sleep(1)

abc = input('login_complete : ')

file_name = '2018-12-08_Monster_Resumes.csv'
csv_file = open(file_name, 'r')
new_file = open(('NEW-' + file_name), 'a')
fieldnames = ['name', 'link', 'exp', 'location', 'nationality', 'info', 'extra_info', 'phone', 'email', 'extra_details', 'industry', 'heading']
writer = csv.DictWriter(new_file, fieldnames=fieldnames)
writer.writeheader()
reader = csv.DictReader(csv_file)
for row in reader:
    link = row.get('link')
    driver.get(link)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    try:
        phone = soup.find('span', {'class': 'mob_container'}).text.strip()
    except:
        phone = '-'
    try:
        email = '-'
        email_fields = soup.find('div', {'class': 'skinfo'}).split('<br>')
        got_it = False
        for email_field in email_fields:
            if '@' in email_field and '.' in email_field:
                email = email_field.text.strip()
                got_it = True
        if not got_it:
            email = soup.find('div', {'class': 'skinfo'}).text.replace('\n', '').replace('\t', '').replace('  ','' ).strip()
    except:
        email = '-'
    try:
        extra_details = soup.find('div', {'class': 'skr_basicinfo_other'}).text.replace('\n', '').replace('\t', '').replace('  ', '').strip()
    except:
        extra_details = '-'
    try:
        industry = '-'
        sub_divs = soup.findAll('div', {'class': 'scndinfo'})
        for sub_div in sub_divs:
            if 'ndustry' in sub_div.text :
                industry = sub_div.text.strip()
    except:
        industry = '-'
    try:
        heading = soup.find('div', {'class': 'res_h1'}).text.strip()
    except:
        heading = '-'
    new_dict = {'phone': phone, 'email': email, 'extra_details': extra_details, 'industry': industry, 'heading': heading}
    new_dict_valid = [True if new_dict[i] == '-' else False for i in new_dict]
    if all(new_dict_valid):
        input('check for captcha')
    my_dict = dict(row)
    my_dict.update(new_dict)
    try:
        writer.writerow(my_dict)
        print(count, '-', my_dict)
        count += 1
    except:
        errors += 1
        print('-----', errors)

print('Total Errors : ', errors)







# from selenium import webdriver
# from bs4 import BeautifulSoup
# import csv
# import datetime
# import time
#
# errors = 0
# count = 0
#
# file_name = '2018-12-08_Monster_Resumes.csv'
# csv_file = open(file_name, 'r')
# new_file = open(('NEW-' + file_name), 'a')
# fieldnames = ['name', 'link', 'exp', 'location', 'nationality', 'info', 'extra_info', 'phone', 'email', 'extra_details', 'industry', 'heading']
# writer = csv.DictWriter(new_file, fieldnames=fieldnames)
# reader = csv.DictReader(csv_file)
# for row in reader:
#
#     try:
#         phone = soup.find('span', {'class': 'mob_container'}).text.strip()
#     except:
#         phone = '-'
#     try:
#         email_field = soup.find('div', {'class': 'skinfo'}).text.strip()
#         if '\n' in email_field:
#             email = email_field.split('\n')[-1].text.strip()
#         else:
#             email = email_field
#     except:
#         email = '-'
#     try:
#         extra_details = soup.find('div', {'class': 'skr_basicinfo_other'}).text.strip()
#     except:
#         extra_details = '-'
#     try:
#         industry = '-'
#         sub_divs = soup.findAll('div', {'class': 'scndinfo'})
#         for sub_div in sub_divs:
#             if 'ndustry' in sub_div.text :
#                 industry = sub_div.text.strip()
#     except:
#         industry = '-'
#     try:
#         heading = soup.find('div', {'class': 'res_h1'}).text.strip()
#     except:
#         heading = '-'
#     new_dict = {'phone': phone, 'email': email, 'extra_details': extra_details, 'industry': industry, 'heading': heading}
#     # my_dict = dict(row).update(new_dict)
#     my_dict = dict(row)
#     my_dict.update(new_dict)
#     print(my_dict)
#     print(type(my_dict))
#     # try:
#     writer.writerow(my_dict)
#     print(count, '-', my_dict)
#     count += 1
#     # except:
#     #     errors += 1
#     #     print('-----', errors)
#
# print('Total Errors : ', errors)