import requests
import time

for _ in range(12):
    response = requests.get('http://myapp-service/statistics')
    with open('stats.txt', 'a') as file:
        file.write(response.text + '\n')
    time.sleep(5) 