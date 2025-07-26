from django.db.models.base import Model as Model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import View, DetailView
from .models import Article, Subset
from .station import stations


def news_list(request, subset_id: int, page_num: int):
    per_page: int = 15  # 每页数量
    subset_list = Subset.objects.all()
    article_list = Article.objects.filter(subset_id=subset_id).order_by("-create_time")
    paginator = Paginator(article_list, per_page)
    page_obj = paginator.get_page(page_num)
    context = {
        "subset_list": subset_list,
        "subset_primary": get_object_or_404(Subset, pk=subset_id),
        "article_list": page_obj,
        "subset_id": subset_id,
        "page_num": {"pre_num": page_num - 1, "next_num": page_num + 1},
    }
    return render(request, "news/news_list.html", context)


class NewsDetailView(DetailView):
    template_name: str = "news/news_detail.html"
    context_object_name: str = "article"
    model = Article

    def get_object(self, queryset=None) -> Model:
        id = self.kwargs.get("id")
        article = get_object_or_404(self.model, pk=id)
        article.read += 1  # type: ignore
        article.save()
        return article


def home(request):
    context = {
        "station_list": stations,
        "news_list": Article.objects.order_by("-create_time")[:6],
    }
    return render(request, "news/home_page.html", context)


class StationDetailView(View):
    template_name: str = "news/station_detail.html"

    def get(self, request, id: int):
        count: int = len(stations)
        if id < 1 or id > count:
            return HttpResponseRedirect("/")
        context = {
            "station": stations[id - 1],
        }
        return render(request, self.template_name, context)
