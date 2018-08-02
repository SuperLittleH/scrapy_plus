"""爬虫组件封装"""
from scrapy_plus.item import Item #导入Item对象
from scrapy_plus.http.request import Request #导入Request对象


class Spider(object):
    """
    1.构建请求信息，也就是生成请求对象
    2.解析响应对象，返回数据对象或者新的请求对象
    """

    start_url = 'http://www.baidu.com' #默认初始请求地址

    def start_request(self):
        """构造初始请求对象并返回"""
        return Request(self.start_url)


    def parse(self,response):
        """
        解析请求
        并返回新的请求对象，或者数据对象
        :param response:
        :return:
        """
        return Item(response.body) #返回item对象