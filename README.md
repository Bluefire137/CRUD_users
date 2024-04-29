> Flask, SQLAlchemy, PostgreSQL

Вывод, добавление, редактирование и удаление записей пользователей в PostgreSQL

Зависимости: requirements.txt

Ход:
1) запустить interactions.py для создания БД и таблиц

2) запустить server.py для запуска сервера

3) выполнить запросы по типу:

• GET http://127.0.0.1:5005/get_all_username/

• POST http://127.0.0.1:5005/add_user_info/:
fetch('/add_user_info', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'peter',
        password: 'asd',
        email: 'peter@gmail.com'
    })
})
.then(response => response.text())
.then(console.log)

• PUT http://127.0.0.1:5005/edit_user_info/peter:
fetch('/edit_user_info', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'petr',
        password: 'pass',
        email: 'petr@mail.com'
    })
})
.then(response => response.text())
.then(console.log)

• DELETE http://127.0.0.1:5005/delete_user_info/petr
