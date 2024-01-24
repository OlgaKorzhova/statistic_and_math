import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

# Список городов
cities = ["Moscow", "New York", "Beijing"]

# Задаем URL источника данных о погоде
url_template = "https://rp5.ru/{city}/{year}/{month}" 

# Создание пустого DataFrame для хранения погодных данных
weather_data = pd.DataFrame(columns=["City", "Date", "Temperature"])

# Запрос погодных данных для каждого города
for city in cities:
    # Задаем параметры для URL
    current_date = pd.Timestamp.utcnow()
    year = current_date.year
    month = current_date.month
    
    # Создаем URL с актуальными параметрами
    url = url_template.format(city=city, year=year, month=month)
    
    # Отправляем GET-запрос на получение HTML-страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Извлечение дат и температур из HTML-страницы
    dates = []
    temperatures = []
    
    date_elements = soup.select(".date")
    temperature_elements = soup.select(".t_0")
    
    for date_element, temperature_element in zip(date_elements, temperature_elements):
        date = pd.to_datetime(date_element.text, format="%d.%m.%Y")
        temperature = float(temperature_element.text.replace("°C", "").replace(",", "."))
        
        dates.append(date)
        temperatures.append(temperature)
    
    # Добавление данных в DataFrame
    city_weather_data = pd.DataFrame({"City": city, "Date": dates, "Temperature": temperatures})
    weather_data = weather_data.append(city_weather_data, ignore_index=True)

# График изменения температуры в разных городах
plt.figure(figsize=(10, 6))
for city in cities:
    city_data = weather_data[weather_data["City"] == city]
    plt.plot(city_data["Date"], city_data["Temperature"], label=city)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Change in Different Cities")
plt.legend()
plt.show()

# График распределения температуры
plt.figure(figsize=(8, 6))
plt.hist(weather_data["Temperature"], bins=20)
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Temperature Distribution")
plt.show()

# Сохранение данных в HDFS
hdfs_path = "/path/to/hdfs/weather_data.csv"
weather_data.to_csv(hdfs_path, index=False)

# Выгрузка данных из HDFS на локальный компьютер
local_path = "/path/to/local/weather_data.csv"
subprocess.run(["hdfs", "dfs", "-get", hdfs_path, local_path])