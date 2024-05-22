import requests
import time

while True:
    response = requests.get('http://127.0.0.1:8000/statistics')
    with open('stats.txt', 'a') as file:
        file.write(response.text + '\n')
    time.sleep(5) 