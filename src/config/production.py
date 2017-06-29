from .base import *


SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://site_engine_rest:site12345@10.34.52.49:5432/site_engine_rest'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True