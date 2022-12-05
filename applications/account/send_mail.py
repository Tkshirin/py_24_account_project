from django.core.mail import send_mail

def send_hello(email):
    send_mail(
        'Вас приветствует крутой сайт', # title
        'привет, как дела?', #body
        'toktobekkyzysirin@gmail.com', # from
        [email], # to
    )