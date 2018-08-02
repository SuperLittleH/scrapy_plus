"""引擎组件"""


from scrapy_plus.http.request import Request

from scrapy_plus.core.spider import Spider
from scrapy_plus.core.downloader import Downloader
from scrapy_plus.core.scheduler import Scheduler
from scrapy_plus.core.pipeline import Pipeline


class Engine():

    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()


    def start(self):
        self._start_engine()


    def _start_engine(self):
        # 1.爬虫模块发出初始请求
        start_request = self.spider.start_request()

        # 2.把初始请求添加给调度器
        self.scheduler.add_request(start_request)

        # 3.从调度器获取请求对象，交给下载器发起请求，获取一个响应对象
        request = self.scheduler.get_request()

        # 4.利用下载器发起请求
        response = self.downloader.get_response(request)

        # 5.利用爬虫的解析响应的方法，处理响应得到结果
        result = self.spider.parse(response)

        # 6.判断结果
        if isinstance(result,Request):
            # 6.1如果是请求对象那么交给调度器
            self.scheduler.add_request(result)

        else:
            # 6.2否则在交给管道处理
            self.pipeline.process_item(result)