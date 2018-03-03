DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database',
        'USER': 'usershop',
        'PASSWORD': 'security_database_root',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
