from django.urls import path
from . import views


app_name = "news"
urlpatterns = [
    path("", views.home, name="index"),
    path("list/<int:subset_id>/<int:page_num>", views.news_list, name="list"),
    path("detail/<int:id>/", views.news_detail, name="detail"),
    path("station/<int:id>/", views.station_detail, name="station"),
]
