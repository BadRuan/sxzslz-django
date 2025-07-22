from django.urls import path
from .views import NewsDetailView, news_list, StationDetailView, home


app_name = "news"
urlpatterns = [
    path("", home, name="index"),
    path("list/<int:subset_id>/<int:page_num>", news_list, name="list"),
    path("detail/<int:id>/", NewsDetailView.as_view(), name="detail"),
    path("station/<int:id>/", StationDetailView.as_view(), name="station"),
]
