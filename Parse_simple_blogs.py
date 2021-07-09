import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://www.hunting.ru/blogs/'
HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0' , 'accept':'*/*'}
FILE = 'bloggs.csv'

 
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='record btn-hidden-wrap')

    blog_names = []

    for item in items:
        head = item.find('a', class_='a record__title').get_text(strip=True)
        author = item.find('span', class_='record__date-in').find_next('a').get_text()
        text = item.find('div', class_='record__text').get_text(strip=True)
        blog_names.append({
            'head': head,
            'author': author,
            'text': text
            })

    return blog_names
         
def save_file(items, path):
    with open(path, 'w', newline='') as file_a:
        writer = csv.writer(file_a, delimiter=';')
        writer.writerow(['head', 'author', 'text'])
        for item in items:
            writer.writerow([item['head'], item['author'], item['text']])



html = requests.get(URL, headers = HEADERS)

if html.status_code == 200:
    print('success')
    
    a = get_content(html.text)
    save_file(a, FILE)
    
    print(f'Получено {len(a)} записей')
else:
    print('Error')
