import requests
from bs4 import BeautifulSoup
import mysql.connector

# اتصال به دیتابیس
db = mysql.connector.connect(
    host="localhost",
    user="root",  # نام کاربری MySQL
    password="0113",  # کلمه عبور MySQL
    database="country_info"  # نام دیتابیس
)

cursor = db.cursor()

# وب‌اسکرپینگ
url = 'https://scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# استخراج اطلاعات کشورها
countries = soup.find_all('div', class_='country')
for country in countries:
    name = country.find('h3').text
    population = int(country.find('span', class_='population').text.replace(',', ''))
    area = float(country.find('span', class_='area').text.replace(' km²', '').replace(',', ''))

    # محاسبه چگالی جمعیت
    estimated_density = population / area if area > 0 else 0

    # ذخیره اطلاعات در دیتابیس
    cursor.execute("INSERT INTO countries (name, population, area, estimated_density) VALUES (%s, %s, %s, %s)", 
                   (name, population, area, estimated_density))

# تایید تغییرات و بستن اتصال
db.commit()
cursor.close()
db.close()
