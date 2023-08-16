# sap-sqlalchemy-connect

Migrates table `MARA` from Hana to Postgres

# Attention!
 You need to create `.env` file wich contents:

```

PG_HOST=your_postgres_host
PG_PORT=your_postgres_port
PG_USER=your_postgres_user
PG_PASS=your_postgres_pass
PG_NAME=your_postgres_database_name


HANA_HOST=your_hana_host
HANA_PORT=your_hana_port
HANA_USER=your_hana_user
HANA_PASS=your_hana_pass

```

## Installation
Install requirements with

```
python -m pip install -r requirements.txt 
```

If you need postgres, run with docker compose

```
sudo docker-compose up -d
```
Then cheate table `mara`. Sql query is in folder `SQL`

There is no Hana in this compose .-.

# Launch

Just

```
python main.py
```

##

