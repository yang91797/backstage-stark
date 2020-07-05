from django.test import TestCase

# Create your tests here.


class SearchGroupRow(object):
    def __init__(self):
        """

        :param title: 表字段名称，用于显示组合搜索的列名称
        :param queryset_or_tuple: 组合搜索关联获取到的数据
        :param option: 配置
        """
        self.title = "title"      # 字段名称

    def __iter__(self):
        yield '<div class="whole">'
        yield self.title
        yield '</div>'
        yield '<div class="others">'


