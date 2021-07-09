import requests
from bs4 import BeautifulSoup
import csv
import re

URL = 'https://www.hunting.ru/forum/'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0' , 'accept':'*/*'}
FILE = 'forums.csv'

 
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_=re.compile('node forum level_2'))

    forum_names = []

    for item in items:
        block = item.find('h3', class_='nodeTitle').find_next('a').get_text(strip=True)
        theme = item.find('span', class_='lastThreadTitle').find_next('a').get_text()
        auth = item.find('span', class_='lastThreadMeta').find_next('span', class_='lastThreadUser').find_next('a').get_text()

        time_call = item.find('abbr', class_='DateTime muted lastThreadDate')
        if time_call:
            time = time_call.get_text(strip=True)
        else:
            time = item.find('span', class_='DateTime muted lastThreadDate').get_text(strip=True)

        forum_names.append({
            'block': block,
            'theme': theme,
            'auth': auth,
            'time': time
            })

    return forum_names
         
def save_file(items, path):
    with open(path, 'w', newline='') as file_a:
        writer = csv.writer(file_a, delimiter=';')
        writer.writerow(['block', 'theme', 'auth', 'time'])
        for item in items:
            writer.writerow([item['block'], item['theme'], item['auth'], item['time']])



html = requests.get(URL, headers = HEADERS)

if html.status_code == 200:
    print('success')
    
    a = get_content(html.text)
    save_file(a, FILE)
    
    print(f'Получено {len(a)} записей')
else:
    print('Error')
