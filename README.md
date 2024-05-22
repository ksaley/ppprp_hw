## Prerequities
Необходимо, чтобы были установлены следующие инструменты:
* Docker
* kubectl
* Minikube для локального тестирования

## Запуск

Нужно выполнить следующие команды: 
* `minicube start`
* `./deploy.sh`
* `minikube service myapp-service`


Последняя команда выведет информацию об адресе, куда нужно обращаться за статистикой:

curl http://<адрес-сервиса>/time

curl http://<адрес-сервиса>/statistics
