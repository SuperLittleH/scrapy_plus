"""下载器组件"""

import requests
from scrapy_plus.http.response import Response


class Downloader():
    """根据请求对象，发起http或者https请求,拿到响应并返回"""
    def get_response(self,request):
        """发起请求获取响应的方法"""
        #1.根据请求对象，发起请求，获取响应
        #判断请求方法
        if request.method.upper() == 'GET':
            resp = requests.get(request.url, headers=request.headers)

        elif request.method.upper() == 'POST':
            resp = requests.post(request.url, headers= request.headers,data=request.data)
        else:
            # 如果不是get或者post请求抛出异常
            raise  Exception('不支持的请求方法')
        # 2.构建响应对象，并返回
        return Response(url=resp.url, status_code=resp.status_code, headers=resp.headers, body=resp.content)

