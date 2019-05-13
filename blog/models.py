from django.db import models

# Create your models here.
from django.db.models import Model


class Article(Model):
    """博客表"""
    name = models.CharField(max_length=256, verbose_name="博客名")
    abstract = models.TextField(verbose_name="摘要")
    content = models.TextField(verbose_name="博客内容")
    read_num = models.IntegerField(verbose_name="阅读数", default=0)
    comment_num = models.IntegerField(verbose_name="评论数", default=0)
    image = models.FileField(upload_to="static/user_data/blog_img", verbose_name="博客图片")
    time = models.DateField(auto_now_add=True, verbose_name="发布日期")
    tips = models.BooleanField(default=False, verbose_name="是否在首页展示")
    # 标签一对多
    gategory = models.ForeignKey(to="Category", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="文章分类")

    def __str__(self):
        return self.name


class Category(Model):
    """分类"""
    name = models.CharField(max_length=256, verbose_name="标签名")
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(Model):
    """评论"""
    user = models.CharField(max_length=128, verbose_name="用户名")
    avatar = models.CharField(max_length=128, verbose_name="头像", default="/static/user_data/avatar.jpg")
    content = models.TextField(verbose_name="评论内容")
    time = models.DateField(auto_now_add=True, verbose_name="评论日期")
    # 外键关联文章
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name="文章id")

    def __str__(self):
        return self.content
