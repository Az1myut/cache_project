new_book = {
    'subject': """Регистрация новой книги""",
    'message': """Сообщение от сервиса Book. Создание новой записи.""",
    "html_message": """<h2>Здравствуйте</h2><p>Произошла регистрация новой книги.</p>"""
}

saved_book = {
    'subject': """Книга {name} была сохранена""",
    'message': """Сообщение от сервиса Book. Сохранение записи.""",
    "html_message": """<h2>Здравствуйте</h2><p>Произошло сохранение книги {name}.</p>"""
}

testing_message = {
    'subject': """Книга {name}. Это сообщение для тестирования.""",
    'message': """Сообщение от сервиса Book. Тестирование сохранения.""",
    "html_message": """<h2>Здравствуйте</h2><p>Производится тестирование сохранение книги {name}.</p>"""
}

deleted_book = {
    'subject': """Книга {name} была удалена""",
    'message': """Сообщение от сервиса Book. Удаление записи.""",
    "html_message": """<h2>Здравствуйте</h2><p>Произошло удаление книги {name}.</p>"""
}

from_email = "my_email@my.me"

recipient_list = ["recipient@recipient.email"]
testing_email = "testing_email@testing_email.email"
