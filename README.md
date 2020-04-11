# Mem base

Мемная база

## About Mem base

Mem base - это личный проект, созданный с целью хранения мемов, мемасиков, мэмосов.
У каждого мема есть собсвенная страница, название, тэги и, естественно, картинка.


## Requirements

  + Python 3.5 (рекомендую использовать в virtualenvwrapper)
  + Django 2.2
  + environ ([link](https://github.com/joke2k/django-environ))

## Installing

`$ git clone https://github.com/velgi/mem_base`  
`$ mkdir -p mem_base/media/images` (папка для хранения изображений)  
`$ workon django_env` (если используется virtualenvwrapper)  
`$ pip3 install django-environ`  
`$ python3 manage.py makemigrations`  
`$ python3 manage.py migrate`  

## Details

  + Параметры `SECRET_KEY` , `ALLOWED_HOSTS` и `DEBUG` задаются в файле mem_base/.env , который, в свою очередь, подключается библиотекой environ в mem_base/settings.py. Формат параметров соответствует изначальному формату в settings.py , но без дополнительныйх символов типа `'` или же явного объвления массива `[]`;
  + Все тэги при сохранении переводтся в нижний регистр ;
  + Поддерживаемый формат изображений - jpg ;
  + Работа проверялась исключительно встроенными средствами `python3 manage.py runserver 0.0.0.0:8001`, планируетя перевод на nginx+uwsgi
