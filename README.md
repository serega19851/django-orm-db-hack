# Файл для проекта e-diary 
Позволяет исправлять базу данных.

### Инструкция проекта
Зайдите по ссылки (https://github.com/serega19851/django-orm-db-hack),
клонируйте проект к себе локально.

Положите файл scripts.py рядом с файлом manage.py проекта e-diary

### Инструкция как пользоваться файлом.
Внутри проекта e-diary запускаете django shell 
```
python django shell
```
Далее вам предстоит импортировать скрипты из scripts.py в django shell
```
from e-diary.scripts import fix_marks, remove_chastisements, create_commendation
```
После этого вызываем функцию fix_marks с обязательным аргументом. Функция позволяет исправлять оценки 2, 3 на 5.
```
fix_marks("ваша фамилия имя или очество ученика")
```
Вызывая функцию remove_chastisements с обязательным аргументом, удаляет замечания от учителей.
```
remove_chastisements("ваша фамилия имя или очество ученика")
```
Вызывая функцию create_commendation с обязательными двумя аргументами(ФИО школьника, Школьный предмет)
, создает похвалу от учителей.
```
create_commendation("ваша фамилия имя или очество ученика", "Музыка например" )
```
### Зайдите на сайт электронного дневника
- Оценки исправлены?
- Замечания исчезли?
- Появилась похвала от учителя?