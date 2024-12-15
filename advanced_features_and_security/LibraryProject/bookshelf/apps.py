from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'
    def ready(self):
        # Import signals after the app is ready to avoid circular import issues
        import bookshelf.signals
