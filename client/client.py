'''
import sqlalchemy

from sqlalchemy.orm import sessionmaker


class MySQLConnection:
    def __init__(self, host, port, user, password, db_name, rebuild_db=False):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.rebuild_db = rebuild_db
        self.connection = self.connect()

        session = sessionmaker(
            bind=self.connection,
            autocommit=True,
            enable_baked_queries=False,
            expire_on_commit=True,  # изменения в рамках одной сессии, они не добавляются в БД
        )

        self.session = session()

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name if db_created else ""}',
            encoding='utf8'
        )
        return engine.connect()


    # SQL-инъекция
    def execute_query(self, query):
        res = self.connection.execute(query)
        return res
'''