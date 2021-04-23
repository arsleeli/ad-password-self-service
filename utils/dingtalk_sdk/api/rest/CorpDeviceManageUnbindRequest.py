"""
Created by auto_sdk on 2018.07.25
"""
from api.base import RestApi


class CorpDeviceManageUnbindRequest(RestApi):
    def __init__(self, url=None):
        RestApi.__init__(self, url)
        self.device_id = None
        self.device_service_id = None

    def getHttpMethod(self):
        return 'POST'

    def getapiname(self):
        return 'dingtalk.corp.device.manage.unbind'
