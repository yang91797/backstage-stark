from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules


class StarkConfig(AppConfig):
    name = 'stark'

    def ready(self):
        """
        自动去每一个已注册的app下找到stark.py,然后执行
        :return:
        """
        autodiscover_modules('stark')
