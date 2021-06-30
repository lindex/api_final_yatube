#  api_final_yatube

REST API для небольшой социальной сети yatube в рамках [курса яндекс практикум](https://praktikum.yandex.ru/backend-developer "курса яндекс практикум").
Реализованы подписки, комментарии, посты, группы.


## Установка
1. Клонируйте репозиторий
`git clone https://github.com/lindex/api_final_yatube` 

2. Установите виртуальное окружение и установить зависимости `requirements.txt`
`pip install -r requirements.txt
`
3. Выполнить миграции в проекте
`python manage.py makemigrations`
`python manage.py migrate`

4. Запустите сервер
`python manage.py runserver`

### Документация
Документация API доступна по адресу http://localhost:8000/redoc/

### Работа с проектом
Для работы внутри проекта потребуется JWT token.
Чтобы его получить нужно выполнить POST-запрос http://localhost:8000/api/v1/token/ передав поля `username` и `password`.

Ответ API:
```json
{
    "access": "ХХХХХХХХХХХ",
    "refresh": "ХХХХХХХХХХХХ"
}
```
`access`  - токен для доступа к запросам
`refresh`  - токен для обновления `access`

При отправке запросов токен `access` должен передаваться в формате 
` Authorization: Bearer <token>`


### Запросы
`GET` Запрос для получения списка **постов**:

 url : http://127.0.0.1:8000/api/v1/posts/
Authorization: `Bearer Token`
Token: `<token>`

Ответ
```json
[
    {
        "id": 1,
        "author": "adminMark",
        "text": "Best post",
        "pub_date": "2021-06-29T12:39:34.065610Z",
        "group": null
    }
]
```
Responcee API_Yatube: 200 OK

