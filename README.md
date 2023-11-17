## ATMBanking

Это небольшой пет проект, который своим функционалом повторяет 
некоторые возможности обычного банкомата, такие как 
внесение какой-либо суммы на счет, снятие со счета или запрос 
списка банковских операций за определенный период. При операции пополения счета, если 
такого клиента нет в базе данных, то он добавится. Если


Приложение допускает несколько вариантов запуска:
1. Локальный, с взаимодействием через CLI или API  
(в этом режиме используется СУБД **SQLite**, которая очищается перед каждым запуском, для активации этого режима требуется переменная окружения `LAUNCH=loc`)
2. API сервис через _docker-compose_
3. API сервис на удаленном сервере

#### Итак, чтобы запустить приложение в локальном режиме с CLI или API:  
Шаг 1 - скачивание приложения
```shell
mkdir atm && cd atm
git clone https://github.com/Shiiq/atm-banking.git
```
Шаг 2 - настройка виртуального окружения  
```shell
python3 -m venv venv
source venv/bin/activate
cd atm-banking
```
Шаг 3 - установка зависимостей  
Через pip
```shell
python3 -m pip install -r requirements.txt
```
Через poetry
```shell
poetry shell
poetry install
```
Шаг 4 - запуск
```shell
export LAUNCH=loc
python3 runner.py -cli
или
python3 runner.py -api 
```

#### Примеры запросов для CLI:  
```deposit john doe 15000``` внести сумму на счет  
```withdraw john doe 15000``` снять сумму со счета  
```bankstatement john doe 01-01-2023 31-12-2024``` список совершенных операций за указанный период

#### Примеры запросов для API:  
POST /deposit/
```shell
curl -X POST http://127.0.0.1:10000/deposit/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name":"john",
    "last_name":"doe",
    "amount": "15000"
  }'
```
```json
{
  "operation_datetime":"2023-11-16T12:53:27",
  "operation_type":"deposit",
  "operation_amount":15000,
  "current_balance":15000
}
```
POST /withdraw/
```shell
curl -X POST http://127.0.0.1:10000/withdraw/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name":"john",
    "last_name":"doe",
    "amount": "15000"
  }'
```
```json
{
  "operation_datetime":"2023-11-16T12:54:32",
  "operation_type":"withdraw",
  "operation_amount":15000,
  "current_balance":0
}
```
POST /bank_statement/
```shell
curl -X POST http://127.0.0.1:10000/bank_statement/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "john",
    "last_name": "doe",
    "since": "2023-11-01",
    "till": "2023-11-30"
  }'
```
```json
{
  "since":"2023-11-01",
  "till":"2023-11-30",
  "balance":0,
  "operations":[
    {
      "operation_datetime":"2023-11-16T12:55:25",
      "operation_type":"deposit",
      "operation_amount":15000
    },
    {
      "operation_datetime":"2023-11-16T12:55:31",
      "operation_type":"withdraw",
      "operation_amount":15000
    }
  ]
}
```

Запуск приложения в Docker