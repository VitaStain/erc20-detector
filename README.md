# ERC-20 detector API

- - -
ERC-20 detector API is a Python backend service for checking contract and set standard and version

## Contents

- - - 

- [Stack](#stack)
- [Installation](#installation)
- [Run](#run)
- [Run with Docker](#run-with-docker)
- [Documentation](#documentation)
- [Content](#content)

## Stack:

- - - 

* Python 3.10
* Fastapi 0.111
* Pydantic 2.8.2
* Sqlalchemy 2.0.31
* Alembic 1.13.2
* Taskiq 0.11.6
* Poetry 1.8.3

## Installation:

- - - 

#### 1. Go to IDE and run in terminal:

   ```bash
   git clone https://github.com/VitaStain/erc20-detector.git
   ```

#### 2. Set env variables in .env file (an example can be found in the file ".env.example"

  ```bash
  cp .env.example .env
  ```

##### 2.1 Set ETHERSCAN__API_KEY (get from https://etherscan.io/myapikey)

## Run:

- - - 

#### 1. Install poetry:

   ```bash
   pip install poetry
   ```

#### 2. Install requirements:

   ```bash
   poetry install
   ```

#### 3. Apply database migrations

   ```bash
   alembic upgrade head
   ```

#### 4. Start postgresql and create database

#### 5. Run api:

   ```bash
   python -m src
   ```

#### 6. Run taskiq:

   ```bash
   taskiq worker --workers 2 src.config.tkq:broker
   ```

## Run with Docker

- - - 

#### 1. Build:

   ```bash
   docker compose --project-directory . build
   ```

or

   ```bash
   make build
   ```

#### 2. Run:

   ```bash
   docker compose --project-directory . up -d
   ```

or

   ```bash
   make up
   ```

## Documentation

- - - 

- Swagger. Check on http://127.0.0.1:8000
- Redoc. Check on http://127.0.0.1:8000//redoc

## Content

- - - 

### 1. Standards

#### 1.1 GET api/v1/standards/ - Get all the standards

#### 1.2 POST api/v1/standards/ - Add standard to database

Request body:

```json
{
  "name": "string",
  "functions": [
    {
      "name": "string"
    }
  ]
}
```

name - Standard name  
functions name - Name function or event for this standard

#### 1.3 DELETE /api/v1/standards/{standard_name} - Delete standard from database by name

#### 1.4 GET /api/v1/standards/{standard_name} - Get standard from database by name

### 2. Extensions

#### 2.1 POST /api/v1/extensions/ - Parse extensions from github repository

Request body:

default value:

```json
{
  "repo_owner": "OpenZeppelin",
  "repo_name": "openzeppelin-contracts",
  "directory": "contracts/token/ERC20/extensions",
  "standard_name": "ERC-20"
}
```

### 3. Contracts

#### 3.1 GET /api/v1/contracts/ - Get all the contracts from database

#### 3.2 POST /api/v1/contracts/ - Add contract to database (Get source code from ETHERSCAN)

(REQUIRED ETHERSCAN__API_KEY var)

#### 3.3 GET /api/v1/contracts/{contract_id} - Get the contract from database by id

#### 3.4 POST /api/v1/contracts/check_contracts - Start task for detection contracts

(Which have status = wait_processing and do not have standard)

#### 3.5 POST /api/v1/contracts/check_contracts/{contract_id} - Start task for detection contract by id