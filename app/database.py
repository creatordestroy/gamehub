from peewee import MySQLDatabase
from playhouse.pool import PooledMySQLDatabase
from app.config import Config

config = Config()

db = PooledMySQLDatabase(
    config.DATABASE['DB_NAME'],
    user=config.DATABASE['DB_USER'],
    password=config.DATABASE['DB_PASSWORD'],
    host=config.DATABASE['DB_HOST'],
    port=config.DATABASE['DB_PORT'],
    max_connections=20  # maximum number of connections in the pool
)
