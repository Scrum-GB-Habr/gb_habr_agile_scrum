## Проект "Habr"
## Командная разработка по методологии Agile:Scrum
## Учебный проект

### Базовая документация к проекту

Основные системные требования:

* Ubuntu 16.04.6 LTS и выше 
* Python 3.8
* MySQL 5.7
* Django 3.2
* Зависимости (Python) из requirements.txt

### Установка необходимого ПО
#### обновляем информацию о репозиториях
```
apt update
```
#### Установка nginx, СУБД MySQL, Git, virtualenv, gunicorn
nginx
```
apt install nginx
```
СУБД MySQL
<br><br>
Подробное описание смотри тут: <a href="https://losst.ru/ustanovka-mysql-ubuntu-16-04">УСТАНОВКА MYSQL В UBUNTU</a>
<br> Краткое описание
```
sudo apt install mysql-server
sudo mysql_secure_installation
```
Git
```
apt install git-core
```
virtualenv
```
apt install python3-venv
```
gunicorn
```
apt install gunicorn
```
#### Настраиваем виртуальное окружение
При необходимости, для установки менеджера пакетов pip выполняем команду:
```
apt install python3-pip
```
Создаем и активируем виртуальное окружение:
```
mkdir /opt/venv
python3 -m venv /opt/venv/habr_env
source /opt/venv/habr_env/bin/activate
```
Создаем директории под логи:
```
mkdir /opt/venv/habr_env/run/
mkdir /opt/venv/habr_env/logs/
mkdir /opt/venv/habr_env/logs/nginx/
```
Устанавливаем права:
```
chown -R hh /opt/venv/habr_env
```
Клонируем репозиторий:
```
git clone https://github.com/Scrum-GB-Habr/gb_habr_agile_scrum.git
cd venv/habr_env/gb_habr_agile_scrum/habr
```
Ставим зависимости:
```
pip install -r requirements.txt
```
#### «MySQL» Запускаем интерпретатор команд сервера:
```
sudo mysql
```
Создаем BD
```
> CREATE DATABASE habr;
```
Создаем пользователя 
<br>
username и password - замените в settings.py и в коде ниже на свои

```
> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
> GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;
```
#### Настройка проекта

Создаем суперпользователя(админа)

```
(venv) $ python manage.py createsuperuser
```
к примеру (логин/пароль): admin:123
#### Выполнение миграций и сбор статических файлов проекта
Выполняем миграции:
```
(venv) $ python manage.py migrate
```
Собираем статику:
```
(venv) $ python manage.py collectstatic
```

#### Тест запуска
```
(venv) $ python manage.py runserver
```
#### Назначение прав доступа
```
chown -R habr /home/habr_env/
chmod -R 755 /home/habr_env/gb_habr_agile_scrum/habr
```
Настроим параметры службы «gunicorn»
```
sudo nano /etc/systemd/system/gunicorn.service


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=USER_NAME
Group=www-data
WorkingDirectory=/home/habr_env/gb_habr_agile_scrum/habr
ExecStart=/home/habr_env/gb_habr_agile_scrum/habr/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/habr_env/gb_habr_agile_scrum/habr/habr.sock habr.wsgi

[Install]
WantedBy=multi-user.target

```
Активирование и запуск сервиса
```
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```
Настройки параметров для nginx
```
sudo nano /etc/nginx/sites-available/habr.conf

server {
    listen 80;
    server_name <*.*.*.*>; ### server_name необхоимо написать ip-адрес сервера

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/habr_env/gb_habr_agile_scrum/habr;
    }

    location /media/ {
        root /home/habr_env/gb_habr_agile_scrum/habr;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/habr_env/gb_habr_agile_scrum/habr/habr.sock;
    }
}
```
Перезапускаем службу «nginx»
```
sudo systemctl restart nginx
```
#### Активировируем сайт
```
sudo ln -s /etc/nginx/sites-available/habr /etc/nginx/sites-enabled
```

##### После этого в браузере можно ввести ip-адрес сервера и откроется проект.


### Примечания для разработчиков
В проекте при миграциях заполняется БД:
 - Пользователи: admin, user, user2
    пароль у всех 123
 - Группа "Модераторы"
 - Категории
 - Несколько статей


**ВНИМАНИЕ!** Теперь не все миграции можно удалять. Обязательно оставляем 0001 и 0002 в main и authapp. 
