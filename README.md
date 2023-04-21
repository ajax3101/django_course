# django_course
курсы Django от CyberBionic


[Выполнено задание №2:](https://github.com/ajax3101/django_course/blob/main/task/Django_UA_%20DZ_2.pdf)

Завдання 1 - папка dz_2  

Завдання 2 - папка dz_2_2

Завдання 3 - папка weather

Клонируем репо

```bash
git clone https://github.com/ajax3101/django_course.git
```

Устанавливаем и активируем виртуальное окружение

```bash
    python3 -m venv venv
    . venv/bin/activate
 ```

Устанавливаем модули:
загружаем файл с зависимостями проекта

```bash
 pip install -r requirements.txt
```

Запус приложения

```bash
 python manage.py makemigrations 
 python manage.py migrate
 python manage.py runserver 
```
