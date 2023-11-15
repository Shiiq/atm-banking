Это небольшой пет проект, который своим функционалом повторяет некоторые возможности обычного банкомата, такие как внесение какой-либо суммы на счет, снятие со счета и запрос списка банковских операций за определенный период.

Приложение допускает несколько вариантов запуска:
1. Локальный запуск с взаимодействием через терминал
2. Локальный запуск API сервиса (можно как через docker-compose, так и без)
3. Запуск API на удаленном сервере

Установка приложения:  
Шаг 1 - скачивание приложения
```
mkdir atm && cd atm
git clone https://github.com/Shiiq/atm-banking.git
```
Шаг 2 - настройка виртуального окружения  
Windows
```
python -m venv venv
venv\Scripts\activate.bat
cd atm-banking
```
*nix
```
python3 -m venv venv
source venv/bin/activate
cd atm-banking
```
Шаг 3 - установка зависимостей  
Через pip
```
python -m pip install -r requirements.txt
```
через poetry
```
poetry install
```
Шаг 4 - запуск CLI приложения
```
export LAUNCH=loc
python atm/runner.py -cli
```

Примеры запросов:  
```deposit john doe 15000``` внести сумму на счет  
```withdraw john doe 5000``` снять сумму со счета  
```bankstatement john doe 01-01-2023 31-12-2024``` список совершенных операций за указанный период
