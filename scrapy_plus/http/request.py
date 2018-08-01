"""封装Request对象"""


class Request(object):
    """框架内内置请求对象，设置请求信息"""
    def __init__(self,url,method='GET', headers=None, data=None):
        self.url = url #请求地址
        self.method = method #请求方法
        self.headers = headers #请求头
        self.data = data  #请求体





