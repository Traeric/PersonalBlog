from django import template
from blog import models

register = template.Library()


@register.simple_tag
def category_article_num(category_id):
    """
    计算某个分类下的文章数
    :param category_id:
    :return:
    """
    return models.Category.objects.filter(id=category_id)[0].article_set.count()


@register.simple_tag
def load_article_by_date(date):
    """
    通过时间加载文章
    :param date:
    :return:
    """
    year = str(date)[:4]
    articles = models.Article.objects.filter(time__year=year)
    return articles


@register.simple_tag
def check_style(loop_count):
    """
    循环次数
    :param loop_count:
    :return:
    """
    style_list = ['list-group-item-success', 'list-group-item-info', 'list-group-item-warning',
                  'list-group-item-danger']
    return style_list[loop_count % 4]
