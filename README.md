<h2>Развернуть через Docker локально:</h2>

1) Скачать или клонировать репозиторий
2) перейти в директорию scr
3) запустить команду
<code>docker-compose up -d --build</code>
4) создать суперпользователя <br><code>docker-compose exec web python manage.py createsuperuser</code>




<h2>Документация</h2>

http://localhost:8000/redoc/
или
http://localhost:8000/swagger/
