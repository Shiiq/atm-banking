Это небольшой пет проект, который своим функционалом повторяет некоторые возможности обычного банкомата, такие как внесение какой-либо суммы на счет, снятие со счета и запрос списка банковских операций за определенный период.

Приложение допускает несколько вариантов запуска:
1. Локальный запуск с взаимодействием через терминал
2. Локальный запуск API сервиса (можно как через docker-compose, так и без)
3. Запуск API на удаленном сервере

Установка приложения:
```
mkdir atm && cd atm
git clone https://github.com/Shiiq/atm-banking.git
```
Если нет Poetry
```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```
Если есть Poetry
```
cd atm-banking
poetry install
```

Запуск CLI приложения
```
export LAUNCH=loc
python3 atm/runner.py -cli
```

Примеры запросов:  
```deposit john doe 15000``` внести сумму на счет  
```withdraw john doe 5000``` снять сумму со счета  
```bankstatement john doe 01-01-2023 31-12-2023```  список совершенных операций за указанный период
