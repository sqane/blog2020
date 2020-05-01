Инструкция по разверте проекта:
1.Создать и поключить виртуальное окружение (python 3.6)
2.В корне проекта установить requirements (pip install -r requirements.txt)
3.В blog/settings.py подключить пустую БД (:78)
4.Подменить путь для статики в  blog/settings.py (STATICFILES_DIRS = ['полный путь к проекту/static'] 
5.Выполнить миграции (python manage.py migrate)
6.Запустить django server (python manage.py runserver либо файл manage.py запустить в отладке)

Корневый url первая страница, url  создания поста /new_post/