#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse
from django.conf.urls import url
from stark.service.v1 import site, StarkHandler, get_choice_text, StarkModelForm, Option
from app01 import models


class DepartHandler(StarkHandler):

    list_display = ['id', 'title', StarkHandler.display_edit, StarkHandler.display_del]

    def extra_urls(self):
        """
        额外增加URL
        :return:
        """
        return [
            url(r'^detail/(\d+)/$', self.detail_view)
        ]

    def detail_view(self, request, pk):
        return HttpResponse('详情页面')


site.register(models.Depart, DepartHandler)


class MyOption(Option):
    def get_db_condition(self, request, *args, **kwargs):
        return {}           # {'id__gt': request.GET.get('nid')}


class UserInfoModelForm(StarkModelForm):
    """
    自定制添加用户时显示的列
    """
    class Meta:
        model = models.UserInfo
        fields = ['name', 'gender', 'classes', 'age', 'email']


class UserInfoHandler(StarkHandler):

    # 定制页面显示的列
    list_display = [
        StarkHandler.display_checkbox,
        'id',
        'name',
        get_choice_text('性别', 'gender'),
        get_choice_text('班级', 'classes'),
        'age', 'email', 'depart',
        StarkHandler.display_edit,
        StarkHandler.display_del
    ]

    per_page_count = 10     # 每页显示数据个数
    has_add_btn = True      # 是否显示添加按钮

    order_list = ['id']     # 数据排序方式

    # 姓名中或邮箱中含有关键字 不加__contains就是精确查找
    search_list = ['name__contains', 'email__contains']

    action_list = [StarkHandler.action_multi_delete]    # 批量删除

    # model_form_class = UserInfoModelForm      #   自定制 添加/编辑 页面显示的字段
    # def save(self, form, is_update=False):
    #     form.instance.depart_id = 1
    #     form.save()

    search_group = [
        Option('gender', is_multi=True),
        MyOption('depart', db_condition={'id__gt': 2}),      # db_condition:ORM的筛选条件

        # Option('gender', text_func=lambda field_object: '666' )
    ]

    # def get_urls(self):
    #     """
    #     修改或重写URL
    #     :return:
    #     """
    #     patterns = [
    #         url(r'^list/$', self.changelist_view),
    #         url(r'^add/$', self.add_view),
    #     ]
    #
    #     return patterns


site.register(models.UserInfo, UserInfoHandler)

