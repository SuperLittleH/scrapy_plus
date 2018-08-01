"""item对象"""


class Item(object):
    """框架内置item对象"""
    def __init__(self,data):
        #data表示传入的数据
        self._data = data #设置为简单的私有属性



    @property
    def data(self):
        """对外提供data进行访问，一定成都达到保护的作用"""
        return self._data