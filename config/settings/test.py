from .local import *

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': {'ENGINE': 'django.db.backends.sqlite3'}
}
