from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "news"
    verbose_name: str = "文章管理"
