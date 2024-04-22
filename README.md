> Flask, SQLAlchemy, PostgreSQL

Проект по выводу, добавлению, модификации записей о пользователях в PostgreSQL

Установить зависимости: flask, configparser, threading, sqlalchemy

Запустить interactions.py для создания БД и таблиц

Запустить server.py

Выполнить запрос из Postman по типу:

• GET http://127.0.0.1:5005/get_user_info/user_test

• POST http://127.0.0.1:5005/add_user_info c Header: Content-type Application/json и Body:
{
"username":"uzver",
"password":"pass",
"email":"uzver_mail"
}

• PUT http://127.0.0.1:5005/edit_user_info/user_test c Header: Content-type Application/json и Body:
{
"username":"uzver1",
"password":"pass",
"email":"uzver1_mail"
}
