from django.contrib import admin
from .models import User, Subset, Article


admin.site.site_header = "芜湖市鸠江区沈巷镇水利站后台管理系统"
admin.site.index_title = "后台"

admin.site.register(User)
admin.site.register(Subset)
admin.site.register(Article)
