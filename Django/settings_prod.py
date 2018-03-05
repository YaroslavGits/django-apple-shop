DEBUG = False

ALLOWED_HOSTS = ["appleshopdjango.pythonanywhere.com", ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'appleshopdjango$my_project',
        'USER': 'appleshopdjango',
        'PASSWORD': 'DB_passw0rd',
        'HOST': 'appleshopdjango.mysql.pythonanywhere-services.com',   # Or an IP Address that your DB is hosted on
    }
}
