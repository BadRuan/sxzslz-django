from django.contrib import admin
from .models import User, Subset, Article


admin.site.register(User)
admin.site.register(Subset)
admin.site.register(Article)
