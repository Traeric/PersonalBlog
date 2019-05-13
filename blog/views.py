import json

from django.shortcuts import render, HttpResponse
from django.views import View
from . import models
import datetime

# Create your views here.


def dashboard(request):
    # 加载最热门文章
    hot_article = models.Article.objects.order_by("-read_num")
    hot_article = hot_article if len(hot_article) < 6 else hot_article[:6]
    # 加载推荐文章
    recommend_article = models.Article.objects.filter(tips=True)
    # 加载最新文章
    new_article = models.Article.objects.order_by("-id")
    new_article = new_article if len(new_article) < 5 else new_article[:5]
    # 加载文章分类
    category = models.Category.objects.all()
    data = {
        "hot_article": hot_article,
        "recommend_article": recommend_article,
        "new_article": new_article,
        "category": category,
    }
    return render(request, "dashboard.html", data)


def load_article(request, catagory_id):
    """
    通过分类查找所有的文章
    :param request:
    :param catagory_id:
    :return:
    """
    articles = models.Category.objects.filter(id=catagory_id)[0].article_set.order_by("-id")
    article_data = []
    for article in articles:
        article_data.append({
            "id": article.id,
            "name": article.name,
            "abstract": article.abstract,
            "image": "/" + str(article.image),
            "time": datetime.datetime.strftime(article.time, "%Y-%m-%d"),
        })
    return HttpResponse(json.dumps(article_data))


def article_details(request, article_id):
    """
    文章详细
    :param request:
    :param article_id:
    :return:
    """
    # 加载最新文章
    new_article = models.Article.objects.order_by("-id")
    new_article = new_article if len(new_article) < 5 else new_article[:5]
    # 加载文章分类
    category = models.Category.objects.all()
    # 加载当前文章
    article = models.Article.objects.filter(id=article_id)
    # 加载评论
    comments = models.Comment.objects.filter(article=article[0])
    # 添加阅读量
    article.update(read_num=article[0].read_num + 1)
    data = {
        "new_article": new_article,
        "category": category,
        "article": article[0],
        "comments": comments,
    }
    return render(request, "article.html", data)


def save_comment(request):
    """
    保存评论
    :param request:
    :return:
    """
    article_id = request.POST.get("article_id", None)
    name = request.POST.get("name", None)
    comment = request.POST.get("comment", None)
    msg = ""
    flag = True
    if name.strip() == "":
        msg = "名称不能为空"
        flag = False
    if comment.strip() == "":
        msg = "评论不能为空"
        flag = False
    if flag:
        # 保存评论
        comment = models.Comment.objects.create(user=name, content=comment, article_id=article_id)
        # 评论数加一
        article = models.Article.objects.filter(id=article_id)
        comment_num = article[0].comment_num + 1
        article.update(comment_num=comment_num)
        return HttpResponse(json.dumps({
            "flag": flag,
            "avatar": comment.avatar,
            "name": comment.user,
            "comment": comment.content,
        }))
    return HttpResponse(json.dumps({
        "flag": flag,
        "msg": msg,
    }))


class AboutMe(View):
    """关于我"""

    def get(self, request):
        return render(request, "about_me.html")


def archives(request):
    """
    归档页面
    :param request:
    :return:
    """
    date_list = models.Article.objects.dates('time', 'year', 'DESC')
    return render(request, "archives.html", {
        "date_list": date_list,
    })
