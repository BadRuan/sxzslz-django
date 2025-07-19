from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
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
    return render(request, "news/list.html", context)


def news_detail(request, id: int):
    article = get_object_or_404(Article, pk=id)
    article.read += 1
    article.save()
    context = {"article": article}
    return render(request, "news/detail.html", context)


def home(request):
    context = {
        "station_list": stations,
        "news_list": Article.objects.filter(subset_id=1).order_by("-create_time")[:10],
        "notice_list": Article.objects.filter(subset_id=2).order_by("-create_time")[
            :10
        ],
        "files_list": Article.objects.filter(subset_id=4).order_by("-create_time")[:4],
    }
    return render(request, "news/home.html", context)


def station_detail(request, id: int):
    count: int = len(stations)
    if id < 1 or id > count:
        return Http404("")
    context = {
        "station": stations[id - 1],
    }
    return render(request, "news/station_detail.html", context)
