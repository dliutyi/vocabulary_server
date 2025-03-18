from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager
import os

class PostgresDB:
    def __init__(self):
        self.app = None
        self.pool = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.pool = SimpleConnectionPool(
            1, 1,
            host=os.environ.get("DATABASE_HOST"),
            database=os.environ.get("DATABASE_NAME"),
            user=os.environ.get("DATABASE_USER"),
            password=os.environ.get("DATABASE_PASSWORD")
        )
        return self.pool

    @contextmanager
    def get_cursor(self):
        if self.pool is None:
            self.connect()
        con = self.pool.getconn()
        try:
            yield con.cursor()
            con.commit()
        finally:
            self.pool.putconn(con)