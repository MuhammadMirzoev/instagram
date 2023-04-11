from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Страница регистрации
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(1)
        # Добавляем пользователя в базу данных
        conn = sqlite3.connect('db/users.db')
        print(11)
        cursor = conn.cursor()
        print(2222)
        cursor.execute('INSERT INTO users VALUES (?, ?)', (username, password))
        print(2)
        conn.commit()
        conn.close()
        return redirect("""https://instagram.com/alv.maga?igshid=YmMyMTA2M2Y=""")

        # return redirect(url_for('login'))
    else:
        return render_template('index.html')
        # return ("""<!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Вход в аккаунт</title>
# </head>
# <body>
#     <h1>Вход</h1>
#     <form action="/" method="post">
#         <label for="username">Логин:</label>
#         <input type="text" id="username" name="username" required><br><br>
#         <label for="password">Пароль:</label>
#         <input type="password" id="password" name="password" required><br><br>
#         <input type="submit" value="Войти">
#     </form>
# </body>
# </html>
# """)

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('register'))


# Страница входа
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         Получаем данные из формы
        # return """<href = 'https://instagram.com/alv.maga?igshid=YmMyMTA2M2Y='"""
#         username = request.form['username']
#         password = request.form['password']
#
#         # Проверяем, есть ли такой пользователь в базе данных
#         conn = sqlite3.connect('users.db')
#         c = conn.cursor()
#         c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#         user = c.fetchone()
#         conn.close()
#
#         if user:
#             return 'Добро пожаловать, {}!'.format(username)
#         else:
#             return 'Неверный логин или пароль'
#     else:
#         return render_template("""<!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Вход</title>
# </head>
# <body>
#     <h1>Вход</h1>
#     <form action="/login" method="post">
#         <label for="username">Логин:</label>
#         <input type="text" id="username" name="username" required><br><br>
#         <label for="password">Пароль:</label>
#         <input type="password" id="password" name="password" required><br><br>
#         <input type="submit" value="Войти">
#     </form>
# </body>
# </html>
# """"")

if __name__ == '__main__':
    # Создаем базу данных

    # Запускаем веб-сервер
    app.run(port=5050, host='127.0.0.1')
