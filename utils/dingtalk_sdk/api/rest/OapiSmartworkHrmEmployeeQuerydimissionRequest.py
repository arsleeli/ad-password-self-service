"""
Created by auto_sdk on 2020.12.09
"""
from api.base import RestApi


class OapiSmartworkHrmEmployeeQuerydimissionRequest(RestApi):
    def __init__(self, url=None):
        RestApi.__init__(self, url)
        self.offset = None
        self.size = None

    def getHttpMethod(self):
        return 'POST'

    def getapiname(self):
        return 'dingtalk.oapi.smartwork.hrm.employee.querydimission'
