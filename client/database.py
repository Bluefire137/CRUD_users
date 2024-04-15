import psycopg2

with psycopg2.connect(dbname="DishDash", user="postgres", password="ghbdtn137", host="127.0.0.1") as conn:
    with conn.cursor() as cursor:
        # команда для создания базы данных Dishes
        # cursor.execute("CREATE DATABASE Dishes")

        cursor.execute("CREATE TABLE Users (id_users SERIAL PRIMARY KEY, id_dish smallint)")

        # cursor.execute("DROP TABLE IF EXISTS  Dish_ingredients CASCADE; CREATE TABLE  Dish_ingredients(id_dish smallint,id_ingredient smallint,PRIMARY KEY(id_dish, id_ingredient), FOREIGN KEY (id_dish) REFERENCES  Dishes(id_dish), FOREIGN KEY (id_ingredient) REFERENCES  Ingredients(id_ingredient))")
        print("Таблица успешно создана")
        conn.commit()
