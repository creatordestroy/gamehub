from peewee import MySQLDatabase
from playhouse.pool import PooledMySQLDatabase
import config

db = PooledMySQLDatabase(
    config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    max_connections=20,  # maximum number of connections in the pool
)
