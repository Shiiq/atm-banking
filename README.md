## ATMBanking

Это небольшой пет проект, который своим функционалом повторяет 
некоторые возможности обычного банкомата, такие как 
внесение какой-либо суммы на счет, снятие со счета или запрос 
списка банковских операций за определенный период.

Приложение допускает несколько вариантов запуска:
1. Локальный, с взаимодействием через CLI или API  

Приложение будет запущено напрямую из терминала. В этом режиме используется СУБД **SQLite**, 
данные в которой очищаются перед каждым запуском. Чтобы запустить в таком режиме,
требуется задать переменную окружения `LAUNCH` со значением `loc` (команда `export LAUNCH=loc`).

2. Запуск сервиса через *docker-compose*  

В этом случае приложение и все его компоненты будут развернуты и запущены в контейнерах
(СУБД **PostgreSQL**, сервис для запуска миграций БД, **Nginx** в роли прокси сервера и само приложение).


### Запуск приложения в локальном режиме с CLI или API:  
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
```
```shell
python3 runner.py -cli
или
python3 runner.py -api 
```

#### Примеры запросов для CLI:  
- **Запрос для пополнения или снятия со счета:**  
`<команда> <имя> <фамилия> <сумма>`   
Например:  
`deposit john doe 15000`  
`withdraw john doe 15000`  
- **Запрос для получения списка совершенных операций:**  
`<команда> <имя> <фамилия> <дата от ДД-ММ-ГГГГ> <дата до ДД-ММ-ГГГГ>`  
Например:  
`bankstatement john doe 01-01-2023 31-12-2024`  
- **Чтобы закончить работу с терминалом**  
`exit`
d
#### Примеры запросов для API:  
- **POST /deposit/**
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
  "operation_datetime": "2023-11-16T12:53:27",
  "operation_type": "deposit",
  "operation_amount": 15000,
  "current_balance": 15000
}
```
- **POST /withdraw/**
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
  "operation_datetime": "2023-11-16T12:54:32",
  "operation_type": "withdraw",
  "operation_amount": 15000,
  "current_balance": 0
}
```
- **POST /bank_statement/**
```shell
curl -X POST http://127.0.0.1:10000/bank_statement/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "john",
    "last_name": "doe",
    "since": "2023-01-01",
    "till": "2023-12-31"
  }'
```
```json
{
  "since": "2023-11-01",
  "till": "2023-11-30",
  "current_balance": 0,
  "operations": [
    {
      "operation_datetime": "2023-11-16T12:55:25",
      "operation_type": "deposit",
      "operation_amount": 15000
    },
    {
      "operation_datetime": "2023-11-16T12:55:31",
      "operation_type": "withdraw",
      "operation_amount": 15000
    }
  ]
}
```

### Запуск API сервиса через Docker Compose:  
Шаг 1 - скачивание приложения
```shell
mkdir atm && cd atm
git clone https://github.com/Shiiq/atm-banking.git
```
Шаг 2 - разворачивание и запуск сервиса
```shell
cd atm-banking
docker compose --env-file .env.template -f docker-compose.remote.yml up -d --build
```
#### Примеры запросов для API:  
- **POST /deposit/**
```shell
curl -X POST http://127.0.0.1:18900/deposit/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name":"john",
    "last_name":"doe",
    "amount": "15000"
  }'
```
```json
{
  "operation_datetime": "2023-11-16T12:53:27",
  "operation_type": "deposit",
  "operation_amount": 15000,
  "current_balance": 15000
}
```
- **POST /withdraw/**
```shell
curl -X POST http://127.0.0.1:18900/withdraw/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name":"john",
    "last_name":"doe",
    "amount": "15000"
  }'
```
```json
{
  "operation_datetime": "2023-11-16T12:54:32",
  "operation_type": "withdraw",
  "operation_amount": 15000,
  "current_balance": 0
}
```
- **POST /bank_statement/**
```shell
curl -X POST http://127.0.0.1:18900/bank_statement/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "john",
    "last_name": "doe",
    "since": "2023-01-01",
    "till": "2023-12-31"
  }'
```
```json
{
  "since": "2023-11-01",
  "till": "2023-11-30",
  "current_balance": 0,
  "operations": [
    {
      "operation_datetime": "2023-11-16T12:55:25",
      "operation_type": "deposit",
      "operation_amount": 15000
    },
    {
      "operation_datetime": "2023-11-16T12:55:31",
      "operation_type": "withdraw",
      "operation_amount": 15000
    }
  ]
}
```

#### TODO:
- [ ] тесты
- [ ] CI/CD
- [ ] ...
