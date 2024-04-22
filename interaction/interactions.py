from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from exception.exception import UserNotFoundException
from models.models import Base, User

# подключение к базе данных PostgreSQL с помощью SQLAlchemy
class DbInteraction:

    def __init__(self, host, port, user, password, db_name, rebuild_db=False):
        self.engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}')

        if rebuild_db:
            self.create_table_users()
            self.create_table_dishes()

    def create_table_users(self):
        Base.metadata.create_all(self.engine)

    def create_table_dishes(self):
        Base.metadata.create_all(self.engine)


    def get_user_info(self, username):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = session.query(User).filter_by(username=username).first()
        if user:
            session.expire_all() #заставляет сессию обновить все объекты, удаляет кэш
            return {'username': user.username, 'email': user.email, 'password': user.password}
        else:
            raise UserNotFoundException('User not found!')

    def add_user_info(self, username, email, password):
        user = User(
            username=username,
            password=password,
            email=email
        )
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add(user)
        session.commit()
        return self.get_user_info(username)

    def edit_user_info(self, username, new_username=None, new_email=None, new_password=None):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        user = session.query(User).filter_by(username=username).first()
        if user:
            if new_username is not None:
                user.username = new_username
            if new_email is not None:
                user.email = new_email
            if new_password is not None:
                user.password = new_password
            session.commit()
            return self.get_user_info(username if new_username is None else new_username)
        else:
            raise UserNotFoundException



if __name__ == '__main__':
    db = DbInteraction(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='ghbdtn137',
        db_name='some_db',
        rebuild_db=True)
