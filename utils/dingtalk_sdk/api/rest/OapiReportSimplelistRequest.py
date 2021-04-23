"""
Created by auto_sdk on 2019.12.18
"""
from api.base import RestApi


class OapiReportSimplelistRequest(RestApi):
    def __init__(self, url=None):
        RestApi.__init__(self, url)
        self.cursor = None
        self.end_time = None
        self.size = None
        self.start_time = None
        self.template_name = None
        self.userid = None

    def getHttpMethod(self):
        return 'POST'

    def getapiname(self):
        return 'dingtalk.oapi.report.simplelist'
